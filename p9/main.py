import random

for _ in range(2):
    data = []

    with open('iris.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        for line in lines[1:]:
            # dividir cada linea en elementos y agregarla a la lista de datos
            row = line.strip().split(',')
            data.append(row)

    # mezclar los datos aleatoriamente
    random.shuffle(data)

    # calcular el índice de división entre entrenamiento y prueba
    total_samples = len(data)
    train_size = int(0.8 * total_samples)

    # inicializar conjuntos de entrenamiento y prueba
    train_data = []
    test_data = []

    # dividir los datos en conjuntos de entrenamiento y prueba
    for i in range(total_samples):
        if i < train_size:
            train_data.append(data[i])
        else:
            test_data.append(data[i])


    print(f"Numero de muestras en conjunto de entrenamiento: {len(train_data)}")
    print(f"Numero de muestras en conjunto de prueba: {len(test_data)}")

    print("\nDatos de entrenamiento:")
    for row in train_data:
        print(row)

    print("\nDatos de prueba:")
    for row in test_data:
        print(row)
print("Motivo: Hacer al menos dos ciclos para dividir un conjunto de datos en train (80%) y test (20%), en el conjunto de datos Iris, es util para:")
print("1. Evaluar el modelo de manera más robusta utilizando técnicas como la validacion cruzada.")
print("2. Determinar la estabilidad del modelo al evaluar su rendimiento en diferentes divisiones de los datos de prueba.")
print("En resumen, ayuda a obtener evaluaciones más confiables y a comprender mejor el comportamiento del modelo en diferentes escenarios.")