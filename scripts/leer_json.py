# leer_json.py - Cargar el reporte JSON de la API
import json
import pandas as pd

# TODO 1 y 2: importa json y pandas, y carga data/ventas.json con json.load
with open("data/ventas.json", encoding="utf-8") as f:
    datos = json.load(f)

# TODO 3: convierte la lista de diccionarios en un DataFrame
# Si el JSON tiene una clave contenedora o estructuras anidadas, json_normalize o DataFrame lo aplana:
ventas = pd.json_normalize(datos)

# TODO 4: imprime las dimensiones y las primeras filas
print("Dimensiones (filas, columnas):", ventas.shape)
print("\nPrimeras filas:")
print(ventas.head())
print("\nTipos de columna:")
print(ventas.dtypes)