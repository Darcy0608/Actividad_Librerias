
import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(inventario)

# Valor de las existencias
df["valor_inventario"] = df["precio"] * df["stock"]

# Indicamos si se necesita reponer el producto
df["reponer"] = df["stock"] < 10

# Mostramos la tabla completa
print(df)
