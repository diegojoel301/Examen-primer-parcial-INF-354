from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df = pd.read_csv('../winequality-red.csv')
print("La normalización de los datos en su conjunto de calidad de vinos puede ayudar a mejorar la interpretación de los modelos, la comparabilidad de características y la eficacia de los algoritmos, lo que potencialmente puede mejorar su capacidad para determinar la calidad de los vinos de manera más precisa")

scaler = MinMaxScaler()
# Los valores estaran entre 0 y 1
df_normalized = scaler.fit_transform(df)

df_normalized = pd.DataFrame(df_normalized, columns=df.columns)

print(df_normalized)
