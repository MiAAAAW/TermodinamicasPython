# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# from modules.GP_particule import *
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import tkinter as tk
# import datetime
# from tkinter import messagebox
# import tkinter.ttk as ttk

# class GazParfait():
#     def __init__(self,master) -> None:      
#         self.NOM_APPLI = "Gaz Parfait"  
#         self.animation = None
#         self.setup_window(master)
#         self.create_widgets()

#     def setup_window(self,master):
#         self.root = master
#         self.root.title(self.NOM_APPLI)
#         self.root.configure(bg="black")
#         self.root.resizable(False,False)

#     def create_widgets(self):
#         #on va créer les widgets
#         self.create_parameter_window() 
#         self.create_figure()
#         self.create_simulation_window()


        
#     def create_parameter_window(self):
#         #On a plusieurs paramètres à modifier, on va créer une frame pour les paramètres
#         self.parameter_frame = tk.Frame(self.root,bg="white")
#         self.parameter_frame.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

#         #premier paramètre: nombre de particules
#         self.nb_part_label = tk.Label(self.parameter_frame,text="Nombre de particules")
#         self.nb_part_label.grid(row=0,column=0)
#         self.nb_part_entry = tk.Entry(self.parameter_frame,width=10)
#         self.nb_part_entry.insert(0,"300")
#         self.nb_part_entry.grid(row=0,column=1)

#         #deuxième paramètre: taille de la boîte
#         self.taille_label = tk.Label(self.parameter_frame,text="Taille de la boîte")
#         self.taille_label.grid(row=1,column=0)
#         self.taille_entry = tk.Entry(self.parameter_frame,width=10)
#         self.taille_entry.insert(0,"100")
#         self.taille_entry.grid(row=1,column=1)

#         #troisième paramètre: durée de la simulation
#         self.duree_label = tk.Label(self.parameter_frame,text="Durée de la simulation")
#         self.duree_label.grid(row=2,column=0)
#         self.duree_entry = tk.Entry(self.parameter_frame,width=10)
#         self.duree_entry.insert(0,"20")
#         self.duree_entry.grid(row=2,column=1)

#         #quatrième paramètre: nombre d'itération
#         self.nb_iter_label = tk.Label(self.parameter_frame,text="Nombre d'itération")
#         self.nb_iter_label.grid(row=3,column=0)
#         self.nb_iter_entry = tk.Entry(self.parameter_frame,width=10)
#         self.nb_iter_entry.insert(0,"200")
#         self.nb_iter_entry.grid(row=3,column=1)

#         #cinquième paramètre: rayon des particules
#         self.rayon_label = tk.Label(self.parameter_frame,text="Rayon des particules")
#         self.rayon_label.grid(row=4,column=0)
#         self.rayon_entry = tk.Entry(self.parameter_frame,width=10)
#         self.rayon_entry.insert(0,"1")
#         self.rayon_entry.grid(row=4,column=1)

#         #sixième paramètre: masse des particules
#         self.masse_label = tk.Label(self.parameter_frame,text="Masse des particules")
#         self.masse_label.grid(row=5,column=0)
#         self.masse_entry = tk.Entry(self.parameter_frame,width=10)
#         self.masse_entry.insert(0,"1e-23")
#         self.masse_entry.grid(row=5,column=1)

#         #septième paramètre: température
#         self.temp_label = tk.Label(self.parameter_frame,text="Température")
#         self.temp_label.grid(row=6,column=0)
#         self.temp_entry = tk.Entry(self.parameter_frame,width=10)
#         self.temp_entry.insert(0,"300")
#         self.temp_entry.grid(row=6,column=1)

#         #huitième paramètre: mode mélange, on ajoute une checkbox pour ce mode
#         self.melange = tk.IntVar()
#         self.melange_check = tk.Checkbutton(self.parameter_frame,text="Mode mélange",variable=self.melange)
#         self.melange_check.grid(row=7,column=1)

#         #on ajoute un bouton pour lancer la simulation
#         self.lancer_button = tk.Button(self.parameter_frame,text="Lancer la simulation",command=self.lancer_simulation)
#         self.lancer_button.grid(row=8,column=0,columnspan=2)

#         #on ajoute un bouton pour sauvegarder la simulation
#         self.sauvegarder_button = tk.Button(self.parameter_frame,text="Sauvegarder",command=self.sauvegarder)
#         self.sauvegarder_button.grid(row=9,column=0,columnspan=2)

#         #on ajoute une barre de progression
#         self.progress_bar = ttk.Progressbar(self.parameter_frame,orient=tk.HORIZONTAL,length=200,mode='determinate')
#         self.progress_bar.grid(row=10,column=0,columnspan=2)
#         self.progress_bar["value"] = 0

