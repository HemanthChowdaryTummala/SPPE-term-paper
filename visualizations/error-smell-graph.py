import matplotlib.pyplot as plt
import numpy as np
years = list(range(2013, 2024))
celery = [0.0001554629, 0.0001541289, 0.0001514629,0.0001424767 ,0.0001425440 ,0.0001454629 ,0.0001454590 ,0.0001404494 ,0.0001477001 ,0.0001390315 ,0.0001360320 ]
luigi = [0.0002498075,0.0001272436,0.0000953284,0.0000790784,0.0000770370,0.0000711366,0.0000623685,0.0000623873,0.0000621653,0.0000615925,0.0000615436]
matplotlib_vals = [0.0000260206,0.0000216264 ,0.0000199467 , 0.0000198422,0.0000197785 ,0.0000181096 , 0.0000180895, 0.0000181576, 0.0000182673,0.0000180246 ,0.0000180071 ]
numpy_vals = [ 0.0000398338, 0.0000329621, 0.0000346849, 0.0000330703,0.0000321396 ,0.0000242384 ,0.0000227517 , 0.0000227090,0.0000253935 ,0.0000233843 ,0.0000227040 ]
pandas_vals = [ 0.0000513677,0.0000694044 , 0.0000254654, 0.0000412128,0.0000303786,0.0000198018 , 0.0000158299,0.0000125496 , 0.0000111018, 0.0000102628, 0.00000928720]
scikit_learn_vals = [ 0.0000445598,0.0000447686,0.0000418380 , 0.0000407917, 0.0000406890, 0.0000350358, 0.0000333577,0.0000307247 , 0.0000252403,0.0000243649 ,0.0000187710]
scrapy_vals = [ 0.0001361752,0.0001117073 ,0.0001206075 ,0.0001050607 , 0.0001232488, 0.0001118579,0.0000965878 ,0.0000990671 ,0.0000958065 , 0.0000906149,0.0000864674]

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

plt.title('Z-Score Normalized error code smell Occurrences per LOC for Repositories (2013-2023)')
plt.xlabel('Year')
plt.ylabel('Z-Score Normalized Value')
plt.legend()
plt.grid(True)
plt.show()
