import numpy as np

# Creamos el array con las ventas
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])

# Aumentamos las ventas un 10 %
ventas = ventas * 1.10

# Mostramos las ventas
print('Las ventas son:', ventas)

# Mostramos las ventas con aumento y el total de la semana
print("Ventas con aumento:", ventas)
print("Total de la semana:", np.sum(ventas))
