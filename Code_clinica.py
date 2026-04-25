#Nombre: Juan Diego Bohorquez Tique
#Grupo: 213022_662
#Programa:Ingenieria de sistemas
#Codigo Fuente: Autoria propia

#Muestra mensaje de bienvenida y lista de procedimientos
print("Bienvenido al programa para conocer el valor de un procedimiento en la clinica\nTipos de procedimientos:")
print("Radiografía: 30000\nEcografía: 35000\nLaboratorio: 25000\nConsulta Externa: 40000\nConsulta Especializada: 80000\n")

#Valida que el código tenga 5 dígitos
def validar(codigo):
    codigo = str(codigo)
    if len(codigo) != 5:
        return 0
    if not codigo.isdigit():
        return 0
    if codigo[0] not in "12":
        return 0
    if codigo[1] not in "12345":
        return 0
    return 1

#Determina el tipo de paciente según el primer dígito
def tipo(codigo):
    return ["AFILIADO", "PARTICULAR"][int(str(codigo)[0]) - 1]

#Determina el procedimiento según el segundo dígito
def servicio(codigo):
    procedimientos = ["RADIOGRAFÍA", "ECOGRAFÍA", "LABORATORIO", "CONSULTA EXTERNA", "CONSULTA ESPECIALIZADA"]
    return procedimientos[int(str(codigo)[1]) - 1] if 1 <= int(str(codigo)[1]) <= 5 else "DESCONOCIDO"

#Devuelve el costo del procedimiento
def costo(procedimiento_nombre):
    nombres = ["RADIOGRAFÍA", "ECOGRAFÍA", "LABORATORIO", "CONSULTA EXTERNA", "CONSULTA ESPECIALIZADA"]
    valores = [30000, 35000, 25000, 40000, 80000]
    for i, nombre in enumerate(nombres):
        if procedimiento_nombre == nombre:
            return valores[i]
    return 0

#Calcula descuento o recargo según el tipo de paciente y suma de dígitos
def descuReca(codigo, tipo_paciente, costo_normal):
    suma = sum(int(d) for d in str(codigo)[2:])
    porcentaje = 0.15 if suma % 2 == 0 else 0.25
    return -costo_normal * porcentaje if tipo_paciente == "AFILIADO" else costo_normal * porcentaje

#Calcula el total a pagar
def pago(costo_normal, descuento_recarga):
    return costo_normal + descuento_recarga

#Función principal: Pide el código, calcula y muestra el resultado
def principal():
    codigo = input("Ingrese el código del paciente(5 digitos): ").strip()
    if validar(codigo) == 0:
        print("Código inválido. Debe tener 5 dígitos, ser numérico, iniciar con 1 o 2 y el segundo dígito entre 1 y 5.")
        return
    tipo_paciente = tipo(codigo)
    procedimiento_nombre = servicio(codigo)
    costo_normal = costo(procedimiento_nombre)
    descuento_recarga = descuReca(codigo, tipo_paciente, costo_normal)
    total = pago(costo_normal, descuento_recarga)
    print(f"Tipo de paciente: {tipo_paciente}")
    print(f"Procedimiento: {procedimiento_nombre}")
    print(f"Costo base: ${costo_normal}")
    print(f"Descuento/Recargo: ${descuento_recarga}")
    print(f"Total a pagar: ${total}")

principal()

