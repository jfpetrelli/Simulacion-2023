import scipy.stats as stat #utilizado para obtener el valor de chi cuadrado con N grados de libertad y un alfa.
import random 
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt

def generador_aleatorios_python(cantidadNumerosAleatorios,rango_desde, rango_hasta):
    lista = []
    for i in range(cantidadNumerosAleatorios):
        numero_aleatorio = random.randint(rango_desde, rango_hasta)
        lista.append(numero_aleatorio/10000)
    return lista

def generador_parte_media_del_cuadrado(cantidadNumerosAleatorios,semilla_parametro):
    semilla = semilla_parametro
    lista = []
    for i in range(cantidadNumerosAleatorios):
        cuadrado = semilla**2
        cadena = str(cuadrado).zfill(8)
        semillaActualizada = cadena[2:6]
        lista.append(int(semillaActualizada))
        semilla = int(semillaActualizada)
    return lista

def generador_congruencial_lineal(cantidadNumerosAleatorios,semilla_parametro,modulo,multiplicador,incremento):
    semilla = semilla_parametro
    lista = []
    for i in range(cantidadNumerosAleatorios):
        numero_aleatorio = ((multiplicador * semilla) + incremento ) % modulo
        lista.append(numero_aleatorio/modulo)
        semilla = numero_aleatorio
    return lista

def genera_Ejex(cantidadNumerosAleatorios,rango_hasta):
    lista = []
    for i in range(cantidadNumerosAleatorios):
        lista.append(i*rango_hasta/cantidadNumerosAleatorios)
    return lista

def genera_Ejex_De0a1(cantidadNumerosAleatorios,rango_hasta):
    lista = []
    for i in range(cantidadNumerosAleatorios):
        lista.append(i*rango_hasta/cantidadNumerosAleatorios/10000)
    return lista

def genera_VariableIndependiente(cantidadNumerosAleatorios):
    lista = []
    for i in range(cantidadNumerosAleatorios):
        lista.append(i)
    return lista

# Test Chi cuadrado
def test_chiCuadrado(lista):
    obs = []
    esp = []
    cant_elementos = len(lista)
    x2_max = 12.59
    for i in range(10):
        obs.append(0)
        esp.append(cant_elementos/10)

    obsesp = []
    obsesp2 = []
    chi_cuadrado = []

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    f = 0
    g = 0
    h = 0
    j = 0
    l = 0

    for i in lista:
        if (i < 0.1):
            obs[0] = a = a + 1
        elif (i >= 0.1 and i < 0.2):
            obs[1] = b = b + 1
        elif (i >= 0.2 and i < 0.3):
            obs[2] = c = c + 1
        elif (i >= 0.3 and i < 0.4):
            obs[3] = d = d + 1
        elif (i >= 0.4 and i < 0.5):
            obs[4] = e = e + 1
        elif (i >= 0.5 and i < 0.6):
            obs[5] = f = f + 1
        elif (i >= 0.6 and i < 0.7):
            obs[6] = g = g + 1
        elif (i >= 0.7 and i < 0.8):
            obs[7] = h = h + 1
        elif (i >= 0.8 and i < 0.9):
            obs[8] = j = j + 1
        elif (i >= 0.9 and i < 1):
            obs[9] = l = l + 1

    for i in range(10):
        obsesp.append(obs[i] - esp[i])
        obsesp2.append(obsesp[i] ** 2)
        chi_cuadrado.append((obsesp2[i] / esp[i]))

    chi_acum = sum(chi_cuadrado)

    if chi_acum < x2_max:
        estado = 'Aceptado'
    else:
        estado = 'Rechazado'
    return 'Test chicuadrados: ', estado


# TEST de Independencia: Corridas de Arriba y Abajo de la Media
def test_corridas_media (conjunto, media = 0.5, Z = 1.96):
    media_esperada = media
    n1 = 0
    n2 = 0
    b = 1
    aux = ''

    for n in conjunto:
        if n < media_esperada:
            n1 += 1
            if aux == 'sobre':
                b += 1
            aux = 'bajo'
        else:
            n2 += 1
            if aux == 'bajo':
                b += 1
            aux = 'sobre'

    N = n1 + n2
    if N <= 1:
        estado = 'Rechazado'

    else:
        media_test = (2 * n1 * n2 ) / (n1 + n2 ) +1
        varianza_test = (2 * n1 * n2 * (2 * n1 * n2 - N)) / (N ** 2 * (N - 1))
        if varianza_test != 0:
            z_muestra = (b - media_test) / sqrt(varianza_test)

            if z_muestra < Z:
                estado = 'Aceptado'
            else:
                estado = 'Rechazado'
        else:
            estado = 'Rechazado'

    return 'Test de corridas: ', estado

#Test Prueba de series
def test_prueba_series (conjunto):
    tabla = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    indice = [0, 0]
    N = len(conjunto)
    n = len(tabla)

    frecuencia_tabla = (N - 1) / n ** 2
    x_esperado = 36.42
    for i in range(N-1):
        pareja = [conjunto[i], conjunto[i+1]]
        for j in range(len(pareja)):
            if pareja[j] < 0.2:
                indice[j] = 0
            elif pareja[j] < 0.4:
                indice[j] = 1
            elif pareja[j] < 0.6:
                indice[j] = 2
            elif pareja[j] < 0.8:
                indice[j] = 3
            elif pareja[j] <= 1:
                indice[j] = 4
        tabla[indice[0]][indice[1]] += 1

    aux_sum = 0

    for i in range(n):
        for j in range(n):
            aux_sum += ((tabla[i][j] - frecuencia_tabla) ** 2)
    X = ((n ** 2) / (N - 1)) * aux_sum

    if X < x_esperado:
        estado = 'Aceptado'
    else:
        estado = 'Rechazado'
    return 'Test prueba de series: ', estado