#     def generer_liste_particules_melange(self):
#         #Données initiales spéciales
#         taille = int(self.taille_entry.get())
#         rayon, masse = float(self.rayon_entry.get()), float(self.masse_entry.get())
#         N = int(self.nb_part_entry.get())
#         colors = []
#         liste_particule = []
#         for i in range (N):
#             pos =  rayon + np.random.rand(2)*(taille-2*rayon) 
#             if pos[0]>taille/2:
#                 v= [np.random.rand() * -20,0]
#                 colors.append('r')
#             else:
#                 v= [np.random.rand() * 20,0]
#                 colors.append('b')
#             liste_particule.append(Particule(rayon, masse, pos, v))
#         return liste_particule, colors  
    
#     def lancer_simulation(self):
#         #on va lancer la simulation
#         #on va récupérer les paramètres
#         self.lancer_button["state"] = "disabled"
#         self.sauvegarder_button["state"] = "disabled"
#         #si la simulation est déjà lancée, on la stoppe
#         if self.animation != None:
#             self.animation.event_source.stop()
#             self.animation._stop()
#             self.animation = None
#         self.axs[0].cla()
#         self.axs[1].cla()
#         self.create_figure()
        
        
#         self.N = int(self.nb_part_entry.get())
#         self.taille = int(self.taille_entry.get())
#         self.duree = int(self.duree_entry.get())
#         self.nb_iteration = int(self.nb_iter_entry.get())
#         self.rayon = float(self.rayon_entry.get())
#         self.masse = float(self.masse_entry.get())
#         self.T = int(self.temp_entry.get())
#         print("Lancement de la simulation...")
#         print("paramètres: ")
#         print("Nombre de particules: ",self.N)
#         print("Taille de la boîte: ",self.taille)
#         print("Durée de la simulation: ",self.duree)
#         print("Nombre d'itération: ",self.nb_iteration)
#         print("Rayon des particules: ",self.rayon)

#         #on va créer la liste de particules
#         dt = self.duree/self.nb_iteration

        
#         #On va créer le scatter plot
#         # Initialisation des sous-graphiques
#         if self.melange.get() == 1:
#             liste_particule, colors = self.generer_liste_particules_melange()
#             self.v, self.distrib = MB_distribution(liste_particule)
#         else:
#             liste_particule = generation_liste_particules_bis(self.N,self.rayon,self.masse, self.taille,self.T)
#             colors = np.random.rand(self.N)
#             self.v, self.distrib = MB_distribution_bis(liste_particule,self.T)
#         x0,y0 = [liste_particule[j].all_pos[0][0] for j in range(self.N)], [liste_particule[j].all_pos[0][1] for j in range(self.N)]
#         self.points = self.axs[0].scatter(x0, y0, s = 50**(self.rayon), alpha=0.7,c=colors, label='Température: '+str(self.T)+str(' K'))

#         self.frames = []
#         for i in range(self.nb_iteration):
#             self.frames.append(liste_particule)
#             maj_all_pos(liste_particule, dt, self.taille)
#             self.progress_bar["value"] = i/self.nb_iteration*100
#             self.root.update()
#             if i%40==0:
#                 print("Itération numéro ",i, "...")
#         print("Fin simulation")

#         #on va calculer la pression
#         #pression = pression(liste_particule, 10)
#         self.pression = pression(liste_particule, 10)

#         self.animation = FuncAnimation(self.fig, self.update,init_func=self.init ,frames=self.nb_iteration, interval=20)
#         self.simulation_canvas.draw()
#         self.lancer_button["state"] = "normal"
#         self.sauvegarder_button["state"] = "normal"
    
#     def init(self):
#         #on va initialiser la figure
#         self.axs[0].set_xlim(0, self.taille)
#         self.axs[0].set_ylim(0, self.taille)
#         #self.axs[0].set_title('Position des particules')
#         self.axs[0].legend(loc='upper right')
    
#         self.axs[1].set_title('Histogramme des vitesses')
#         self.axs[1].set_xlabel('Vitesse')
#         self.axs[1].set_ylabel("Densité")

#         return self.points,
    
#     def update(self,i):
#         #on va mettre à jour la figure
#         #on va récupérer la liste de particules
#         liste_particule = self.frames[i]

