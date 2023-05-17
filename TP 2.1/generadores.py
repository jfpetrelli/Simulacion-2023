import random
import scipy.stats as stats
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
import os

archivo = open("Resultados.txt", "w")
#Para tests
test = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
test2= [0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5,
        0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5,
        0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5,
        0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5,
        0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5, 0.0, 0.9, 0.1, 0.8, 0.2, 0.7, 0.3, 0.6, 0.4, 0.5,]
test_corridas = [41, 68, 89, 94, 74, 91, 55, 62, 36, 27, 19, 72, 75, 9, 54, 2, 1, 36, 16, 28, 18, 1,
                 95, 69, 18, 47, 23, 32, 82, 53, 31, 42, 73, 4, 83, 45, 13, 57, 63, 29]
test3 = [0.1, 0.1, 0.1, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.9]
media_corridas = sum(test_corridas) / len (test_corridas)


#Generadores
def medioCuadrado(semilla, cantidad):

    listaSemillas = [semilla]
    listaValores = []
    listaPseudo = []

    for i in range(cantidad):

        valor = int(listaSemillas[i]) ** 2
        valor = str(valor).zfill(8)
        listaValores.append(int(valor))

        pseudo = str(valor)[2:6]
        listaPseudo.append(float("0." + pseudo))

        if pseudo == "0000":
            break

        if i+1 != cantidad:
            listaSemillas.append(int(pseudo))

    return listaPseudo
def gcl(semilla, a, c,  m, cantidad):

    listaSemillas = [semilla]
    listaValores = []
    listaPseudo = []

    for i in range(cantidad):
        valor = (a * listaSemillas[i] + c) % m
        listaValores.append(valor)

        psuedo = valor / m
        listaPseudo.append(psuedo)

        if i+1 != cantidad:
            listaSemillas.append(valor)

    return listaPseudo

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
    """
        print("lista de frec observada: ", obs)
        print(sum(obs))
        print("lista de frec observada - esperada: ", obsesp)

        print("lista chi cuadrado: ", chi_cuadrado)
        print("sumatoria chi cuadrado: ", chi_acum)
        print("tabla chi cuadrada ", stats.chisquare(obs))
    """

    if chi_acum < x2_max:
        estado = 'Aceptado'
    else:
        estado = 'rechazado'
    return 'Test Chicuadrados: ', estado

"""    
print(test_chiCuadrado(test))
print(test_chiCuadrado(test2))
print(test_chiCuadrado(test3))
"""
# TEST DE POKER
'''
 indice -  DESCRIPCION               - Frecuencia esperada
    [0] - Todos distintos            - 0.3024
    [1] - un par                     - 0.5040
    [2] - dos pares                  - 0.1080
    [3] - pierna (tres iguales)      - 0.0720
    [4] - Full (par y pierna)        - 0.0090
    [5] - poker (cuatro iguales)     - 0.0045
    [6] - Todos iguales (5 iguales)  - 0.0001
  '''
def mano_poker(numero):

    contador = [0]*10
    if isinstance(numero, float):
        aux = str(numero)
        num = aux[2:7]
    else:
        aux = str(numero)
        num = aux[0:5]

    for digito in num:
        contador[int(digito)] += 1

    if contador.count(5) == 1:
        return 6, 'Todos iguales'
    elif contador.count(4) == 1:
        return 5, 'poker'
    elif contador.count(3) == 1 and contador.count(2) == 1:
        return 4, 'full'
    elif contador.count(3) == 1:
        return 3, 'Pierna'
    elif contador.count(2) == 2:
        return 2, 'par doble'
    elif contador.count(2) == 1:
        return 1, 'par simple'
    else:
        return 0, 'distintos'
def x2(obs, esp):
    aux_x2 = [0] * len(esp)
    for i in range(len(esp)):
        aux_x2[i] = ((obs[i] - esp[i]) ** 2) / esp[i]
    sum_x2 = sum(aux_x2)
    return sum_x2
def test_poker(conjunto):
# Objetivo
    #x2 6 grados de libertad, 95% = 12.59
    x2_maximo = 12.59
#Frecuencias esperadas
    #            distintos   par  pardoble pierna  full    poker  5iguales
    frecuencias = [0.3024, 0.5040, 0.1080, 0.0720, 0.0090, 0.0045, 0.0001]
    for i in range(len(frecuencias)):
         frecuencias[i] *= len(conjunto)