rango_desde = 0
rango_hasta = 10000
numerosAleatoriosPython = []
numerosAleatoriosGLC = []
numerosParteMediaDelCuadrado = []
cantidadNumerosAleatorios = 1500

numerosAleatoriosPython = generador_aleatorios_python(cantidadNumerosAleatorios,rango_desde, rango_hasta)
semilla = 1991
numerosParteMediaDelCuadrado = generador_parte_media_del_cuadrado(cantidadNumerosAleatorios,semilla)

modulo = 32768 
multiplicador = 26765 
incremento = 21001
numeros_congruencial_lineal = generador_congruencial_lineal(cantidadNumerosAleatorios,semilla,modulo,multiplicador,incremento)


print("numerosAleatoriosPython")
print(numerosAleatoriosPython)
#print("-----------------------")
#print("numerosParteMediaDelCuadrado")
#print(numerosParteMediaDelCuadrado)
#print("-----------------------")
#print("numerosAleatoriosGCL")
#print(numeros_congruencial_lineal)

ejex_DiagramaPuntos = genera_VariableIndependiente(cantidadNumerosAleatorios)

listaOrdenadaAleatoriosPython = []
ListaOrdenadaMediaDelCuadrado = []
listaOrdenadaAleatoriosPython = sorted(numerosAleatoriosPython)
ListaOrdenadaMediaDelCuadrado = sorted(numerosParteMediaDelCuadrado)

#print("variable listaOrdenadaAleatoriosPython")
#print(listaOrdenadaAleatoriosPython)

#print("variable ListaOrdenadaMediaDelCuadrado")
#print(ListaOrdenadaMediaDelCuadrado)

print("Resultados de tests generador python")
resultado_test_chi2 = test_chiCuadrado(numerosAleatoriosPython)
resultado_test_corridas = test_corridas_media(numerosAleatoriosPython)
resultado_test_prueba_series = test_prueba_series(numerosAleatoriosPython)
print(resultado_test_chi2)
print(resultado_test_corridas)
print(resultado_test_prueba_series)

print("Resultados de tests GCL")
resultado_test_chi2 = test_chiCuadrado(numeros_congruencial_lineal)
resultado_test_corridas = test_corridas_media(numeros_congruencial_lineal)
resultado_test_prueba_series = test_prueba_series(numeros_congruencial_lineal)
print(resultado_test_chi2)
print(resultado_test_corridas)
print(resultado_test_prueba_series)

print("Resultados de tests generador parte media del cuadrado")
resultado_test_chi2 = test_chiCuadrado(numerosParteMediaDelCuadrado)
resultado_test_corridas = test_corridas_media(numerosParteMediaDelCuadrado)
resultado_test_prueba_series = test_prueba_series(numerosParteMediaDelCuadrado)
print(resultado_test_chi2)
print(resultado_test_corridas)
print(resultado_test_prueba_series)




x = genera_Ejex(cantidadNumerosAleatorios,rango_hasta)
plt.plot(x)
plt.plot(sorted(numerosParteMediaDelCuadrado))
plt.title("Números aleatorios con orden ascendente del método media del cuadrado")
plt.ylabel("Número aleatorio")
plt.xlabel("Orden")
plt.show() 


x = genera_Ejex(cantidadNumerosAleatorios,max(numeros_congruencial_lineal))
plt.plot(x)
plt.plot(sorted(numeros_congruencial_lineal))
plt.title("Números aleatorios con orden ascendente del método congruencial lineal")
plt.ylabel("Número aleatorio")
plt.xlabel("Orden")
plt.show() 


x = genera_Ejex(cantidadNumerosAleatorios,cantidadNumerosAleatorios)
plt.plot(x)
plt.plot(sorted(numerosAleatoriosPython))
plt.title("Números aleatorios con orden ascendente del generador python")
plt.ylabel("Número aleatorio")
plt.xlabel("Orden")
plt.show() 

x = genera_Ejex_De0a1(cantidadNumerosAleatorios,rango_hasta)
plt.scatter(ejex_DiagramaPuntos, numerosAleatoriosPython)
plt.xlabel("Numero aleatorio")
plt.ylabel("Valor")
plt.title("Diagrama de puntos generador python")
plt.show()

plt.scatter(ejex_DiagramaPuntos, numerosParteMediaDelCuadrado)
plt.xlabel("Numero aleatorio")
plt.ylabel("Valor")
plt.title("Diagrama de puntos generador parte media del cuadrado")
plt.show()

plt.scatter(ejex_DiagramaPuntos, numeros_congruencial_lineal)
plt.xlabel("Numero aleatorio")
plt.ylabel("Valor")
plt.title("Diagrama de puntos generador congruencial lineal")
plt.show()




# bibliografia
#https://www.victoriglesias.net/algoritmo-de-generacion-de-numeros-pseudoaleatorios/