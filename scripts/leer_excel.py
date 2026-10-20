# leer_excel.py - Cargar el consolidado Excel de finanzas
import pandas as pd

# TODO 1 y 2: importa pandas y carga data/ventas.xlsx indicando la hoja correcta
ventas = pd.read_excel("data/ventas.xlsx", sheet_name="ventas")

# TODO 3: imprime las dimensiones y las primeras filas
print("Dimensiones (filas, columnas):", ventas.shape)
print("\nPrimeras filas:")
print(ventas.head())
print("\nTipos de columna:")
print(ventas.dtypes)