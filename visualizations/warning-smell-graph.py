import matplotlib.pyplot as plt
import numpy as np
years = list(range(2013, 2024))
celery =[0.001367158, 0.001331080, 0.001313960, 0.001104194, 0.001097912, 0.001109112, 0.001109082, 0.001187962, 0.001170615, 0.001167557, 0.001154007]
luigi = [0.0002655384, 0.0001943177, 0.0001234396, 0.0001100141, 0.0001093342, 0.0001005101, 0.0000970688, 0.0000971563, 0.0000966800, 0.0000962143, 0.0000951758]
matplotlib_vals = [0.0000378939, 0.0000327325, 0.0000302892, 0.0000290860, 0.0000290101, 0.0000252599, 0.0000250271, 0.0000252201, 0.0000252355, 0.0000250833, 0.0000251077]
numpy_vals = [0.0000548791, 0.0000500629, 0.0000492053, 0.0000530183, 0.0000531849, 0.0000499539, 0.0000518100, 0.0000518871, 0.0000514845, 0.0000532045, 0.0000519123]
pandas_vals = [0.0000790216, 0.0000959953, 0.0000413636, 0.0000500646, 0.0000464249, 0.0000343435, 0.0000248881, 0.0000180408, 0.0000156737, 0.0000150148, 0.0000152381]
scikit_learn_vals = [0.0000336246, 0.0000338561, 0.0000316857, 0.0000323846, 0.0000319508, 0.0000271162, 0.0000258766, 0.0000236058, 0.0000206072, 0.0000195019, 0.0000192477]
scrapy_vals = [0.0001541387, 0.0001471497, 0.0001628516, 0.0001307439, 0.0001588754, 0.0001444623, 0.0000614001, 0.0000660663, 0.0000607282, 0.0000591946, 0.0000537935]

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

plt.title('Z-Score Normalized warning code smell Occurrences per LOC for Repositories (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Z-Score Normalized Value')
plt.legend()
plt.grid(True)
plt.show()