#Frecuencias observadas
    observadas = [0] * 7
    for numero in conjunto:
        tipo = mano_poker(numero)
        observadas[tipo[0]] += 1

    coef = x2(observadas, frecuencias)
    if coef < x2_maximo:
        estado = "Aceptado"
    else:
        estado = "rechazado"
    return 'Test Poker: ',  estado
"""
for i in range(10):
    semilla = random.randint(0,999999999)
    conjunto_gcl = gcl(semilla, 7 ** 5, 0, 2 ** 31, 150000)
    print('150.000 elemetos', test_poker(conjunto_gcl[2]))

a = True

while a:
    semilla = random.randint(0, 999999999)
    conjunto_gcl = gcl(semilla, 7 ** 5, 0, 2 ** 31, 150000)
   
    aux = test_poker(conjunto_gcl[2])
    print('150.000 elemetos', aux)
    if aux[1] == 'rechazado':
        a = False
"""

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
        estado = 'rechazado'

    else:
        media_test = (2 * n1 * n2 ) / (n1 + n2 ) +1
        varianza_test = (2 * n1 * n2 * (2 * n1 * n2 - N)) / (N ** 2 * (N - 1))
        if varianza_test != 0:
            z_muestra = (b - media_test) / sqrt(varianza_test)

            if z_muestra < Z:
                estado = 'Aceptado'
            else:
                estado = 'rechazado'
        else:
            estado = 'rechazado'

    return 'Test corridas: ', estado
"""
a = test_corridas_media(test2)
b = test_corridas_media(test)
c = test_corridas_media(test_corridas, media= 50)
print(a)
print(b)
print(c)
"""

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
    return 'Test Series: ', estado
"""
print(test_prueba_series(test))
print(test_prueba_series(test2))
"""
"""
def test_global(conjunto):
    print(test_chiCuadrado(conjunto))
    print(test_poker(conjunto))
    print(test_corridas_media(conjunto))
    print(test_prueba_series(conjunto))   
    return 
"""
def test_global(conjunto):
    t_chi = test_chiCuadrado(conjunto)
    t_poker = test_poker(conjunto)
    t_corri = test_corridas_media(conjunto)
    t_serie = test_prueba_series(conjunto)
    estado = 'Rechazado'
    archivo.write(str(t_chi)+"\n")
    archivo.write(str(t_poker)+"\n")
    archivo.write(str(t_corri)+"\n")
    archivo.write(str(t_serie)+"\n")
    if t_chi[1] == 'Aceptado' and t_poker[1] == 'Aceptado' and t_corri[1] == 'Aceptado' and t_serie[1] == 'Aceptado':
        estado = 'Aceptado'
    return estado

def test_global_gcl(conjunto):
    t_chi = test_chiCuadrado(conjunto)
    t_poker = test_poker(conjunto)
    t_corri = test_corridas_media(conjunto)
    t_serie = test_prueba_series(conjunto)
    estado = 'Rechazado'
    archivo.write(str(t_chi)+"\n")
    archivo.write(str(t_poker)+"\n")
    archivo.write(str(t_corri)+"\n")
    archivo.write(str(t_serie)+"\n")
    if t_chi[1] == 'Aceptado' and t_poker[1] == 'Aceptado' and t_corri[1] == 'Aceptado' and t_serie[1] == 'Aceptado':
        estado = 'Aceptado'
    return estado

""""
print('conjunto test')
test_global(test)
print('conjunto test2')
test_global(test2)
"""
def test_global_100():
    acept = 0
    recha = 0
    for i in range(100):
        archivo.write('Iteracion N°: '+ str(i+1) + "\n")
        semilla = random.randint(0, 999999999)
        archivo.write('Semilla: ' + str(semilla) + "\n")
        conjunto_gcl = gcl(semilla, 7 ** 5, 0, 2 ** 31, 15000)
        aux = test_global(conjunto_gcl)
        if aux == 'Aceptado':
            acept += 1
        else:
            recha += 1
        del (conjunto_gcl)
    resultado_global.append('Los resultados en 100 conjuntos de Random GCL con 15.000 elementos son:\n')
    resultado_global.append('aceptado: ' + str(acept) + "\n")
    resultado_global.append('rechazado: ' + str(recha)  + "\n")

