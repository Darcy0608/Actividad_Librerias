import numpy as np

# Creamos un array con las notas
notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

# Mostramos los resultados
print("Las notas son:", notas)
print("El Promedio es de:", np.mean(notas))
print("El Maximo es:", np.max(notas))
print("El Minimo es:", np.min(notas))
print("Desviacion estandar:", np.std(notas))