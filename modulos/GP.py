
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from modulos.GP_particula import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import datetime
#from tkinter import messagebox
from tkinter import messagebox, PhotoImage
import tkinter.ttk as ttk

class GasPerfecto():
    def __init__(self, master) -> None:      
        self.NOMBRE_APLICACION = "THERMOXSIMU"  
        self.animacion = None
        self.configurar_ventana(master)
        self.crear_widgets()
        self.cargar_icono()  # Cargar el logo como icono de la ventana


    def configurar_ventana(self, master):
        self.root = master
        self.root.title(self.NOMBRE_APLICACION)
        self.root.configure(bg="skyblue")
        self.root.resizable(False, False)

    def cargar_icono(self):
        # Cargar la imagen del logo (asegúrate de que la ruta sea correcta)
        self.icono = PhotoImage(file=r"C:/Users/INTEL/Desktop/ODIN LABORATORY/software/SimuXGas/logox.png")

        # Establecer el logo como icono en la barra de título
        self.root.iconphoto(False, self.icono)

    def crear_widgets(self):
        # Vamos a crear los widgets
        self.crear_ventana_parametros() 
        self.crear_figura()
        self.crear_ventana_simulacion()

    def crear_ventana_parametros(self):
        # Tenemos varios parámetros a modificar, vamos a crear un frame para los parámetros
        self.frame_parametros = tk.Frame(self.root, bg="white")
        self.frame_parametros.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Primer parámetro: número de partículas
        self.etiqueta_num_particulas = tk.Label(self.frame_parametros, text="Número de partículas")
        self.etiqueta_num_particulas.grid(row=0, column=0)
        self.entrada_num_particulas = tk.Entry(self.frame_parametros, width=10)
        self.entrada_num_particulas.insert(0, "300")
        self.entrada_num_particulas.grid(row=0, column=1)

        # Segundo parámetro: tamaño de la caja
        self.etiqueta_tamano = tk.Label(self.frame_parametros, text="Tamaño de la caja")
        self.etiqueta_tamano.grid(row=1, column=0)
        self.entrada_tamano = tk.Entry(self.frame_parametros, width=10)
        self.entrada_tamano.insert(0, "100")
        self.entrada_tamano.grid(row=1, column=1)

        # Tercer parámetro: duración de la simulación
        self.etiqueta_duracion = tk.Label(self.frame_parametros, text="Duración de la simulación")
        self.etiqueta_duracion.grid(row=2, column=0)
        self.entrada_duracion = tk.Entry(self.frame_parametros, width=10)
        self.entrada_duracion.insert(0, "20")
        self.entrada_duracion.grid(row=2, column=1)

        # Cuarto parámetro: número de iteraciones
        self.etiqueta_num_iteraciones = tk.Label(self.frame_parametros, text="Número de iteraciones")
        self.etiqueta_num_iteraciones.grid(row=3, column=0)
        self.entrada_num_iteraciones = tk.Entry(self.frame_parametros, width=10)
        self.entrada_num_iteraciones.insert(0, "200")
        self.entrada_num_iteraciones.grid(row=3, column=1)

        # Quinto parámetro: radio de las partículas
        self.etiqueta_radio = tk.Label(self.frame_parametros, text="Radio de las partículas")
        self.etiqueta_radio.grid(row=4, column=0)
        self.entrada_radio = tk.Entry(self.frame_parametros, width=10)
        self.entrada_radio.insert(0, "1")
        self.entrada_radio.grid(row=4, column=1)

        # Sexto parámetro: masa de las partículas
        self.etiqueta_masa = tk.Label(self.frame_parametros, text="Masa de las partículas")
        self.etiqueta_masa.grid(row=5, column=0)
        self.entrada_masa = tk.Entry(self.frame_parametros, width=10)
        self.entrada_masa.insert(0, "1e-23")
        self.entrada_masa.grid(row=5, column=1)

        # Séptimo parámetro: temperatura
        self.etiqueta_temp = tk.Label(self.frame_parametros, text="Temperatura")
        self.etiqueta_temp.grid(row=6, column=0)
        self.entrada_temp = tk.Entry(self.frame_parametros, width=10)
        self.entrada_temp.insert(0, "300")
        self.entrada_temp.grid(row=6, column=1)

        # Octavo parámetro: modo mezcla, añadimos una casilla de verificación para este modo
        self.modo_mezcla = tk.IntVar()
        self.casilla_mezcla = tk.Checkbutton(self.frame_parametros, text="Modo mezcla", variable=self.modo_mezcla)
        self.casilla_mezcla.grid(row=7, column=1, pady=(20, 0))

        # Añadimos un botón para iniciar la simulación
        self.boton_iniciar = tk.Button(self.frame_parametros, text="Iniciar simulación", command=self.iniciar_simulacion)
        self.boton_iniciar.grid(row=8, column=0, columnspan=2, pady=(20, 0))

        # Añadimos un botón para guardar la simulación
        self.boton_guardar = tk.Button(self.frame_parametros, text="Guardar", command=self.guardar)
        self.boton_guardar.grid(row=9, column=0, columnspan=2, pady=(20, 0))

        # Añadimos una barra de progreso
        self.barra_progreso = ttk.Progressbar(self.frame_parametros, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.barra_progreso.grid(row=15, column=0, columnspan=2, pady=(20, 0))
        self.barra_progreso["value"] = 0

    def generar_lista_particulas_mezcla(self):
        # Datos iniciales especiales
        tamano = int(self.entrada_tamano.get())
        radio, masa = float(self.entrada_radio.get()), float(self.entrada_masa.get())
        N = int(self.entrada_num_particulas.get())
        colores = []
        lista_particulas = []
        for i in range(N):
            pos = radio + np.random.rand(2) * (tamano - 2 * radio)
            if pos[0] > tamano / 2:
                v = [np.random.rand() * -20, 0]
                colores.append('r')
            else:
                v = [np.random.rand() * 20, 0]
                colores.append('b')
            lista_particulas.append(Particula(radio, masa, pos, v))
        return lista_particulas, colores 
    
    def mostrar_estadisticas(self):
        """Función para mostrar estadísticas finales de la simulación."""
        promedio_presion = np.mean(self.presion)
        temperatura_media = np.mean([float(self.entrada_temp.get()) for _ in range(self.num_iteraciones)])
        messagebox.showinfo("Estadísticas de la Simulación", f"Presión media: {promedio_presion:.2f} Pa\nTemperatura media: {temperatura_media:.2f} K") 
    
    def iniciar_simulacion(self):
        # Vamos a iniciar la simulación
        # Recuperamos los parámetros
        self.boton_iniciar["state"] = "disabled"
        self.boton_guardar["state"] = "disabled"
        # Si la simulación ya está en curso, la detenemos
        if self.animacion != None:
            self.animacion.event_source.stop()
            self.animacion._stop()
            self.animacion = None
        self.axs[0].cla()
        self.axs[1].cla()
        self.crear_figura()
        
        self.N = int(self.entrada_num_particulas.get())
        self.tamano = int(self.entrada_tamano.get())
        self.duracion = int(self.entrada_duracion.get())
        self.num_iteraciones = int(self.entrada_num_iteraciones.get())
        self.radio = float(self.entrada_radio.get())
        self.masa = float(self.entrada_masa.get())
        self.T = int(self.entrada_temp.get())
        print("Iniciando la simulación...")
        print("Parámetros: ")
        print("Número de partículas: ", self.N)
        print("Tamaño de la caja: ", self.tamano)
        print("Duración de la simulación: ", self.duracion)
        print("Número de iteraciones: ", self.num_iteraciones)
        print("Radio de las partículas: ", self.radio)

        # Creamos la lista de partículas
        dt = self.duracion / self.num_iteraciones
        
        # Creamos el scatter plot
        # Inicializamos los subgráficos
        if self.modo_mezcla.get() == 1:
            lista_particulas, colores = self.generar_lista_particulas_mezcla()
            self.v, self.distrib = distribucion_MB(lista_particulas)
        else:
            lista_particulas = generacion_lista_particulas_bis(self.N, self.radio, self.masa, self.tamano, self.T)
            colores = np.random.rand(self.N)
            self.v, self.distrib = distribucion_MB_bis(lista_particulas, self.T)
        x0, y0 = [lista_particulas[j].todas_pos[0][0] for j in range(self.N)], [lista_particulas[j].todas_pos[0][1] for j in range(self.N)]
        self.puntos = self.axs[0].scatter(x0, y0, s=50 ** (self.radio), alpha=0.7, c=colores, label='Temperatura: ' + str(self.T) + str(' K'))

        self.frames = []
        for i in range(self.num_iteraciones):
            self.frames.append(lista_particulas)
            actualizar_todas_pos(lista_particulas, dt, self.tamano)
            self.barra_progreso["value"] = i / self.num_iteraciones * 100
            self.root.update()
            if i % 40 == 0:
                print("Iteración número ", i, "...")
        print("Fin de la simulación")

       
        self.presion = presion(lista_particulas, 10)

     
        self.animacion = FuncAnimation(self.fig, self.actualizar, init_func=self.inicializar, frames=self.num_iteraciones, interval=20, blit=False)
        self.canvas_simulacion.draw()
        self.boton_iniciar["state"] = "normal"
        self.boton_guardar["state"] = "normal"
        self.mostrar_estadisticas()     
    
    def inicializar(self):
        # Inicializamos la figura
        self.axs[0].set_xlim(0, self.tamano)
        self.axs[0].set_ylim(0, self.tamano)
        self.axs[0].legend(loc='upper right')
    
        self.axs[1].set_title('Histograma de velocidades')
        self.axs[1].set_xlabel('Velocidad')
        self.axs[1].set_ylabel("Densidad")

        return self.puntos,
    
    def actualizar(self, i):
        # Actualizamos la figura
        lista_particulas = self.frames[i]

        # Actualizamos el scatter plot
        x = [lista_particulas[j].todas_pos[i][0] for j in range(self.N)]
        y = [lista_particulas[j].todas_pos[i][1] for j in range(self.N)]
        self.axs[0].set_title(f'Presion: {self.presion[i % len(self.presion)]} Pa')
        self.puntos.set_offsets(np.c_[x, y])

        # Actualizamos el histograma
        self.axs[1].clear()
        self.axs[1].hist([lista_particulas[j].todas_vit_norma[i] for j in range(self.N)], bins=19, density=True)
        self.axs[1].plot(self.v, self.distrib, label="Teoría (Maxwell-Boltzmann)", color="yellow")
        self.axs[1].grid(True, color='dimgrey', linewidth=0.5)
        self.axs[1].set_ylim(0, np.max(self.distrib) * 1.8)
        self.axs[1].set_xlim(0, np.max(self.v) * 1.1)
        self.axs[1].legend()
        self.canvas_simulacion.draw()
        self.root.update()

        return self.puntos,

    def crear_figura(self):
    # Creamos la figura matplotlib
        plt.style.use('dark_background')
        if not hasattr(self, "fig"):
            self.fig, self.axs = plt.subplots(1, 2, figsize=(13, 6.5))

        self.fig.set_facecolor("black")
        self.axs[0].set_facecolor("black")
        self.axs[1].set_facecolor("black")

        self.axs[0].set_xlim(0, int(self.entrada_tamano.get()))
        self.axs[0].set_ylim(0, int(self.entrada_tamano.get()))
        self.axs[0].set_title('Posición de las partículas')

        # Aquí se supone que deberías tener algo como un scatter plot o una gráfica
        # Asegúrate de agregar gráficos con un `label`
        self.points = self.axs[0].scatter([0], [0], s=50, label='Partículas')  # Ejemplo de scatter con un label

        # Solo llama a `legend()` si hay etiquetas definidas
        self.axs[0].legend(loc='upper right')

        self.axs[1].set_title('Histograma de velocidades')
        self.axs[1].set_xlabel('Velocidad')
        self.axs[1].set_ylabel("Densidad")

        self.axs[0].set_aspect('equal')

    def crear_ventana_simulacion(self):
        # Creamos la ventana de simulación, usando matplotlib, por lo que crearemos un canvas especial
        self.frame_simulacion = tk.Frame(self.root)
        self.frame_simulacion.grid(row=0, column=0)

        self.canvas_simulacion = FigureCanvasTkAgg(self.fig, master=self.frame_simulacion)  
        self.canvas_simulacion.draw()
        self.canvas_simulacion.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def guardar(self):
        # Guardamos la simulación, es decir, la animación
        # Creamos un nombre de archivo
        ahora = datetime.datetime.now()
        nombre_archivo = "gas_perfecto_" + str(ahora.day) + "_" + str(ahora.month) + "_" + str(ahora.year) + "_" + str(ahora.hour) + "_" + str(ahora.minute) + "_" + str(ahora.second) + ".gif"
        if hasattr(self, "animacion"):
            self.animacion.save(nombre_archivo, fps=10)
        else:
            messagebox.showerror("Error", "Debe iniciar la simulación antes de poder guardarla")
    

    def run(self):
        self.root.mainloop()
