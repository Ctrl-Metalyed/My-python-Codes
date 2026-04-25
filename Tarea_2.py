#Ejercicio 3: Sistema de Nómina Empresarial
#Juan Diego Bohorquez Tique 

#Se crea la clase base empleado que representa los atributos comunes de los empleados en general.
class Empleado:
    def __init__(self, nombre, identificacion, salario_base):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario_base = salario_base

    def calcular_salario(self):
        raise NotImplementedError

    def mostrar_informacion(self, detalle=False, incluir_bonos=False):
        info = f"Nombre: {self.nombre}\nID: {self.identificacion}\n"
        if detalle:
            info += f"Salario: {self.calcular_salario()}\n"
        return info
    
#Se crean las subclases para cada tipo de empleado y su metodo para calcular el salario según sus características. 

#Para el empleado a tiempo completo se coloca salario base y bonificacion en caso de ser necesario.
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, identificacion, salario_base, bonificacion=0):
        super().__init__(nombre, identificacion, salario_base)
        self.bonificacion = bonificacion

    def calcular_salario(self):
        return self.salario_base + self.bonificacion

#Para el empleado por horas se coloca el numero de horas trabajadas y el pago por hora para calcular su salario.
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, identificacion, horas_trabajadas, pago_por_hora):
        super().__init__(nombre, identificacion, 0)
        self.horas_trabajadas = horas_trabajadas
        self.pago_por_hora = pago_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.pago_por_hora

#Para el empleado por comision se coloca el salario base, las ventas realizadas y el porcentaje de comision para calcular su salario.
class EmpleadoComision(Empleado):
    def __init__(self, nombre, identificacion, salario_base, ventas=0, porcentaje=0.1):
        super().__init__(nombre, identificacion, salario_base)
        self.ventas = ventas
        self.porcentaje = porcentaje

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje)


class Bonificable:
    def __init__(self):
        self.bonificaciones = []

    def agregar_bonificacion(self, boni):
        self.bonificaciones.append(boni)

    def obtener_bonificaciones(self):
        return sum(self.bonificaciones)

#El empleado a tiempo completo bonificado hereda de EmpleadoTiempoCompleto y Bonificable, lo que le permite tener un salario base y además agregar bonificaciones adicionales.
class EmpleadoTiempoCompletoBonificado(EmpleadoTiempoCompleto, Bonificable):
    def __init__(self, nombre, identificacion, salario_base):
        EmpleadoTiempoCompleto.__init__(self, nombre, identificacion, salario_base)
        Bonificable.__init__(self)

    def calcular_salario(self):
        return self.salario_base + self.obtener_bonificaciones()

#Se crea la clase SistemaNomina para gestionar los empleados y calcular la nómina total de la empresa.
class SistemaNomina:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        for emp in self.empleados:
            if emp.identificacion == empleado.identificacion:
                return False
        self.empleados.append(empleado)
        return True
    
# Calcula la nómina total de la empresa
    def calcular_nomina(self):
        total = 0
        resultados = ""

        for emp in self.empleados:
            salario = emp.calcular_salario()
            resultados += f"{emp.nombre}: {salario:,.0f}\n"
            total += salario

        resultados += f"\nTotal payroll: {total:,.0f}"
        return resultados


#Se implementa la interfaz gráfica utilizando Tkinter
import tkinter as tk
from tkinter import ttk, messagebox

sistema = SistemaNomina()

#Cambiamos de forma dinamica el texto del campo de entrada segun el tipo de empleado ingresado.
def cambiar_campos(event):
    tipo = combo_tipo.get()

    if tipo == "Full-Time":
        label1.config(text="Base Salary")   
        label2.config(text="Bonus")

    elif tipo == "Part-Time":
        label1.config(text="Hours Worked")
        label2.config(text="Hourly Rate")

    elif tipo == "Commission":
        label1.config(text="Base Salary")
        label2.config(text="Sales")

    elif tipo == "Bonused":
        label1.config(text="Base Salary")
        label2.config(text="Bonus")


def agregar_empleado():
    tipo = combo_tipo.get()
    nombre = entry_nombre.get()
    id_ = entry_id.get()

    if not nombre or not id_ or not tipo:
        messagebox.showerror("Error", "Complete all fields")
        return

    try:
        v1 = float(entry1.get())
    except:
        messagebox.showerror("Error", "Invalid numeric data")
        return

    if tipo == "Full-Time":
        try:
            v2 = float(entry2.get())
        except:
            messagebox.showerror("Error", "Invalid numeric data")
            return
        emp = EmpleadoTiempoCompleto(nombre, id_, v1, v2)

    elif tipo == "Part-Time":
        try:
            v2 = float(entry2.get())
        except:
            messagebox.showerror("Error", "Invalid numeric data")
            return
        emp = EmpleadoPorHoras(nombre, id_, v1, v2)

    elif tipo == "Commission":
        try:
            v2 = float(entry2.get())
        except:
            messagebox.showerror("Error", "Invalid numeric data")
            return
        emp = EmpleadoComision(nombre, id_, v1, v2)

    elif tipo == "Bonused":
        emp = EmpleadoTiempoCompletoBonificado(nombre, id_, v1)

        # Permite múltiples bonificaciones separadas por coma
        bonos = entry2.get().split(",")

        try:
            for b in bonos:
                b = b.strip()
                if b:
                    emp.agregar_bonificacion(float(b))
        except:
            messagebox.showerror("Error", "Invalid bonus format")
            return

    if not sistema.agregar_empleado(emp):
        messagebox.showerror("Error", "Employee ID already exists")
        return

    lista_empleados.insert(tk.END, f"{nombre} - {tipo}")
    messagebox.showinfo("Success", "Employee added")


#Limpia los campos después de agregar un empleado
    entry_nombre.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)


def eliminar_empleado():
    seleccion = lista_empleados.curselection()

    if not seleccion:
        messagebox.showwarning("Warning", "Select an employee")
        return

    index = seleccion[0]
    sistema.empleados.pop(index)
    lista_empleados.delete(index)

    messagebox.showinfo("Success", "Employee removed")


def calcular_nomina():
    resultado = sistema.calcular_nomina()
    text_resultado.delete("1.0", tk.END)
    text_resultado.insert(tk.END, resultado)


#Ventana principal
root = tk.Tk()
root.title("Payroll System")


tk.Label(root, text="Employee Name").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="Employee ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()


#ComboBox que permite seleccionar el tipo de empleado desde una lista desplegable
tk.Label(root, text="Employee Type").pack()
combo_tipo = ttk.Combobox(root, values=[
    "Full-Time",
    "Part-Time",
    "Commission",
    "Bonused"
])
combo_tipo.pack()
combo_tipo.config(state="readonly")

#Cambia dinámicamente los campos según el tipo  de empleado seleccionado
combo_tipo.bind("<<ComboboxSelected>>", cambiar_campos)


label1 = tk.Label(root, text="")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

#Integracion de los botones para agregar, eliminar empleados y calcular la nómina total de la empresa.
tk.Button(root, text="Add Employee", command=agregar_empleado).pack()

#Lista en tkinter donde se almacenan los empleados agregados al sistema.
tk.Label(root, text="Employees List").pack()
lista_empleados = tk.Listbox(root)
lista_empleados.pack()

tk.Button(root, text="Delete Employee", command=eliminar_empleado).pack()

#Boton de calcular la nómina total usando el sistema
tk.Button(root, text="Recalculate payroll", command=calcular_nomina).pack()

#Muestra el resultados del cálculo de la nómina
text_resultado = tk.Text(root, height=10)
text_resultado.pack()

root.mainloop()