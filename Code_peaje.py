#Nombre: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa:Ingenieria de sistemas
#Codigo Fuente: Autoria propia

#Muestra mensaje de bienvenida
print("Bienvenido al programa de control de pagos del peaje\nTipos de precios:")

#Diccionario con tipos de vehículos y precios
tipos = {"1": ("Vehículo", 3500), "2": ("Camión", 12000), "3": ("Tracto mula", 16000)}
cantidad = {k: 0 for k in tipos}
total = 0
#Muestra los tipos y precios
for k, v in tipos.items():
    print(f"({k}) {v[0]} ${v[1]}")
print("(0) Finalizar")

#Bucle principal: registra los pagos y suma el total
while True:
    t = input("Tipo (1,2,3,0): ").strip()
    if not t.isdigit():
        print("Ingrese solo números (0-3)")
        continue
    if t == '0': break
    if t in tipos:
        cantidad[t] += 1
        total += tipos[t][1]
        print(f"Cobrado: ${tipos[t][1]}")
    else:
        print("Ingrese un tipo valido.")

#Muestra el total recaudado y el tipo más frecuente
print(f"\nTotal recaudado el dia de hoy: ${total}")
for k, v in tipos.items():
    print(f"{v[0]}: {cantidad[k]} - ${cantidad[k]*v[1]}")
if sum(cantidad.values()):
    mayor = max(cantidad, key=cantidad.get)
    print(f"Tipo de Automotor que más transitó por el peaje hoy: {tipos[mayor][0]} ({cantidad[mayor]})")
else:
    print("No se registraron automotores.")


