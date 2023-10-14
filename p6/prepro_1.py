import pandas as pd

# Cargar el conjunto de datos desde un archivo CSV
df = pd.read_csv('../winequality-red.csv')

print("Eliminacion de duplicados")
print("Nos ayudará a evitar la redundancia en cada columna para cada variable categórica y mejorando la calidad de los datos.")

# Mostrar el número de filas antes de eliminar duplicados
print(f'Número de filas antes de eliminar duplicados: {len(df)}')

# Eliminar duplicados
df = df.drop_duplicates()

# Mostrar el número de filas después de eliminar duplicados
print(f'Número de filas después de eliminar duplicados: {len(df)}')

# Ahora puedes continuar con el preprocesamiento en scikit-learn si es necesario
