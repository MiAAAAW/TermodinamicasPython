import tkinter as tk
from tkinter import messagebox
import modules.GP as GasPerfecto

class Interfaz(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Creamos el menú
        self.crear_menu()

        # Iniciar Gas Perfecto por defecto
        self.cambiar_a_gas_perfecto()

    def crear_menu(self):
        # Menú para la aplicación
        self.barra_menu = tk.Menu(self)

        # Menú de archivo con opción para salir
        menu_gasperfecto = tk.Menu(self.barra_menu, tearoff=0)
        menu_gasperfecto.add_command(label="Salir", command=self.quit)
        self.barra_menu.add_cascade(label="Archivo", menu=menu_gasperfecto)

        # Menú de ayuda
        menu_ayuda = tk.Menu(self.barra_menu, tearoff=0)
        menu_ayuda.add_command(label="Ayuda", command=self.ayuda_gas_perfecto)
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
        self.barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.config(menu=self.barra_menu)

    def ayuda_gas_perfecto(self):
        messagebox.showinfo("Ayuda Gas Perfecto", "Programa de simulación de gas perfecto con bolas...")

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "Esta aplicación fue creada por estudiantes...")

    def cambiar_a_gas_perfecto(self):
        # Iniciar Gas Perfecto
        print("Iniciando Simulacion")
        self.app = GasPerfecto.GasPerfecto(self)
        self.app.run()

if __name__ == "__main__":
    interfaz = Interfaz()
