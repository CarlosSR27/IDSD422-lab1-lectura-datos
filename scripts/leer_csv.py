# leer_csv.py - Cargar el reporte CSV del ERP
import pandas as pd

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
ventas = pd.read_csv("data/ventas.csv")

# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
print("Dimensiones (filas, columnas):", ventas.shape)

# TODO 3: imprime las primeras filas para revisar las columnas
print("\nPrimeras filas:")
print(ventas.head())

# TODO 4: imprimir los tipos de columna
print("\nTipos de columna:")
print(ventas.dtypes)