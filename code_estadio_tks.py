#Nombre: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa:Ingenieria de sistemas
#Codigo Fuente: Autoria propia

print("bienvenido al programa de compras de boletos del estadio el campin")
print("Sectores disponibles:")
print("A: Norte Alta $15000")
print("B: Norte Baja $13000")
print("C: Oriental Alta $10000")
print("D: Occidental Alta $11000")
print("E: Exclusivo $20000")
#creamos la variable sectores para definir los diferentes precios de las boletas
sectores = {
    "A": 15000,
    "B": 13000,
    "C": 10000,
    "D": 11000,
    "E": 20000
}

    #se le solicita al usuario que ingrese los datos de las boletas
sector = input("Ingrese el sector en el que desea comprar la boleta (A, B, C, D o E): ").upper() #el .upper() convierte la letra a mayuscula
if sector not in sectores:
    print ("Error: El sector ingresado no es valido")
    exit()

cantidad =input("Ingrese la cantidad de boletas que desea comprar: ")

    #se valida que el valor ingresado sea un entero
cantidad = int(cantidad)
if cantidad <= 0:
    print("Error: La cantidad debe ser un número entero positivo.")

    #se crea el calculo que define el precio total de las boletas adquiridas
if sector in sectores:
    precio_unitario = sectores[sector]
    total = precio_unitario * cantidad 

    #se muestra el resumen de la compra
    print("\nResumen de la compra")
    print(f"total a pagar: ${total}")
    print(f"precio unitario de la boleta: {precio_unitario}")
    print(f"cantidad de boletas compradas:{cantidad}")



    






