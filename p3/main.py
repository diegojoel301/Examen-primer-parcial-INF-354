import pandas as pd
import numpy as np

dataset = pd.read_csv("dataset.csv")

for columna in dataset.columns:
    # verificar si la columna tiene valores faltantes
    if dataset[columna].isnull().any():
        # estrategia de imputación utilizando la mediana
        mediana_columna = dataset[columna].median()
        dataset[columna].fillna(mediana_columna, inplace=True)

print("Imputacion con estrategia de la media")
print(dataset)

dataset = pd.read_csv("dataset.csv")
# iterar a traves de todas las columnas nuevamente para aplicar la estrategia de moda
for columna in dataset.columns:
    # verificar si la columna tiene valores faltantes
    if dataset[columna].isnull().any():
        # estrategia de imputación utilizando la moda
        moda_columna = dataset[columna].mode().iloc[0]
        dataset[columna].fillna(moda_columna, inplace=True)

print("Imputacion con estrategia de la moda")
print(dataset)

print("La imputacion nos permite eliminar los valores faltantes, lo que suele ser comun en conjuntos de datos en el mundo real")
print("Proposito de uso de la estrategia de la media: Se la usa para preservar la tendencia central y evitar la perdida de informacion importante debido a los valroes faltantes, se usa cuando se busca una coherencia estadisticas y no cambiar un vacio por un dato que genere sesgos significativos")
print("Proposito de uso de la estretegia de la moda: Es util cuando se trata de datos categoricos o discretos y se busca conservar la frecuencia relativa de las categorias en la columna, util cuando se desea preservar la estructura de categorias de los datos")