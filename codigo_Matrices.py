#Nombre del estudiante: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa: Ingenieria de sistemas
#Codigo Fuente: Autoria propia

print ("Programa para calcular la suma total de los elementos de una matriz y el perimetro de los bordes.")
#creamos la matriz
Columna = []
for i in range(5):
    fila = []
    for j in range(5):
        while True:
            entrada = input(f"Ingresa los valores de la matriz seguidos de un enter para cada uno, [{i}][{j}] (solo numeros enteros entre 10 y 90 ): ")
            try:
                valor = int(entrada)
            except ValueError:
                print("Error: Por favor ingresa un número entero válido entre 10 y 90.")
                continue
            if 10 <= valor <= 90:
                fila.append(valor)
                break
            else:
                print("Error: El número debe estar entre 10 y 90. Inténtalo de nuevo.")
    Columna.append(fila)           
          

#mostramos la  matriz
print("La matriz ingresada es:")
for fila in Columna:
    print(fila)

#calculamos la suma total y el promedio
suma = 0
for i in range(5):
    for j in range(5):
        suma += Columna[i][j]
perimetro = 0
for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            perimetro += Columna[i][j]
print(f"La suma total de los elementos de la matriz es: {suma}")
print(f"El perimetro de los bordes de la matriz es: {perimetro}")
