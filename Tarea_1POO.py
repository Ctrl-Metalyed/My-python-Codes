import tkinter as tk
from tkinter import messagebox

#Creamos la clase Usuario con los parameteros de usuario y contraseña siendo ambos "programacion"
class Usuario:
    def __init__(self):
        self._usuario = "programacion"
        self._password = "programacion"

    def validar(self, usuario_ingresado, password_ingresada):
        return usuario_ingresado == self._usuario and password_ingresada == self._password


#Login del sistema
def logearse():
    usuario_ingresado = entrada_user.get()
    password_ingresada = entrada_password.get()

    if user.validar(usuario_ingresado, password_ingresada):
        messagebox.showinfo("Login successful", "Welcome to the bike shop")
        ventana_login.destroy()
        abrir_apptaller()
    else:
        messagebox.showerror("Login failed", "Invalid username or password")


#Creamos la clase BicicletaTaller con los atributos de serial,hora de ingreso y costo por hora
class BicicletaTaller:
    def __init__(self, serial, hora_ingreso, costo_por_hora):
        self.__serial = serial
        self.__hora_ingreso = hora_ingreso
        self.__costo_por_hora = costo_por_hora

    def registrar_ingreso(self, hora):
        self.__hora_ingreso = hora

    def obtener_serial(self):
        return self.__serial
    
    def calcular_total(self, hora_salida):
        horas_en_taller = int(hora_salida - self.__hora_ingreso)
        return horas_en_taller * self.__costo_por_hora
    
    def obtener_hora_ingreso(self):
        return self.__hora_ingreso


#creamos la lista de bicicletas para almacenar la info de cada una
bicicletas = []


#Funciones para el sistema de la clase BicicletaTaller
def registrar_ingreso_bici():
    try:
        serial = entrada_serial.get()
        hora = float(entrada_hora.get())

        if not (0 <= hora <= 23.59):
            messagebox.showerror("Error", "Invalid time")
            return
        
        bici = BicicletaTaller(serial, hora, costo_por_hora=150)
        bicicletas.append(bici)
        
        messagebox.showinfo("Registration", "Registered bike")
        actualizar_lista()

    except:
        messagebox.showerror("Error", "Enter valid data for time (0.00-23.59)")


def actualizar_lista():
    lista_bicis.delete(0, tk.END)

    for i, bici in enumerate(bicicletas):
        lista_bicis.insert(tk.END, f"{i+1}. Serial: {bici.obtener_serial()}")


def pagar_bici():
    try:
        seleccion = lista_bicis.curselection()[0]
        bici = bicicletas[seleccion]

        hora_salida = float(entrada_salida.get())

        if hora_salida < 0 or hora_salida > 23.59:
            messagebox.showerror("Error", "Invalid departure time")
            return
        
        if hora_salida < bici.obtener_hora_ingreso():#validamos que la hora de salida no sea menor a la hora de ingreso
            messagebox.showerror("Error", "The departure time cannot be earlier than the arrival time")
            return

        total = bici.calcular_total(hora_salida)

        messagebox.showinfo("Pay", f" Total to pay: ${total}")
        bicicletas.pop(seleccion)
        actualizar_lista()

    except:
        messagebox.showerror("Error", "Select a bike and make sure you enter a valid departure time (0.00-23.59)")


#Creamos la interfaz del taller de bicicletas
def abrir_apptaller():

    global entrada_serial, entrada_hora, entrada_salida, lista_bicis

    ventana_taller = tk.Tk()   # ← ahora es la ventana principal del taller
    ventana_taller.title("Taller de Bicicletas")
    ventana_taller.geometry("500x400+500+250")
    ventana_taller.configure(bg="gainsboro")
    ventana_taller.resizable(True, True)

    tk.Label(ventana_taller, text="Register Entry", font=("Times New Roman", 12), bg="gainsboro").pack()
    
    tk.Label(ventana_taller, text="Serial:", font=("Times New Roman", 10), bg="gainsboro").pack()
    entrada_serial = tk.Entry(ventana_taller)
    entrada_serial.pack()

    tk.Label(ventana_taller, text="Entry Time(0.00-23.59):", font=("Times New Roman", 10), bg="gainsboro").pack()
    entrada_hora = tk.Entry(ventana_taller)
    entrada_hora.pack()

    tk.Button(ventana_taller, text="Register Entry", command=registrar_ingreso_bici).pack()

    tk.Label(ventana_taller, text="Bicycles in Workshop:", font=("Times New Roman", 12), bg="gainsboro").pack()
    
    lista_bicis = tk.Listbox(ventana_taller)
    lista_bicis.pack()

    tk.Label(ventana_taller, text="Departure Time (0.00-23.59):", font=("Times New Roman", 10), bg="gainsboro").pack()
    entrada_salida = tk.Entry(ventana_taller)
    entrada_salida.pack()

    tk.Button(ventana_taller, text="Pay for Bicycle", command=pagar_bici).pack()

    ventana_taller.mainloop()


user = Usuario()

ventana_login = tk.Tk()
ventana_login.title("Login - Taller de Bicicletas")
ventana_login.geometry("400x300+500+250")
ventana_login.configure(bg="gainsboro")
ventana_login.resizable(True, True)

tk.Label(ventana_login, text="Login",font=("Times New Roman", 12), bg="gainsboro").pack()
entrada_user = tk.Entry(ventana_login)
entrada_user.pack()

tk.Label(ventana_login, text="Password", font=("Times New Roman", 12), bg="gainsboro").pack()
entrada_password = tk.Entry(ventana_login, show="*")
entrada_password.pack()

tk.Button(ventana_login, text="Login", command=logearse).pack()

ventana_login.mainloop()