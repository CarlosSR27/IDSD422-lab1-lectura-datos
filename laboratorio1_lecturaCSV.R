# Cargar la librería necesaria
library(readr)

# Leer los datos de ventas
ventas <- read_csv("data/ventas.csv")

# Explorar los primeros registros
head(ventas)

# Ver las dimensiones de la tabla (filas y columnas)
dim(ventas)

# Ver la estructura interna de los datos
str(ventas)