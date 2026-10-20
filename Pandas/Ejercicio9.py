
import pandas as pd

# Crear el inventario
inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(inventario)

# Guardamos la tabla en un archivo CSV
df.to_csv("inventario.csv", index=False)

# Se leen los datos guardados
datos = pd.read_csv("inventario.csv")

# Mostramos los datos y comprobar si son iguales
print(datos)
print("¿Los datos son iguales?", df.equals(datos))
