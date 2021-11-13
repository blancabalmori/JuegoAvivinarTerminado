#Importamos la librería
import random
import tabulate
from tabulate import TableFormat, tabulate

#Creamos una función para elegir dificultal
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
    
#Desarrollo del juego dependiendo de la dificultad
def juego():
    print("Seleccione un modo: ")
    print("1 = Usuario \n ")
    print("2 = IA \n ")  
    modoelegido = int(input("¿En qué modo desea jugar?: "))
    eleccionmodo = modoelegido
    if 0 < eleccionmodo <= 4 :
        if eleccionmodo == 1 :
            print("Usted ha seleccionado el modo USUARIO.")
        if eleccionmodo == 2 :
            print("Usted ha seleccionado el modo IA.")
        
    else:
        print(" \nSeleccione uno de los modos establecidos (del 1 al 2)")

    if eleccionmodo == 1:
        nintentos = 0
        while nintentos < maxintentos :
            print("\nIntente adivinar el número: ")
            intento = int(input())
            nintentos += 1

            if intento < numero :
                print("\nTe has quedado por debajo del número generado. ")
                print("Te quedan " + str(maxintentos-nintentos) + " intentos.\n")
            if intento > numero :
                print("\nTe has quedado por encima del número generado. ")
                print("Te quedan " + str(maxintentos-nintentos) + " intentos.\n")
            if intento == numero :
                break       
    
        if intento == numero :
            print("Has logrado acertar el número con " + str(nintentos) + " intentos.")
            puntuacion = maxintentos - nintentos
            nombre = str(input("\nIntroduzca su nombre: "))
            tabla = [[" Nombre", "Nivel de dificultad ", "Puntuación "], [nombre, eleccionnivel, puntuacion]]
            print(tabulate(tabla, headers="firstrow", tablefmt="grid"))
        if intento != numero :
            print("Lo sentimos, no has logrado acertar el número en los " + str(maxintentos) + " intentos que tenías.")

    if eleccionmodo == 2:
        nintentos = 0
        minIA = min
        maxIA = max
        intento = (minIA+maxIA)//2
        while intento != numero and nintentos < maxintentos :
            intento = (minIA+maxIA)//2
            nintentos += 1
            print("La IA ha probado el número "+ str(intento) + " y ")
            if intento > numero :
                print("se ha quedado por encima del número generado.\n")
                print("Le quedan " + str(maxintentos-nintentos) + " intentos.\n")
                maxIA = intento
            elif intento < numero :
                print("se ha quedado por debajo del número generado.\n")
                print("Le quedan " + str(maxintentos-nintentos) + " intentos.\n")
                minIA = intento + 1
        print("es el correcto.")
        print("\nLe ha costado " + str(nintentos) + " intentos y por tanto le han sobrado " + str(maxintentos-nintentos) + " intentos.")

elegirnivel()

if eleccionnivel == 1 :
    maxintentos = 20
    nintentos = 0
    min = 0
    max = 100
    numero = random.randint(min, max)
    print(" \nA continuación se le va a pedir que adivine un número generado del 0 al 100.\n ")
    juego()

if eleccionnivel == 2 :
    maxintentos = 50
    nintentos = 0
    min = 0
    max = 1000
    numero = random.randint(min, max)
    print(" \nA continuación se le va a pedir que adivine un número generado del 0 al 1000.\n")
    juego()

if eleccionnivel == 3 :
    maxintentos = 100
    nintentos = 0
    min = 0
    max = 1000000
    numero = random.randint(min, max)
    print(" \nA continuación se le va a pedir que adivine un número generado del 0 al 1000000.\n")
    juego()

if eleccionnivel == 4 :
    maxintentos = 500
    nintentos = 0
    min = 0
    max = 1000000000000
    numero = random.randint(min, max)
    print(" \nA continuación se le va a pedir que adivine un número generado del 0 al 1000000000000.\n")
    juego()