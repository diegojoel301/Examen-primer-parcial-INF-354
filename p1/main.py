import matplotlib.pyplot as plt
def media(valores):
    return sum(valores) / len(valores)

def calcular_moda(vector):
    # Diccionario para guardar la frecuencia de cada elemento
    frecuencia = {}
    
    # inicializamos la moda y el maximo de frecuencia
    moda = None
    max_frecuencia = 0
    
    for elemento in vector:
        # incrementa la frecuencia del elemento en el diccionario
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
        
        # actualiza la moda si se encuentra un nuevo máximo
        if frecuencia[elemento] > max_frecuencia:
            moda = elemento
            max_frecuencia = frecuencia[elemento]
    
    return moda

def calcular_percentiles(columna, percentiles):
    # Ordenamos la columna
    columna_ordenada = sorted(columna)
    
    # Calcula los valores de los percentiles especificados
    resultados = {}
    for p in percentiles:
        if 0 <= p <= 100:
            indice = (len(columna_ordenada) - 1) * p / 100
            if indice.is_integer():
                resultados[f'P{p}'] = columna_ordenada[int(indice)]
            else:
                parte_entera = int(indice)
                parte_decimal = indice - parte_entera
                valor_percentil = (1 - parte_decimal) * columna_ordenada[parte_entera] + parte_decimal * columna_ordenada[parte_entera + 1]
                resultados[f'P{p}'] = valor_percentil
    
    return resultados

def calcular_cuartiles(datos):
    # Ordena la lista de datos
    datos_ordenados = sorted(datos)
    
    # calcula la mediana segundo cuartil = Q2
    if len(datos_ordenados) % 2 == 0:
        mediana = (datos_ordenados[len(datos_ordenados) // 2 - 1] + datos_ordenados[len(datos_ordenados) // 2]) / 2
    else:
        mediana = datos_ordenados[len(datos_ordenados) // 2]
    
    # divide los datos en dos partes (inferior y superior) para calcular Q1 y Q3
    mitad = len(datos_ordenados) // 2
    inferior = datos_ordenados[:mitad]
    superior = datos_ordenados[mitad:]
    
    # calcula Q1 y Q3
    if len(inferior) % 2 == 0:
        Q1 = (inferior[len(inferior) // 2 - 1] + inferior[len(inferior) // 2]) / 2
    else:
        Q1 = inferior[len(inferior) // 2]
    
    if len(superior) % 2 == 0:
        Q3 = (superior[len(superior) // 2 - 1] + superior[len(superior) // 2]) / 2
    else:
        Q3 = superior[len(superior) // 2]
    
    return Q1, mediana, Q3

with open('../winequality-red.csv', 'r') as archivo_csv:
    encabezados = archivo_csv.readline().strip().split(',')

    # Inicializa un diccionario vacío para almacenar las columnas
    dataset = {columna: [] for columna in encabezados} # en vacio todas las columns

    # lee el resto del archivo línea por línea
    for linea in archivo_csv:
        valores = linea.strip().split(',')
        for columna, valor in zip(encabezados, valores):
            dataset[columna].append(float(valor))


descripcion_por_columna = dict()

descripcion_por_columna["fixed acidity"] = "La mayoría de los ácidos involucrados con el vino o fijos o no volátiles (no se evaporan fácilmente)"
descripcion_por_columna["volatile acidity"] = "La cantidad de ácido acético en el vino, que en niveles demasiado altos puede provocar un sabor desagradable a vinagre"
descripcion_por_columna["citric acid"] = "El ácido cítrico, que se encuentra en pequeñas cantidades, puede añadir 'frescura' y sabor a los vinos."
descripcion_por_columna["residual sugar"] = "La cantidad de azúcar que queda después de que se detiene la fermentación, es raro encontrar vinos con menos de 1 gramo/litro y los vinos con más de 45 gramos/litro se consideran dulces"
descripcion_por_columna["chlorides"] = "La cantidad de sal en el vino"
descripcion_por_columna["free sulfur dioxide"] = "La forma libre de SO2 existe en equilibrio entre el SO2 molecular (como gas disuelto) y el ion bisulfito; Previene el crecimiento microbiano y la oxidación del vino."
descripcion_por_columna["total sulfur dioxide"] = "Cantidad de formas libres y ligadas de S02; En concentraciones bajas, el SO2 es prácticamente indetectable en el vino, pero en concentraciones de SO2 libre superiores a 50 ppm, el SO2 se vuelve evidente en la nariz y el sabor del vino."
descripcion_por_columna["density"] = "La densidad del agua es cercana a la del agua dependiendo del porcentaje de alcohol y contenido de azúcar."
descripcion_por_columna["pH"] = "Describe qué tan ácido o básico es un vino en una escala de 0 (muy ácido) a 14 (muy básico); la mayoría de los vinos tienen entre 3 y 4 en la escala de pH"
descripcion_por_columna["sulphates"] = "Un aditivo del vino que puede contribuir a los niveles de dióxido de azufre (S02), que actúa como antimicrobiano y antioxidante."
descripcion_por_columna["alcohol"] = "El porcentaje de alcohol del vino"
descripcion_por_columna["quality"] = "Variable de salida (basada en datos sensoriales, puntuación entre 0 y 10)"

for variable_categoria in dataset.keys():
    print("[+] Para %s" % variable_categoria)
    media_value = str(media(dataset[variable_categoria]))
    moda_value = str(calcular_moda(dataset[variable_categoria]))

    print("La media es %s" % (media(dataset[variable_categoria])))
    print("La moda  es %s" % (calcular_moda(dataset[variable_categoria])))
    Q1, mediana, Q3 = calcular_cuartiles(dataset[variable_categoria])
    print("Q1:", Q1)
    print("Mediana (Q2):", mediana)
    print("Q3:", Q3)

    percentiles_a_calcular = [25, 50, 75]

    resultados_percentiles = calcular_percentiles(dataset[variable_categoria], percentiles_a_calcular)

    for p, valor in resultados_percentiles.items():
        print(f'Percentil {p}: {valor}')

    valores = dataset[variable_categoria]

    # Crea un gráfico para la clase seleccionada
    plt.hist(valores, alpha=0.5)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title(f'Gráfico para {variable_categoria}')
    # Agregar una descripción adicional
    
    # Agregar una descripción debajo del título
    descripcion = descripcion_por_columna[variable_categoria]
    plt.figtext(0.5, 0.85, descripcion, fontsize=10, ha='center')


    # Mostrar el gráfico
    

    plt.show()

    print("=============================================================")
print("Extra: El calculo de la media nos ayudara a saber la tendencia de los datos, la mediana es basicamente nos ayuda a saber la medida de tendencia central que divide los datos en dos mitades iguales, la moda por cada columna nos ayudara a saber sobre los valores mas comunes en cada columna, ayuda a identificar patrones recurrentes y puede ser relevante en situaciones donde se desea conocer cuales son los valores mas populares en la columna")
print("Q1: divide el 25% infenrior de los datos es similar a la mediana")
print("Q2: Es en si la mediana")
print("Q3: divide el 75% infenrior de los datos es similar a la mediana ")
print("Los cuartiles nos ayudan a identificar valores atipicos o extremos")