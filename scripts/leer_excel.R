# leer_excel.R - Cargar el consolidado Excel de finanzas (R)
library(readxl)

# TODO 1: carga data/ventas.xlsx con readxl::read_excel indicando la hoja
ventas <- read_excel("data/ventas.xlsx", sheet = "ventas")

# TODO 2: imprime las dimensiones (dim) y las primeras filas (head)
cat("Dimensiones (filas, columnas):", dim(ventas), "\n\n")
print(head(ventas))
str(ventas)
