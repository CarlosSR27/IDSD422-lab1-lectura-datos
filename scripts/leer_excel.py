# leer_excel.py — Cargar el consolidado Excel de finanzas (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_excel.py

# TODO 1: importa pandas
# TODO 2: carga data/ventas.xlsx indicando la hoja correcta
# TODO 3: imprime las dimensiones y las primeras filas

import pandas as pd
#El m
datos = r'C:\Users\Administrador\Documents\EPN\Cuarto Semestre\E.P. Ciencia de Datos I\Programas\IDSD422-lab1-lectura-datos\data\ventas.xlsx'
ventas = pd.read_excel(datos, sheet_name="ventas",engine="calamine")
print(ventas.head())
print(ventas.shape)
print(ventas.dtypes)