
from modulos.GP_particula import *
from pytest import *

def test_generacion_lista_particulas():
    lista_prueba = generar_lista_particulas(150, 30, 5, 7)
    assert len(lista_prueba) == 150
    assert lista_prueba[0].radio == 30
    assert lista_prueba[0].masa == 5

test_generacion_lista_particulas()

def test_generacion_lista_particulas_bis():
    lista_prueba = generacion_lista_particulas_bis(150, 30, 5, 7, 273.15)
    assert len(lista_prueba) == 150
    assert lista_prueba[0].radio == 30
    assert lista_prueba[0].masa == 5

test_generacion_lista_particulas_bis()

def test_energia_total():
    assert type(energia_total(generar_lista_particulas(150, 30, 5, 7))) == np.float64
                
test_energia_total()