def test_paramediocuadrados(conjunto):
    #no realiza el de poker porque esta programado para 5 digitos
    archivo.write(str(test_chiCuadrado(conjunto)) + "\n")
    archivo.write(str(test_corridas_media(conjunto)) + "\n")
    archivo.write(str(test_prueba_series(conjunto)) + "\n")
    return
"""






################################################

def semilla_aceptada_medio():
    resultado = 'Rechazado'
    semilla = random.randint(1, 9999)
    conjunto_md = medioCuadrado(semilla, 1000)
    a = test_chiCuadrado(conjunto_md[2])
    b = test_corridas_media(conjunto_md[2])
    c = test_prueba_series(conjunto_md[2])
    if a[1] == 'Aceptado' and b[1] == 'Aceptado' and c[1] == 'Aceptado':
        resultado = 'Aceptado'
    print('semilla: ', semilla)
    print(a, b, c)
    return resultado, semilla

aux = 'Rechazado'
contador = 1
while aux != 'Aceptado':
    print("iteracion numero: ", contador)
    respuesta = semilla_aceptada_medio()
    aux = respuesta[0]
    contador += 1

"""
def rand_python_100():
    acept = 0
    recha = 0
    for i in range(100):
        archivo.write('Iteracion N°: ' + str(i+1) + "\n")
        rand_python = []
        for i in range(15000):
            rand_python.append(random.random())
        aux = test_global(rand_python)
        if aux == 'Aceptado':
            acept += 1
        else:
            recha += 1
    resultado_python.append('Los resultados en 100 conjuntos de Random python con 15.000 elementos son:\n')
    resultado_python.append('aceptado: ' + str(acept) + "\n")
    resultado_python.append('rechazado: ' + str(recha) + "\n")

def grafica_dispersion(conjunto):
    n = int(len(conjunto) / 100)
    puntos = []
    promedios = []
    media = []
    for i in range(10):
        inf = 0 + i * n
        sup = n + i * n
        aux = conjunto[inf:sup]
        puntos.append(aux)
#Promedio de X
    for i in range(n):
        sum = 0
        for j in range(10):
            sum += puntos[j][i]
        promedios.append(sum / 10)
#media acumulada
    sum = 0
    for i in range(n):
        sum += promedios[i]
        media.append(sum / (i+1))

    x = np.linspace(1, n, n)
    for i in range(len(puntos)):
        plt.scatter(x, puntos[i],s=50, color='black')
    plt.plot(x, promedios, color='red', label= 'Promedio')
    plt.plot(x, media, color='blue', label= 'Media')
    plt.legend(loc = "upper left")
    plt.title('Grafica de Dispersion de GCL')
    plt.show()

def grafica_dispersion_md(conjunto):
    n = int(len(conjunto) / 100)
    puntos = []
    promedios = []
    media = []
    for i in range(10):
        inf = 0 + i * n
        sup = n + i * n
        aux = conjunto[inf:sup]
        puntos.append(aux)
#Promedio de X
    for i in range(n):
        sum = 0
        for j in range(10):
            sum += puntos[j][i]
        promedios.append(sum / 10)
#media acumulada
    sum = 0
    for i in range(n):
        sum += promedios[i]
        media.append(sum / (i+1))

    x = np.linspace(1, n, n)
    for i in range(len(puntos)):
        plt.scatter(x, puntos[i],s=50, color='black')
    plt.plot(x, promedios, color='red', label= 'Promedio')
    plt.plot(x, media, color='blue', label= 'Media')
    plt.legend(loc = "upper left")
    plt.title('Grafica de Dispersion de MC')
    plt.show()

semilla = random.randint(1000, 9999)
conjunto_md = medioCuadrado(semilla, 10000)
print('Conjunto medios cuadrados\nSemilla: ', semilla)
test_paramediocuadrados(conjunto_md)
grafica_dispersion_md(conjunto_md)

semilla = random.randint(0, 99999999999999999999999999999999)
conjunto_gcl = gcl(semilla, 7 ** 5, 0, 2 ** 31, 10000)
print('conjunto gcl\nSemilla: ', semilla)
test_global_gcl(conjunto_gcl)
grafica_dispersion(conjunto_gcl)



resultado_global = list()
resultado_python = list()


test_global_100()
rand_python_100()

archivo.write("\n" + (resultado_global[0]  + resultado_global[1] + resultado_global[2] + "\n"))
archivo.write((resultado_python[0]  + resultado_python[1] + resultado_python[2] + "\n"))
archivo.close()



