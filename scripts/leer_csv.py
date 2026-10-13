# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
import pandas as pd
# Cargo el csv en un data frame
datos = r"C:\Users\Administrador\Documents\EPN\Cuarto Semestre\E.P. Ciencia de Datos I\Programas\IDSD422-lab1-lectura-datos\data\ventas.csv"
ventas = pd.read_csv(datos)


# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
# Imprimir las dimenciones
ventas.shape


# TODO 3: imprime las primeras filas para revisar las columnas
# Imprimir las primeras filas
ventas.head()


# TODO 4: imprimir los tipos de columna
print('\n Tipos de columna' )
print(ventas.dtypes)
