import pandas as pd
from sklearn.preprocessing import OneHotEncoder

data = pd.read_csv("../winequality-red.csv")

hot_encoder = OneHotEncoder()

hot_encoder.fit(data)
data2 = hot_encoder.transform(data)
print(data2.toarray())

print("Motivo: transforma estas categorias en un conjunto de columnas binarias (variables ficticias), donde cada columna representa una categoria unica.")