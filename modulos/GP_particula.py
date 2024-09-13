
import numpy as np

# Constantes
kb = 1.38064852e-23  # Constante de Boltzmann

'''Clase principal para las diferentes simulaciones de gas perfecto, y funciones básicas para las simulaciones '''

class Particula():
    def __init__(self, radio, masa, posicion, velocidad):
        '''Inicializa los parámetros principales de la partícula, 
        posición y velocidad son vectores 2D de la forma [x, y] y [vx, vy]
        '''

        # Características principales
        self.masa = masa
        self.radio = radio
        self.posicion = np.array(posicion)
        self.velocidad = np.array(velocidad)

        # Almacena las posiciones y velocidades a lo largo de la simulación
        self.todas_pos = [np.copy(self.posicion)]
        self.todas_vit = [np.copy(self.velocidad)]
        self.todas_vit_norma = [np.linalg.norm(np.copy(self.velocidad))]
        self.contador = []

    def actualizar_pos(self, dt):
        """Actualización de la posición después de un tiempo dt"""
        self.posicion += dt * self.velocidad
        self.todas_pos.append(np.copy(self.posicion)) 
        self.todas_vit.append(np.copy(self.velocidad)) 
        self.todas_vit_norma.append(np.linalg.norm(np.copy(self.velocidad))) 

    def probar_colision(self, particula):
        """Devuelve True si hubo una colisión con la particula_probar
        Condición de colisión: la distancia entre los centros de ambas partículas 
        es menor que la suma de los dos radios + pequeño margen de error"""
        
        r1, r2 = self.radio, particula.radio
        pos1, pos2 = self.posicion, particula.posicion
        dist = np.linalg.norm(pos2-pos1)  # Distancia entre las dos partículas

        if dist < (r1 + r2):  # Condición de colisión 
            return True
        else:
            return False
        
    def actualizar_colision(self, particula, dt):
        """Actualización de las velocidades en caso de colisión con otra partícula"""
        
        r1, r2 = self.radio, particula.radio
        v1, v2 = self.velocidad, particula.velocidad
        m1, m2 = self.masa, particula.masa
        pos1, pos2 = self.posicion, particula.posicion
        d = pos1-pos2
        norma = np.linalg.norm(d)

        if norma < (r1 + r2):
            # Ecuaciones de colisión elástica
            self.velocidad = v1 - 2 * m2 / (m1 + m2) * np.dot(v1-v2, d) / (norma**2) * d
            particula.velocidad = v2 - 2 * m1 / (m2 + m1) * np.dot(v2-v1, (-d)) / (norma**2) * (-d)

    def actualizar_pared(self, dt, tamano):
        """Actualización de las velocidades en caso de que la partícula golpee una pared de la caja y rebote,
        caja de dimensión tamaño x tamaño.
        """
        contador = 0
        r, v = self.radio, self.velocidad
        x, y = self.posicion

        proyeccion_x = dt * abs(np.dot(v, np.array([1., 0.])))  # Proyección vertical de la posición
        proyeccion_y = dt * abs(np.dot(v, np.array([0., 1.])))  # Proyección horizontal de la posición

        if np.abs(x) - r < proyeccion_x or abs(tamano - x) - r < proyeccion_x:  # Condición para rebotar en la pared vertical
            self.velocidad[0] *= -1
            contador += 1
        if np.abs(y) - r < proyeccion_y or abs(tamano - y) - r < proyeccion_y:  # Condición para rebotar en la pared horizontal
            self.velocidad[1] *= -1
            contador += 1
        
        self.contador.append(contador)


    
def actualizar_todas_pos(liste_particules, dt, tamano):
    '''Función que permite actualizar el estado de las partículas después de un tiempo dt'''
    # Actualización de las velocidades en caso de colisión o rebote en la pared
    for i in range(len(liste_particules)):
        liste_particules[i].actualizar_pared(dt, tamano)
        for j in range(i + 1, len(liste_particules)):
            liste_particules[i].actualizar_colision(liste_particules[j], dt)

    # Actualización global
    for particula in liste_particules:
        particula.actualizar_pos(dt)


def energia_total(liste_particules): 
    '''Devuelve la energía total del gas'''
    E = sum([0.5 * liste_particules[i].masa * liste_particules[i].todas_vit_norma[0]**2 for i in range(len(liste_particules))])
    # NB: la energía es constante a lo largo del tiempo, de ahí que se escoja la energía en el instante inicial
    return E

def generar_lista_particulas(N, radio, masa, tamano):
    '''Creación de listas de partículas con estados iniciales aleatorios'''
    lista_particulas = []
    for i in range(N):
        pos = radio + np.random.rand(2) * (tamano - 2 * radio)
        v = np.random.uniform(-10, 10, size=2)
        lista_particulas.append(Particula(radio, masa, pos, v))
    return lista_particulas


def generacion_lista_particulas_bis(N, radio, masa, tamano, T):
    '''Creación de listas de partículas con estados iniciales aleatorios'''
    lista_particulas = []
    for i in range(N):
        pos = radio + np.random.rand(2) * (tamano - 2 * radio)
        v_cuadrada = np.sqrt(2 * kb * T / masa) * np.random.uniform(0.5, 1.5)
        angulo = np.random.rand() * 2 * np.pi
        v = [v_cuadrada * np.cos(angulo), v_cuadrada * np.sin(angulo)]
        lista_particulas.append(Particula(radio, masa, pos, v))
    return lista_particulas 


# Teoría, distribución Maxwell-Boltzmann

def distribucion_MB(liste_particules):
    E = energia_total(liste_particules)
    masa = liste_particules[0].masa
    E_media = E / len(liste_particules) 
    velocidades = [liste_particules[j].todas_vit_norma for j in range(len(liste_particules))]
    v = np.linspace(0, np.max(velocidades) * 1.6, 100)
    T = 2 * E_media / (2 * kb)  # Temperatura termodinámica
    distrib = masa * np.exp(-masa * v**2 / (2 * T * kb)) / (2 * np.pi * T * kb) * 2 * np.pi * v
    return v, distrib

def distribucion_MB_bis(liste_particules, T):
    masa = liste_particules[0].masa
    velocidades = [liste_particules[j].todas_vit_norma for j in range(len(liste_particules))]
    v = np.linspace(0, np.max(velocidades) * 1.7, 100)
    distrib = masa * np.exp(-masa * v**2 / (2 * T * kb)) / (2 * np.pi * T * kb) * 2 * np.pi * v
    return v, distrib

def presion(liste_particules, j):
    """Devuelve la presion por intervalo de tiempo correspondiente a j iteraciones"""
    N_it = len(liste_particules)
    choques = np.array(liste_particules[0].contador)
    for i in range(1, N_it):
        choques += liste_particules[i].contador

    presion = []
    for i in range(N_it - j):
        datos = sum(choques[i:i + j])
        presion.append(datos)
    for i in range(j):
        presion.append(datos)
    return presion


