#Importamos la librería
import random

#Creamos una función para elegir nivel
def elegirnivel():
    print("Seleccione un nivel: \n ")
    print("1 = Fácil \n ")
    print("2 = Intermedio \n ")
    print("3 = Avanzado \n ")
    print("4 = Experto \n ")
    seleccionnivel = int(input("Seleccione un nivel: "))
    global eleccionnivel
    nivelelegido = seleccionnivel
    if 0 < nivelelegido <= 4 :
        if nivelelegido == 1 :
            print("Ha seleccionado el nivel fácil.")
        if nivelelegido == 2 :
            print("Ha seleccionado el nivel intermedio.")
        if nivelelegido == 3 :
            print("Ha seleccionado el nivel avanzado.")
        if nivelelegido == 4 :
            print("Ha seleccionado el nivel experto.")
    else:
        print(" \nSeleccione uno de los niveles establecidos (del 1 al 4)")