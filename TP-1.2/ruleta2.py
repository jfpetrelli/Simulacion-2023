import random as rnd
import os  # La uso para limpiar la terminal a la hora de mostrar los menus
import matplotlib.pyplot as plt  # Importo la libreria matplotlib
import numpy as np  # Importo la libria Numpy

global cantApFav  # Define una variable global cantidad apuestas Favorables


def ruleta():  # Defino una funcion ruleta, devuelve un numero aleatorio entre 1 y 37
    return rnd.randint(1, 37)


def menu(): #Menu principal
    os.system('cls')
    print("*** MENU DE OPCIONES ***")
    print("Selecciona una opción")
    print("1 - Martingala")
    print("2 - Fibonacci")
    print("3 - D'Alambert")
    print("0 - Salir")
    while True:
        try:
            op = int(input("Ingrese su opción:  "))
        except ValueError:
            print("Debes ingresar un número (valido)")
            continue
        if op < 0 or op > 3:
            print("Debes ingresar un número comprendido entre 0 y 3")
            continue
        else:
            break
    return op


def menu2(s: str) -> int:   #este es el submenu 
    os.system('cls')
    print("***"+s+"***")
    print(" ")
    print("Selecciona un tipo de capital para la simulación")
    print("1 - Capital infinito")
    print("2 - Capital acotado")
    print("0 - Salir")
    while True:
        try:
            op = int(input("Ingrese su opción:  "))
        except ValueError:
            print("Debes ingresar un número (valido)")
            continue
        if op < 0 or op > 2:
            print("Debes ingresar un número comprendido entre 0 y 2")
            continue
        else:
            break
    return op


def valida_monto(): #Funcion para validar que ingrese un monto correcto NO letras, NO numeros negativos
    while True:
        try:
            monto = int(
                input('Indique el monto de capital inicial con el que comenzaremos $:  '))
        except ValueError:
            print("Debes ingresar un capital valido")
            continue
        if monto < 0:
            print("Debes ingresar un capital superior a 0")
            continue
        else:
            break
    return monto


def girar(calculaPromedio, modo, dinero_tot = None):
    if dinero_tot == None:
        dinero_disp = 0
    else:
        dinero_disp = dinero_tot
    valorApuesta = 1
    cantApFav = 0
    resultados = []
    resultados.append(dinero_disp)
    frecRelativa = []
    apuesta = 1
    if (modo == "Fibonacci"):
        contafib = 1

    for i in range(tiradas):
        result = ruleta()
        if (modo == "Martingala"):
            if (result % 2 == apuesta) & (result != 0):
                dinero_disp += valorApuesta
                valorApuesta = 1
                cantApFav += 1
            else:
                dinero_disp -= valorApuesta
                valorApuesta = valorApuesta*2
        elif (modo == "D'Alambert"):
            if (result % 2 == apuesta) & (result != 0):
                cantApFav += 1
                dinero_disp += valorApuesta
                if apuesta > 1:
                    valorApuesta = valorApuesta - 1
            else:
                dinero_disp -= valorApuesta
                valorApuesta = valorApuesta + 1
        elif (modo == "Fibonacci"):
            contafib = 0
            if (result % 2 == apuesta) & (result != 0):
                dinero_disp += valorApuesta
                cantApFav += 1
                if contafib < 3:
                    contafib = 1
                else:
                    contafib -= 2
            else:
                dinero_disp -= valorApuesta
                contafib += 1
            valorApuesta = fib(contafib)
        resultados.append(dinero_disp)
        frecRelativa.append(cantApFav/(i+1))
        if calculaPromedio:
            promedio[0][i] = promedio[0][i]+dinero_disp/repeticiones
            promedio[1][i] = promedio[1][i]+cantApFav/(i+1)/repeticiones
        if dinero_tot != None:
            if dinero_disp == 0:
                break
            elif dinero_disp < valorApuesta:
                valorApuesta = dinero_disp
    results = []
    results.append(frecRelativa)
    results.append(resultados)
    return results

def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def correr(modo, dinero_tot = None):
    if tiradas == 1:
        results = girar(False, modo, dinero_tot)
        plt.plot(results[0])
        plt.title(modo + " - Frecuencia relativa de apuestas ganadas")
        plt.hlines((18/37),0,tiradas, color='red')
        plt.ylabel('Frecuencia relativa')
        plt.xlabel('Numero total de apuestas')
        plt.show()

        plt.plot(results[1])
        plt.title(modo)
        if dinero_tot != None:
            plt.ylabel('Dinero')
            plt.hlines(cap_ini,0,tiradas, color='red')
        else:
            plt.ylabel('Beneficio acumulado')
            plt.hlines(0,0,tiradas, color='red')
        plt.xlabel('Numero de apuestas')
        plt.show()
    else:
        global promedio
        promedio = [[],[]]
        din = []
        fr = []
        for i in range(tiradas):
            promedio[0].append(0)
            promedio[1].append(0)

        for j in range(repeticiones):
            results = girar(True, modo, dinero_tot)
            fr.append(results[0])
            din.append(results[1])

        for i in range(repeticiones):
            plt.plot(fr[i])
        plt.plot(promedio[1], color='black', label='Promedio')
        plt.legend(loc="lower left")
        plt.title(modo + " - Frecuencia relativa de apuestas ganadas")
        plt.hlines((18/37),0,tiradas, color='red')
        plt.ylabel('Frecuencia relativa')
        plt.xlabel('Numero total de apuestas')
        plt.show()

        for i in range(repeticiones):
            plt.plot(din[i])
        plt.plot(promedio[0], color='black', label='Promedio')
        plt.legend(loc="lower left")
        plt.title(modo)

        if dinero_tot != None:
            plt.ylabel('Dinero')
            plt.hlines(cap_ini,0,tiradas, color='red')
        else:
            plt.ylabel('Beneficio acumulado')
            plt.hlines(0,0,tiradas, color='red')
        plt.xlabel('Numero de apuestas')
        plt.show()
        
# Programa principal
if __name__ == '__main__':
    os.system('cls')
    print("***CARGA DE DATOS INICIALES***")
    promedio = [[], []]
    repeticiones = int(input('Indique la cantidad de veces a repetir el experimento:  '))
    tiradas = int(input('Indique la cantidad de veces que se hara girar la ruleta:  '))
    
    while True:
        estrategia = menu()  # estrategia le puse este nombre por Seleccion de estrategia
        if estrategia == 1:
            while True:
                seleccion = menu2("Estrategia seleccionada Martingala")
                if seleccion == 2:
                    cap_ini = valida_monto()
                    correr("Martingala", cap_ini)
                elif seleccion == 1:
                    correr("Martingala")
                else:
                    break
        elif estrategia == 2:
            while True:
                seleccion = menu2("Estrategia seleccionada Fibonacci")
                if seleccion == 2:
                    cap_ini = valida_monto()
                    correr("Fibonacci", cap_ini)
                elif seleccion == 1:
                    correr("Fibonacci")
                else:
                    break
        elif estrategia == 3:
            while True:
                seleccion = menu2("Estrategia seleccionada D'Alambert")
                if seleccion == 2:
                    cap_ini = valida_monto()
                    correr("D'Alambert", cap_ini)
                elif seleccion == 1:
                    correr("D'Alambert")
                else: 
                    break
        else:
            print("Saliendo...")
            break
    print("FIN")
