
install.packages("jsonlite")
library(jsonlite)
ventas <- fromJSON("data/ventas.json")
View(ventas)
head(ventas)
dim(ventas)
str(ventas)