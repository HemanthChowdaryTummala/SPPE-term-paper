import os
import sys
from collections import Counter

CATEGORY_NAMES = {'C': 'Convention', 'F': 'Fatal', 'I': 'Information', 'W': 'Warning', 'R': 'Refactor', 'E': 'Error'}

def process_pylint_output(file_path):
    pylint_codes = {name: 0 for name in CATEGORY_NAMES.values()}

    with open(file_path, 'r') as file:
        lines = file.readlines()[1:-3]

    for line in lines:
        parts = line.split(':')
        if len(parts) >= 4:
            pylint_code = parts[3].strip()
            category = pylint_code[0] if pylint_code else ''
            if category in CATEGORY_NAMES:
                pylint_codes[CATEGORY_NAMES[category]] += 1

    return pylint_codes

def process_year_folder(year_folder):
    py_results_folder = os.path.join(year_folder, 'py_results')

    if not os.path.exists(py_results_folder):
        print(f"Warning: py_results folder not found in {year_folder}")
        return

    pylint_code_counter = Counter()
    total_lines_of_code = 0

    for file_name in os.listdir(py_results_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(py_results_folder, file_name)
            codes = process_pylint_output(file_path)
            pylint_code_counter.update(codes)

            loc_file_path = os.path.join(year_folder, 'LOC.txt')
            if os.path.exists(loc_file_path):
                with open(loc_file_path, 'r') as loc_file:
                    total_lines_of_code += int(loc_file.read())

    total_occurrences = sum(pylint_code_counter.values())
    print(f"Total occurrences for \033[1m{os.path.basename(year_folder)}\033[0m: {total_occurrences}")

    for name, count in sorted(pylint_code_counter.items()):
        if total_lines_of_code > 0:
            occurrences_per_loc = count / total_lines_of_code
            print(f"\033[1m{name}\033[0m: {count} occurrences, occurrences per LOC: {occurrences_per_loc:.10f}")

    print(f"Total lines of code: {total_lines_of_code}")
    if total_lines_of_code > 0:
        total_occurrences_per_loc = total_occurrences / total_lines_of_code
        print(f"Total occurrences per LOC: {total_occurrences_per_loc:.10f}")
    print("-" * 40)  # Print dashed line after processing each folder

def main(root_folder):
    if not os.path.exists(root_folder):
        print(f"Error: Folder '{root_folder}' not found.")
        sys.exit(1)

    years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023']

    for year in years:
        folder_name = next((name for name in os.listdir(root_folder) if name.startswith(year)), None)
        if folder_name:
            full_path = os.path.join(root_folder, folder_name)
            print(f"Processing folder: {full_path}")
            process_year_folder(full_path)
        else:
            print(f"Warning: Folder not found for {year}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <root_folder>")
        sys.exit(1)

    root_folder = sys.argv[1]

    main(root_folder)
