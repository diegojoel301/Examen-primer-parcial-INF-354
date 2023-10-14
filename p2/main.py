import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# funcion para calcular la media
def calcular_media(valores):
    return np.mean(valores)

# funcion para calcular la moda
def calcular_moda(vector):
    moda = pd.Series(vector).mode()
    return moda[0] if not moda.empty else None

# funcion para calcular percentiles
def calcular_percentiles(columna, percentiles):
    return np.percentile(columna, percentiles)

# funcion para calcular cuartiles
def calcular_cuartiles(datos):
    Q1 = np.percentile(datos, 25)
    mediana = np.percentile(datos, 50)
    Q3 = np.percentile(datos, 75)
    return Q1, mediana, Q3

dataset = pd.read_csv('../winequality-red.csv')

descripcion_por_columna = {
    "fixed acidity": "La mayoría de los ácidos involucrados con el vino o fijos o no volátiles (no se evaporan fácilmente)",
    "volatile acidity": "La cantidad de ácido acético en el vino, que en niveles demasiado altos puede provocar un sabor desagradable a vinagre",
    "citric acid": "El ácido cítrico, que se encuentra en pequeñas cantidades, puede añadir 'frescura' y sabor a los vinos.",
    "residual sugar": "La cantidad de azúcar que queda después de que se detiene la fermentación, es raro encontrar vinos con menos de 1 gramo/litro y los vinos con más de 45 gramos/litro se consideran dulces",
    "chlorides": "La cantidad de sal en el vino",
    "free sulfur dioxide": "La forma libre de SO2 existe en equilibrio entre el SO2 molecular (como gas disuelto) y el ion bisulfito; Previene el crecimiento microbiano y la oxidación del vino.",
    "total sulfur dioxide": "Cantidad de formas libres y ligadas de S02; En concentraciones bajas, el SO2 es prácticamente indetectable en el vino, pero en concentraciones de SO2 libre superiores a 50 ppm, el SO2 se vuelve evidente en la nariz y el sabor del vino.",
    "density": "La densidad del agua es cercana a la del agua dependiendo del porcentaje de alcohol y contenido de azúcar.",
    "pH": "Describe qué tan ácido o básico es un vino en una escala de 0 (muy ácido) a 14 (muy básico); la mayoría de los vinos tienen entre 3 y 4 en la escala de pH",
    "sulphates": "Un aditivo del vino que puede contribuir a los niveles de dióxido de azufre (S02), que actúa como antimicrobiano y antioxidante.",
    "alcohol": "El porcentaje de alcohol del vino",
    "quality": "Variable de salida (basada en datos sensoriales, puntuación entre 0 y 10)"
}

for variable_categoria in dataset.columns:
    print("[+] Para", variable_categoria)
    valores = dataset[variable_categoria]

    media_value = calcular_media(valores)
    moda_value = calcular_moda(valores)
    Q1, mediana, Q3 = calcular_cuartiles(valores)
    percentiles_a_calcular = [25, 50, 75]
    resultados_percentiles = calcular_percentiles(valores, percentiles_a_calcular)

    print("La media es", media_value)
    print("La moda es", moda_value)
    print("Q1:", Q1)
    print("Mediana (Q2):", mediana)
    print("Q3:", Q3)

    for p, valor in zip(percentiles_a_calcular, resultados_percentiles):
        print(f'Percentil {p}: {valor}')

    # Crear un gráfico para la columna seleccionada
    plt.hist(valores, alpha=0.5)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title(f'Gráfico para {variable_categoria}')
    
    # Agregar una descripción debajo del título
    descripcion = descripcion_por_columna.get(variable_categoria, "Descripción no disponible")
    plt.figtext(0.5, 0.85, descripcion, fontsize=10, ha='center')

    # Mostrar el gráfico
    plt.show()

    print("=============================================================")
print("Extra: El calculo de la media nos ayudara a saber la tendencia de los datos, la mediana es basicamente nos ayuda a saber la medida de tendencia central que divide los datos en dos mitades iguales, la moda por cada columna nos ayudara a saber sobre los valores mas comunes en cada columna, ayuda a identificar patrones recurrentes y puede ser relevante en situaciones donde se desea conocer cuales son los valores mas populares en la columna")
print("Q1: divide el 25% infenrior de los datos es similar a la mediana")
print("Q2: Es en si la mediana")
print("Q3: divide el 75% infenrior de los datos es similar a la mediana ")
print("Los cuartiles nos ayudan a identificar valores atipicos o extremos")