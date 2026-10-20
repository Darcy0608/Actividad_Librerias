import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(inventario)


print( df.head())        # Mostramos las primeras filas
print(df.shape)          # Cantidad de filas y columnas
print(df.columns)        # Nombres de las columnas
print(df.describe())     # Mostrar las estadísticas de los datos numericos
