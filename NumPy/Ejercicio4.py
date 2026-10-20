import numpy as np

# Creamos la matriz con las calificaciones
calificaciones = np.array([
    [8.5, 7.0, 9.0, 8.0],  # Carlos
    [6.0, 7.5, 8.0, 7.0],  # Ana
    [9.0, 8.5, 9.5, 9.0]   # Luis
])

# Calculamos el promedio de cada estudiante
print("El promedio por estudiante es de:", calificaciones.mean(axis=1))

# Calculamos el promedio de cada materia
print("El promedio por materia es de:", calificaciones.mean(axis=0))