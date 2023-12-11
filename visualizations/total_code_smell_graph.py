import matplotlib.pyplot as plt
import numpy as np
years = list(range(2013, 2024))
celery =[0.0005802711, 0.0005605184, 0.0005575769, 0.0005674519, 0.0005563367, 0.0005546711, 0.0005546560, 0.0005583336, 0.0005486063, 0.0005320213, 0.0005231075]
luigi = [0.0016586712, 0.0011807019, 0.0008796947, 0.0008033228, 0.0008008137, 0.0007203454, 0.0006838848, 0.0006840958, 0.0006779258, 0.0006754130, 0.0006710080]
matplotlib_vals =[0.0001477326, 0.0001183963, 0.0001073755, 0.0001047116, 0.0001041832, 0.0000946867, 0.0000943211, 0.0000947655, 0.0000951260, 0.0000941442, 0.0000942886]
numpy_vals = [0.0002766917, 0.0002567613, 0.0002549371, 0.0002521960, 0.0002516369, 0.0001932690, 0.0001901617, 0.0001899951, 0.0001999849, 0.0001969785, 0.0001901243]
pandas_vals = [0.0003686232, 0.0004065018, 0.0001681960, 0.0002190186, 0.0001916762, 0.0001382030, 0.0001005322, 0.0000733266, 0.0000646045, 0.0000611731, 0.0000584275]
scikit_learn_vals =[0.0002232937, 0.0002244195, 0.0002101745, 0.0002091826, 0.0002098772, 0.0001931829, 0.0001822230, 0.0001634483, 0.0001330034, 0.0001274499, 0.0001131586]
scrapy_vals = [0.0007126502, 0.0006837377, 0.0007230143, 0.0006168467, 0.0007231237, 0.0006788390, 0.0004844249, 0.0004995495, 0.0004786811, 0.0004577392, 0.0004005154]

# Z-score normalization
celery_normalized = (np.array(celery) - np.mean(celery)) / np.std(celery)
luigi_normalized = (np.array(luigi) - np.mean(luigi)) / np.std(luigi)
matplotlib_normalized = (np.array(matplotlib_vals) - np.mean(matplotlib_vals)) / np.std(matplotlib_vals)
numpy_normalized = (np.array(numpy_vals) - np.mean(numpy_vals)) / np.std(numpy_vals)
pandas_normalized = (np.array(pandas_vals) - np.mean(pandas_vals)) / np.std(pandas_vals)
scikit_learn_normalized = (np.array(scikit_learn_vals) - np.mean(scikit_learn_vals)) / np.std(scikit_learn_vals)
scrapy_normalized = (np.array(scrapy_vals) - np.mean(scrapy_vals)) / np.std(scrapy_vals)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(years, celery_normalized, marker='o', label='Celery', linestyle='-')
plt.plot(years, luigi_normalized, marker='s', label='Luigi', linestyle='-')
plt.plot(years, matplotlib_normalized, marker='^', label='Matplotlib', linestyle='-')
plt.plot(years, numpy_normalized, marker='v', label='NumPy', linestyle='-')
plt.plot(years, pandas_normalized, marker='D', label='Pandas', linestyle='-')
plt.plot(years, scikit_learn_normalized, marker='p', label='scikit-learn', linestyle='-')
plt.plot(years, scrapy_normalized, marker='*', label='Scrapy', linestyle='-')

plt.title('Z-Score Normalized total code smell Occurrences per LOC for Repositories (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Z-Score Normalized Value')
plt.legend()
plt.grid(True)
plt.show()
