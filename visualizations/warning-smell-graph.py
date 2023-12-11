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

def calculate_percentage_change(data):
    initial_value = data[0]
    final_value = data[-1]
    percentage_change = ((final_value - initial_value) / initial_value) * 100
    return percentage_change

# Data for each library
celery_percentage_change = calculate_percentage_change(celery)
luigi_percentage_change = calculate_percentage_change(luigi)
matplotlib_percentage_change = calculate_percentage_change(matplotlib_vals)
numpy_percentage_change = calculate_percentage_change(numpy_vals)
pandas_percentage_change = calculate_percentage_change(pandas_vals)
scikit_learn_percentage_change = calculate_percentage_change(scikit_learn_vals)
scrapy_percentage_change = calculate_percentage_change(scrapy_vals)

# Print the calculated percentage changes
print(f"Celery: {celery_percentage_change:.2f}% decrease")
print(f"Luigi: {luigi_percentage_change:.2f}% decrease")
print(f"Matplotlib: {matplotlib_percentage_change:.2f}% change")
print(f"NumPy: {numpy_percentage_change:.2f}% change")
print(f"Pandas: {pandas_percentage_change:.2f}% decrease")
print(f"Scikit-learn: {scikit_learn_percentage_change:.2f}% decrease")
print(f"Scrapy: {scrapy_percentage_change:.2f}% change")