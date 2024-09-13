# from GP_particule import *
# from pytest import*

# def test_generation_liste_particules():
#     litest=generation_liste_particules(150,30,5,7)
#     assert len(litest)==150
#     assert litest[0].rayon==30
#     assert litest[0].masse==5

# test_generation_liste_particules()

# def test_generation_liste_particules_bis():
#     litest=generation_liste_particules_bis(150,30,5,7,273.15)
#     assert len(litest)==150
#     assert litest[0].rayon==30
#     assert litest[0].masse==5

# test_generation_liste_particules_bis()

# def test_energie_totale():
#     assert type(energie_totale(generation_liste_particules(150,30,5,7)))==np.float64
                
# test_energie_totale()




from modules.GP_particula import *
from pytest import *

def test_generacion_lista_particulas():
    lista_prueba = generacion_lista_particulas(150, 30, 5, 7)
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
    assert type(energia_total(generacion_lista_particulas(150, 30, 5, 7))) == np.float64
                
test_energia_total()
