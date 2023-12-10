import git
import os
import subprocess
from datetime import datetime

def analyze_commit(commit, output_folder):
    commit_date = commit.authored_datetime.strftime('%Y%m%d_%H%M%S')
    commit_folder = os.path.join(output_folder, commit.authored_datetime.strftime('%Y_%m_%d'))
    os.makedirs(commit_folder, exist_ok=True)
    p_files_folder = os.path.join(commit_folder, "p_files")
    py_results_folder = os.path.join(commit_folder, "py_results")
    os.makedirs(p_files_folder, exist_ok=True)
    os.makedirs(py_results_folder, exist_ok=True)
    print(f"Processing commit {commit.hexsha} from {commit.authored_datetime}")
    total_lines = 0
    program_counter = 1
    for item in commit.tree.traverse():
        if item.type == "blob" and item.path.endswith(".py"):
            file_path = os.path.join(p_files_folder, f"program_{program_counter}.py")
            with open(file_path, "w") as file:
                file.write(item.data_stream.read().decode("utf-8"))
            result_path = os.path.join(py_results_folder, f"program_{program_counter}_pylint.txt")
            pylint_command = ["pylint", file_path, "--output-format=text"]
            with open(result_path, "w") as result_file:
                subprocess.run(pylint_command, stdout=result_file)
            program_counter += 1
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                total_lines += len(lines)
    with open(os.path.join(commit_folder, "LOC.txt"), "w") as loc_file:
        loc_file.write(str(total_lines))

def process_yearly_commits(repo_url):
    repo_name = repo_url.split("/")[-1].split(".")[0]
    repo = git.Repo.clone_from(repo_url, repo_name)
    processed_years = set()

    for commit in repo.iter_commits():
        commit_year_month_day = commit.authored_datetime.strftime('%Y_%m_%d')
        if commit_year_month_day[:4] not in processed_years:
            analyze_commit(commit, repo_name)
            processed_years.add(commit_year_month_day[:4])
    repo.git.rev_parse("--abbrev-ref", "HEAD")
    repo.close()

if __name__ == "__main__":
    repo_url = input("Enter the repository URL: ")
    process_yearly_commits(repo_url)
