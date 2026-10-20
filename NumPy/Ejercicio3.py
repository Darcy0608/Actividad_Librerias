import numpy as np

# Creamos el array con las temperaturas en grados Celsius
celsius = np.array([18, 22, 25, 19, 30])

# Convertimos a Fahrenheit
fahrenheit = (celsius * (9/5) + 32)

# Mostrams las temperaturas convertidas
print("Temperaturas en Fahrenheit:", fahrenheit)