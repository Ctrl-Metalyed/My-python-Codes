#Nombre del estudiante: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa: Ingenieria de sistemas
#Codigo Fuente: Autoria propia

while True:
    try:
        print("Hola, este programa obtiene los divisores de un numero entre 10 y 90")
        numero= int (input("Digite un numero entre 10 y 90: "))
        if(numero<10 or numero>90):
            print("Error: El numero debe estar entre 10 y 90")
        else:
            break
    except ValueError:
            print("Error: Debe ingresar un número válido")

#obtener y mostrar los divisores
divisores = []
for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        divisores.append(divisor)

print("Los divisores de", numero, "son:", divisores)
print("Cantidad de divisores:", len(divisores))