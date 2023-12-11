import matplotlib.pyplot as plt
import numpy as np

years = list(range(2013, 2024))
celery = [ 0.0000523677,0.0000503766 ,0.0000509536 ,0.0000474120 ,0.0000446546 , 0.0000442647,0.0000442635 , 0.0000356475, 0.0000349109, 0.0000341635, 0.0000336187]
luigi = [ 0.0001692650, 0.0001516566, 0.0001190668,0.0001076344 ,0.0001079223 ,0.0000934799 ,0.0000821503 ,0.0000823303 , 0.0000816567,0.0000816132 , 0.0000813457]
matplotlib_vals = [ 0.0000186491,0.0000154261 ,0.0000128055 ,0.0000124880 , 0.0000123172,0.0000115734 ,0.0000114838 ,0.0000115299 ,0.0000116322 ,0.0000114988 ,0.0000115271 ]
numpy_vals = [ 0.0000281420,0.0000320683 ,0.0000316493 ,0.0000301434 ,0.0000291420 ,0.0000161477 ,0.0000154370 , 0.0000154548,0.0000168667 ,0.0000161033 ,0.0000154470 ]
pandas_vals = [0.0000417407,0.0000428530 ,0.0000182703 ,0.0000223627 , 0.0000209742, 0.0000157478, 0.0000091596,0.0000049561 ,0.0000043514 ,0.0000038855 ,0.0000036200  ]
scikit_learn_vals = [0.0000167952, 0.0000169195, 0.0000158848, 0.0000154167, 0.0000152338, 0.0000129528, 0.0000118070, 0.0000102174, 0.0000085737, 0.0000083726, 0.0000079638]
scrapy_vals = [0.0000743652, 0.0000766920, 0.0000775527, 0.0000587259, 0.0000767416, 0.0000757424, 0.0000447573, 0.0000484962, 0.0000445067, 0.0000387124, 0.0000342839]

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

plt.title('Z-Score Normalized refactor code smell Occurrences per LOC for Repositories (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Z-Score Normalized Value')
plt.legend()
plt.grid(True)
plt.show()
