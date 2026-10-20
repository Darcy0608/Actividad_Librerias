
import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

# Convertimos los datos en una tabla
df = pd.DataFrame(inventario)

# Filtramos los productos con menos de 10 unidades
productos_reponer = df[df["stock"] < 10]

# Se muestran los productos encontrados
print("Los productos a reponer con stock menor a 10 son: ", productos_reponer)