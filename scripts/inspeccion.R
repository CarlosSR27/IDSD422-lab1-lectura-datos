# inspeccion.R - Tipos, columna derivada e indicadores (R)
# TODO 1: carga data/ventas.csv
ventas <- read.csv("data/ventas.csv")

# TODO 2: imprime la estructura (str) para ver los tipos
# (fija si region llegó como character o factor)
cat("=== Estructura del data.frame ===\n")
str(ventas)

# TODO 3: crea la columna derivada "ticket" = ventas / clientes
ventas$ticket <- ventas$ventas / ventas$clientes
cat("\n=== Tabla con columna 'ticket' ===\n")
print(ventas)

# TODO 4: calcula e imprime los indicadores
cat("\n=== Indicadores de la semana ===\n")

# 1. Venta promedio por sucursal (aggregate)
cat("\n1. Venta promedio por sucursal:\n")
venta_prom_suc <- aggregate(ventas ~ sucursal, data = ventas, FUN = mean)
print(venta_prom_suc)
cat("Venta promedio general:", mean(ventas$ventas), "\n")

# 2. Ticket promedio (ventas totales / clientes totales)
ticket_prom_global <- sum(ventas$ventas) / sum(ventas$clientes)
cat("\n2. Ticket promedio global (ventas totales / clientes totales):", round(ticket_prom_global, 2), "\n")

# 3. Sucursal con mayor y menor venta
suc_max <- ventas[which.max(ventas$ventas), ]
suc_min <- ventas[which.min(ventas$ventas), ]
cat("\n3. Sucursal con MAYOR venta:", suc_max$sucursal, "con", suc_max$ventas, "\n")
cat("   Sucursal con MENOR venta:", suc_min$sucursal, "con", suc_min$ventas, "\n")

# 4. Región con mayor venta total
ventas_region <- aggregate(ventas ~ region, data = ventas, FUN = sum)
reg_max <- ventas_region[which.max(ventas_region$ventas), ]
cat("\n4. Ventas totales por región:\n")
print(ventas_region)
cat("Región con mayor venta total:", reg_max$region, "con", reg_max$ventas, "\n")
