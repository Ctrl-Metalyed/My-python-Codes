#Nombre: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa:Ingenieria de sistemas
#Codigo Fuente: Autoria propia

print ("Programa para calcular el promedio de calificaciones general y de cada uno de los estudiantes, su ranking en orden descendente y el mejor estudiante.")

while True:
    try:    
        num = int(input("Ingrese el número de estudiantes a registrar: "))
        if(num <= 0):
            print("El número de estudiantes debe ser mayor que cero")
        else:
            break
    except ValueError:
            print("Error: Debe ingresar un número entero válido")

estudiantes = []

for i in range(num):
    nombre = input(f"Nombre del estudiante #{i+1}: ")

    while True:
        try:
            nota1 = float(input("Nota 1 (0-100): "))
            if nota1 < 0 or nota1 > 100:
                print("la nota debe ser mayor o igual que 0 y menor o igual que 100")
            else:           
                break
            print("Error: La nota no es valida")
        except ValueError:
            print("Error: Debe ingresar un número válido para la nota.")

    while True:
        try:
            nota2 = float(input("Nota 2 (0-100): "))
            if nota2 < 0 or nota2 > 100:
                print("la nota debe ser mayor o igual que 0 y menor o igual que 100")
            else:           
                break
            print("Error: La nota no es valida")
        except ValueError:
            print("Error: Debe ingresar un número válido para la nota.")
    
    while True:
        try:
            nota3 = float(input("Nota 3 (0-100): "))
            if nota3 < 0 or nota3 > 100:
                print("la nota debe ser mayor o igual que 0 y menor o igual que 100")
            else:           
                break
            print("Error: La nota no es valida")
        except ValueError:
            print("Error: Debe ingresar un número válido para la nota.")
    
    promedio = (nota1 + nota2 + nota3) / 3
    estudiantes.append([nombre, promedio])

# se Ordena la lista de estudiantes por promedio descendente
estudiantes.sort(key=lambda alumno_promedio: alumno_promedio[1], reverse=True)

print("\nPromedio de estudiantes:")
for posicion_estudiante, datos_estudiante in enumerate(estudiantes, 1):
    print(f"{posicion_estudiante}. {datos_estudiante[0]} - Promedio: {datos_estudiante[1]:.2f}")

# Mostrar el mejor estudiante
print(f"\nMejor estudiante: {estudiantes[0][0]} con promedio de: {estudiantes[0][1]:.2f}")

# Promedio general
promedio_general = sum(info_estudiante[1] for info_estudiante in estudiantes) / num
print(f"Promedio general de los estudiantes: {promedio_general:.2f}")