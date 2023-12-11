import matplotlib.pyplot as plt
import numpy as np

# Given data
years = list(range(2013, 2024))
celery = [0.0003083244, 0.0002972007, 0.0002961648, 0.0002671438, 0.000259347, 0.000259347, 0.0002540254, 0.0002534405, 0.0002489337, 0.0002420706, 0.000238056]
luigi = [0.0009740603, 0.0007074841, 0.00054186, 0.0005065958, 0.0005065202, 0.0004552187, 0.0004422972, 0.0004422219, 0.0004374237, 0.000435993, 0.0004329429]
matplotlib_vals = [0.0000651689, 0.0000486114, 0.000044334, 0.0000432954, 0.0000430775, 0.0000397438, 0.0000397206, 0.0000398579, 0.000039991, 0.0000395375, 0.0000396466]
numpy_vals = [0.0001534138, 0.0001413343, 0.0001390744, 0.0001356616, 0.0001368819, 0.0001027277, 0.0000999691, 0.0000997511, 0.0001060389, 0.0001060389, 0.000099868]
pandas_vals = [0.0001964932, 0.0001982491, 0.0000830969, 0.0001053785, 0.0000938985, 0.0000683099, 0.0000506546, 0.0000377801, 0.0000334777, 0.00003201, 0.0000302823]
scikit_learn_vals = [0.0001283141, 0.0001288753, 0.000120766, 0.0001205897, 0.0001220036, 0.0001180781, 0.0001111818, 0.0000989004, 0.0000785822, 0.0000752105, 0.0000671762]
scrapy_vals = [0.0003479711, 0.0003481887, 0.0003620025, 0.0003223163, 0.0003642579, 0.0003467764, 0.0002816797, 0.00028592, 0.0002776397, 0.0002692173, 0.0002259706]

#Z-score normalization
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

plt.title('Z-Score Normalized convention code smell Occurrences per LOC for Repositories (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Z-Score Normalized Value')
plt.legend()
plt.grid(True)
plt.show()
