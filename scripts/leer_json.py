# leer_json.py — Cargar el reporte JSON de la API (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_json.py

# TODO 1: importa json y pandas
import json
import pandas as pd


# TODO 2: carga data/ventas.json con json.load
datos = r"C:\Users\Administrador\Documents\EPN\Cuarto Semestre\E.P. Ciencia de Datos I\Programas\IDSD422-lab1-lectura-datos\data\ventas.json"

with open(datos,encoding='utf-8') as f:
  datos = json.load(f)

ventas = pd.json_normalize(datos)
print(ventas)


# TODO 3: convierte la lista de diccionarios en un DataFrame
# (recuerda del cap. 2: el JSON no llega como tabla directa)
  # Imprime las primeras filas
print(ventas.head())


# TODO 4: imprime las dimensiones y las primeras filas
  # Imprimir las primeras filas
print(ventas.head())

  # Las dimenciones de la tabla
print('\nDimenciones',ventas.shape)
