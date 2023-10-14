import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("../winequality-red.csv")

# Crear una instancia del LabelEncoder
label_encoder = LabelEncoder()

# Ajustar y transformar la columna 'etiqueta' para convertir las clases en valores numéricos
data2 = label_encoder.fit_transform(data['quality'])
print(data2)

print("Motivo: convierte etiquetas categoricas de calidad de vino en valores numericos, lo que es necesario para muchos algoritmos de aprendizaje automatico que requieren características numericas.")