
import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(inventario)

# Se ordenan los productos del mas caro al mas barato
ordenado = df.sort_values("precio", ascending=False)
print(ordenado)

# Mostramos el precio promedio
print("El precio promedio es:", df["precio"].mean())
