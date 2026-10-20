# inspeccion.py - Tipos, columna derivada e indicadores
import pandas as pd

# TODO 1: carga data/ventas.csv
ventas = pd.read_csv("data/ventas.csv")

# TODO 2: imprime los tipos (dtypes) de cada columna
print("=== Tipos de datos (dtypes) ===")
print(ventas.dtypes)

# TODO 3: crea la columna derivada "ticket" = ventas / clientes
ventas["ticket"] = ventas["ventas"] / ventas["clientes"]
print("\n=== Tabla con columna derivada 'ticket' ===")
print(ventas)

# TODO 4: calcula e imprime los indicadores
print("\n=== Indicadores de la semana ===")

# 1. Venta promedio por sucursal
venta_promedio_sucursal = ventas.groupby("sucursal")["ventas"].mean()
print("\n1. Venta promedio por sucursal:")
print(venta_promedio_sucursal)
print(f"Venta promedio general por sucursal: {ventas['ventas'].mean():.2f}")

# 2. Ticket promedio (ventas totales / clientes totales)
ticket_promedio_global = ventas["ventas"].sum() / ventas["clientes"].sum()
print(f"\n2. Ticket promedio (ventas totales / clientes totales): {ticket_promedio_global:.2f}")

# 3. Sucursal con mayor y menor venta
idx_max = ventas["ventas"].idxmax()
idx_min = ventas["ventas"].idxmin()
print(f"\n3. Sucursal con MAYOR venta: {ventas.loc[idx_max, 'sucursal']} ({ventas.loc[idx_max, 'ventas']})")
print(f"   Sucursal con MENOR venta: {ventas.loc[idx_min, 'sucursal']} ({ventas.loc[idx_min, 'ventas']})")

# 4. Región con mayor venta total
ventas_por_region = ventas.groupby("region")["ventas"].sum()
region_mayor = ventas_por_region.idxmax()
print("\n4. Ventas totales por región:")
print(ventas_por_region)
print(f"Región con mayor venta total: {region_mayor} ({ventas_por_region.max()})")