#         #on va mettre à jour le scatter plot
#         x = [liste_particule[j].all_pos[i][0] for j in range(self.N)]
#         y = [liste_particule[j].all_pos[i][1] for j in range(self.N)]
#         self.axs[0].set_title(f'Pression : {self.pression[i%len(self.pression)]} Pa')
#         self.points.set_offsets(np.c_[x,y])

        
#         #on va mettre à jour l'histogramme
#         self.axs[1].clear()
#         self.axs[1].hist([liste_particule[j].all_vit_norme[i] for j in range(self.N)],bins=19,density=True)
#         self.axs[1].plot(self.v,self.distrib,label = "Théorie (Maxwell-Boltzmann)", color="yellow")
#         self.axs[1].grid(True, color='dimgrey',linewidth=0.5)
#         self.axs[1].set_ylim(0,np.max(self.distrib)*1.8)#np.max(self.distrib)*1.8
#         self.axs[1].set_xlim(0,np.max(self.v)*1.1) #np.max(self.v)*1.1
#         self.axs[1].legend()
#         self.simulation_canvas.draw()
#         self.root.update()
#         #self.axs[1].set_title('Histogramme des vitesses')
#         #self.axs[1].set_xlabel('Vitesse')
#         #self.axs[1].set_ylabel("Densité")

#         return self.points,


#     def create_figure(self):
#         #on va créer la figure matplotlib
#         plt.style.use('dark_background')
#         if not hasattr(self,"fig"):
#             self.fig, self.axs = plt.subplots(1, 2, figsize=(13, 6.5))

#         self.fig.set_facecolor("black")
#         self.axs[0].set_facecolor("black")
#         self.axs[1].set_facecolor("black")

#         self.axs[0].set_xlim(0, int(self.taille_entry.get()))
#         self.axs[0].set_ylim(0, int(self.taille_entry.get()))
#         self.axs[0].set_title('Position des particules')
#         self.axs[0].legend(loc='upper right')
    
#         self.axs[1].set_title('Histogramme des vitesses')
#         self.axs[1].set_xlabel('Vitesse')
#         self.axs[1].set_ylabel("Densité")

#         #je l'ai ajouté mais faut faire attention, je sais pas si c'est utile, à tester
#         self.axs[0].set_aspect('equal')
#         #self.axs[1].set_aspect('equal')
#         #self.fig.tight_layout()
        

#     def create_simulation_window(self):
#         #On va créer la fenêtre de simulation, cette fois ci on va utiliser matplotlib, donc on va créer un canvas spécial
#         self.simulation_frame = tk.Frame(self.root)
#         self.simulation_frame.grid(row=0,column=0)

#         self.simulation_canvas = FigureCanvasTkAgg(self.fig, master=self.simulation_frame)  # A tk.DrawingArea.
#         self.simulation_canvas.draw()
#         self.simulation_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

#     def sauvegarder(self):
#         #on va sauvegarder la simulation, çàd l'animation 
#         #on va créer un nom de fichier
#         now = datetime.datetime.now()
#         nom_fichier = "gaz_parfait_"+str(now.day)+"_"+str(now.month)+"_"+str(now.year)+"_"+str(now.hour)+"_"+str(now.minute)+"_"+str(now.second)+".gif"
#         if hasattr(self,"animation"):
#             self.animation.save(nom_fichier,fps=10)
#         else:
#             messagebox.showerror("Erreur","Vous devez d'abord lancer la simulation avant de pouvoir la sauvegarder")
    

#     def run(self):
#         self.root.mainloop()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from modules.GP_particula import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import datetime
from tkinter import messagebox
import tkinter.ttk as ttk

class GasPerfecto():
    def __init__(self, master) -> None:      
        self.NOMBRE_APLICACION = "Gas Perfecto"  
        self.animacion = None
        self.configurar_ventana(master)
        self.crear_widgets()

    def configurar_ventana(self, master):
        self.root = master
        self.root.title(self.NOMBRE_APLICACION)
        self.root.configure(bg="skyblue")
        self.root.resizable(False, False)

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
        self.casilla_mezcla.grid(row=7, column=1)

        # Añadimos un botón para iniciar la simulación
        self.boton_iniciar = tk.Button(self.frame_parametros, text="Iniciar simulación", command=self.iniciar_simulacion)
        self.boton_iniciar.grid(row=8, column=0, columnspan=2)

        # Añadimos un botón para guardar la simulación
        self.boton_guardar = tk.Button(self.frame_parametros, text="Guardar", command=self.guardar)
        self.boton_guardar.grid(row=9, column=0, columnspan=2)

        # Añadimos una barra de progreso
        self.barra_progreso = ttk.Progressbar(self.frame_parametros, orient=tk.HORIZONTAL, length=200, mode='determinate')
        self.barra_progreso.grid(row=10, column=0, columnspan=2)
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
