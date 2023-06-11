import random
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy import stats

"""
 Generacion de valores estocasticas
"""
###### Auxiliares
def nuestro_random():
    r = random.random()
    return r
def x2(obs, esp):
    aux_x2 = [0] * len(esp)
    for i in range(len(esp)):
        aux_x2[i] = ((obs[i] - esp[i]) ** 2) / esp[i]
    sum_x2 = sum(aux_x2)
    x2 = [3.84, 5.99, 7.82, 9.49, 11.07, 12.59, 14.07, 15.51, 16.92, 18.31]
    i = len(obs) - 1
    if sum_x2 < x2[i]:
        estado = 'Aceptado'
    else:
        estado = 'rechazado'
    return estado
def sumas(conjunto):
    limite = max(conjunto)+1
    eje_y = [0] * limite
    eje_x = []
    for i in conjunto:
        eje_y[i] += 1
    for i in range(0, limite):
        eje_x.append(i+1)

    return eje_x, eje_y

###### Frecuencias tests
def frec_uniforme(conjunto, a, b):
    paso = (b - a) / 10
    obs = [0] * 10
    for i in range(0, len(conjunto)):
        aux = a + paso
        for j in range(0, 10):
            if conjunto[i] <= aux:
               obs[j] += 1

               break
            else:
                aux += paso
    esp = [len(conjunto)/10] * 10

    return obs, esp
def frec_exponencial(conjunto, alfa):
    paso = 0.5
    obs = [0] * 6
    esp = []
    aux = paso
    for i in range(0, 6):
        prob = stats.expon.cdf(aux)
        if i != 0:
            prob1 = stats.expon.cdf(aux-paso)
            prob -= prob1
        esp.append(prob*len(conjunto))
        aux += paso
    if esp[-1] != 50000:
        esp[-1] += (50000 - sum(esp))
    for i in range(0, len(conjunto)):
        aux = (paso / alfa)
        for j in range(0, 6):
            if conjunto[i] <= aux:
                obs[j] += 1
                break
            else:
                aux += (paso / alfa)
    if obs[-1] != 50000:
        obs[-1] += (50000 - sum(obs))
    return obs, esp

def frec_normal(conjunto, esp, var):
    std = math.sqrt(var)
    n = len(conjunto)
    resto = 1 - (0.023+0.136+0.341+0.341+0.136)
    obs = [0] * 6
    espe = [0.023 * n, 0.136 * n, 0.341 * n, 0.341 * n, 0.136 * n, resto * n]
    for i in conjunto:
        if i <= esp - 2 * std:
            obs[0] += 1
        elif i <= esp - 1 * std:
            obs[1] += 1
        elif i <= esp :
            obs[2] += 1
        elif i <= esp + 1 * std:
            obs[3] += 1
        elif i <= esp + 2 * std:
            obs[4] += 1
        else:
            obs[5] += 1
    return obs, espe
def frec_binomial(conjunto, n, p):
    paso = n / 10
    obs = [0] * 10
    esp = []
    aux = paso
    for i in range(0, 10):
        prob = stats.binom.cdf(aux, n, p)
        if i != 0:
            prob1 = stats.binom.cdf(aux-paso, n, p)
            prob -= prob1
        esp.append(prob*len(conjunto))
        aux += paso
    for i in range(0, len(conjunto)):
        aux = paso
        for j in range (0, 10):
            if conjunto[i] <= aux:
                obs[j] += 1
                break
            else:
                aux += paso

    return obs, esp
def frec_poisson(conjunto, mu):

    if mu <= 3:
        esp = []
        obs = [0] * 5
        paso = 1
        aux = paso
        acum = 0
        cant = len(conjunto)
        for i in range(0, 5):
            prob = stats.poisson.cdf(aux - 1, mu)
            prob -= acum
            esp.append(prob * cant)
            acum += prob
            aux += paso
        if sum(esp) != cant:
            esp[-1] += (cant - sum(esp))
        for i in range(0, cant):
            for j in range (0, 5):
                if conjunto[i] <= j:
                    obs[j] += 1
                    break
        if sum(obs) != cant:
            obs[-1] += (cant - sum(obs))

    else:
        obs, esp = frec_normal(conjunto, mu, mu)
    return obs, esp
def frec_empirica(conjunto, prob):
    obs = [0] * len(prob)
    esp = []
    for j in range (0, len(prob)):
        esp.append(len(conjunto) * prob[j])

    for i in conjunto:
        aux = prob[0]
        for j in range(0, len(prob)):
            if i <= j:
                obs[j] += 1
                break
    return obs, esp

######DISTRIBUCIONES CONTINUAS
def uniforme(r, a, b):
    """
    Distribucion uniforme
    Tecnica : Transformada inversa
    """
    x = a + (b - a) * r
    return x
def exponencial(a, b):
    x = -(1/b)*math.log(a)
    return x
def gamma(a, k):
    tr = 1
    for i in range(0, k):
        r = nuestro_random()
        tr *= r
    x = -1 * math.log(tr) / a
    return x
def normal( esp, var, k):
    sum = 0
    std = math.sqrt(var)
    for i in range(0, k):
        sum += nuestro_random()
    x = std * math.sqrt( 12 / k ) * (sum - k / 2) + esp
    return x
def pascal(k, q):
    tr = 1
    qr = math.log(q)
    for i in range(0, k):
        tr *= nuestro_random()
    x = math.log(tr) / qr
    x = int(x)
    return x
def binomial(n, p):
    x = 0
    for i in range(0, n):
        r = nuestro_random()
        if (r - p) <= 0:
            x += 1
    return x
def hypgeo(N, muestra, p):
    x = 0
    for i in range (0 , muestra):
        r = nuestro_random()
        if (r - p) <= 0:
            s = 1
            x += 1
        else:
            s = 0
        p = (N * p - s) / (N - 1)
        N -= 1
    return x
def poisson(lam):
    x = 0
    b = math.exp(-lam)
    tr = 1
    r = nuestro_random()
    tr *= r
    while (tr - b) >= 0:
        r = nuestro_random()
        tr *= r
        x += 1
    return x
def empirico (prob):
    r = nuestro_random()
    x=0
    acum = 0
    for i in range (0, len(prob)):
        acum += prob[i]
        if r <= acum:
            x = i
            break
    return x

#######Genera arreglos para estudio
def conjunto_uniforme(cant, a, b):

    num_uniformes = []

    for i in range(cant):
        r = nuestro_random()
        aux = uniforme(r, a, b)
        num_uniformes.append(aux)
    a_min = min(num_uniformes)
    b_max= max(num_uniformes)
    print("-----------------------------------------------------------")
    print("Valores teoricos: a(min) = ", a, ", b(max) = ", b, ", tamaño de muestra = ", cant)
    print("Esperanza: ", (b + a) / 2)
    print("Varianza: ", "%.3f" %((b - a)**2 / 12))
    print("Valores simulados: a(min) = %.3f" %(a_min), ", b(max) = %.3f " %(b_max))
    print("Esperanza: ", "%.3f" %np.mean(num_uniformes))
    print("Varianza: ", "%.3f" % np.var(num_uniformes))
    obs, esp = frec_uniforme(num_uniformes, a, b)
    print("Test de bondad Chi cuadrado: ", x2(obs, esp))
    print("-----------------------------------------------------------")
    return num_uniformes, a_min, b_max
def conjunto_exponencial(cant, alfa):
     num_exp = []
     conjunto=[]
     for i in range(cant):
        conjunto.append(nuestro_random())
        num_exp.append(exponencial(conjunto[i], alfa))
     print("-----------------------------------------------------------")
     print("Valor alfa: ", alfa)
     print("Valores teoricos:")
     print("Esperanza: %.3f" %(1/alfa))
     print("Varianza: %.3f" %(1/alfa)**2)
     print("Valores simulados:")
     print("Esperanza: %.3f" %np.mean(num_exp))
     print("Varianza: %.3f" %np.var(num_exp))
     obs, esp = frec_exponencial(num_exp,alfa)
     print("Test de bondad Chi cuadrado: ", x2(obs, esp))
     print("-----------------------------------------------------------")
     return num_exp
def conjunto_gamma(cant, a, k):

    num_gamma = []

    for i in range(cant):
        aux = gamma(a, k)
        num_gamma.append(aux)
    esperanza = np.mean(num_gamma)
    varianza = np.var(num_gamma)
    alfa = esperanza / varianza
    ko = (esperanza * esperanza) / varianza
    print("-----------------------------------------------------------")
    print("Valores de teoricos de simulacion: alpha = ", a, " k = ", k, ", tamaño de muestra = ", cant)
    print("Esperanza: ", "%.3f" % (k / a))
    print("Varianza: ", "%.3f" % (k / (a * a)))
    print("Valores de obtenidos de simulacion: alpha = ", "%.3f" %alfa, " k = ","%.3f" %ko)
    print("Esperanza: ", "%.3f" %esperanza)
    print("Varianza: ", "%.3f" % varianza)

    return num_gamma
def conjunto_normal(cant,  esp, var, k):

    num_normal = []

    for i in range(cant):
        aux = normal(esp, var, k)
        num_normal.append(aux)
    esperanza = np.mean(num_normal)
    varianza = np.var(num_normal)

    print("-----------------------------------------------------------")
    print("Valores teoricos de  simulacion: k = ", k, ", tamaño de muestra = ", cant)
    print("Esperanza: ", esp)
    print("Varianza: ", var)
    print("Valores de obtenidos de simulacion:")
    print("Esperanza: ", "%.3f" % esperanza)
    print("Varianza: ", "%.3f" % varianza)
    obs, esp = frec_normal(num_normal, esp, var)
    print("Test de bondad Chi cuadrado: ", x2(obs, esp))
    return num_normal

def conjunto_pascal(cant, k ,q):
    num_pascal = []
    for i in range(0, cant):
        num_pascal.append(pascal(k, q))
    esperanza_t = k * q / (1 - q)
    varianza_t = k * q / ((1 - q) * (1 - q))
    esperanza_s = np.mean(num_pascal)
    varianza_s = np.var(num_pascal)

    print("-----------------------------------------------------------")
    print("Valores de teoricos de simulacion: k = ", k, " q = ", q, ", tamaño de muestra = ", cant)
    print("Esperanza: ", esperanza_t)
    print("Varianza: ", varianza_t)
    print("Valores de obtenidos de simulacion:")
    print("Esperanza: ", "%.3f" % esperanza_s)
    print("Varianza: ", "%.3f" % varianza_s)
    return num_pascal
def conjunto_binomial(cant, n, p):
    num_binomial = []
    q = 1 - p
    for i in range(0, cant):
        num_binomial.append(binomial(n, p))
    esperanza_t = n * p
    varianza_t = n * p * q
    esps = np.mean(num_binomial)
    vars = np.var(num_binomial)
    ns = (esps * esps ) / (esps - vars)
    ps = (esps - vars) / esps

    print("-----------------------------------------------------------")
    print("Valores teoricos de  simulacion: tamaño de muestra = ", cant, ', n = ', n, ", p = ", p)
    print("Esperanza: ", "%.3f" %esperanza_t)
    print("Varianza: ", "%.3f" %varianza_t)
    print("Valores de obtenidos de simulacion:n = %.3f" %ns, ", p = %.3f" %ps)
    print("Esperanza: ", "%.3f" % esps)
    print("Varianza: ", "%.3f" % vars)
    obs, esp = frec_binomial(num_binomial, n, p)
    print("Test de bondad Chi cuadrado: ", x2(obs, esp))
    return num_binomial
def conjunto_hypgeo(cant, N, muestra, p):
    num_hypgeo = []
    q = 1 - p
    for i in range(0, cant):
        num_hypgeo.append(hypgeo(N, muestra, p))
    esperanza_t = muestra * p
    varianza_t = muestra * p * q * ((N - muestra) / (N - 1))
    esps = np.mean(num_hypgeo)
    vars = np.var(num_hypgeo)
    ns = (esps * esps) / (esps - vars)
    ps = (esps - vars) / esps

    print("-----------------------------------------------------------")
    print("Valores teoricos de  simulacion: tamaño de muestra = ", cant, ', N = ', N,", n =", muestra, ", p = ", p)
    print("Esperanza: ", "%.3f" % esperanza_t)
    print("Varianza: ", "%.3f" % varianza_t)
    print("Valores de obtenidos de simulacion:")
    print("Esperanza: ", "%.3f" % esps)
    print("Varianza: ", "%.3f" % vars)
    return num_hypgeo
def conjunto_poisson(cant, lam):
    num_poisson = []
    for i in range(0, cant):
        num_poisson.append(poisson(lam))
    esps = np.mean(num_poisson)
    vars = np.var(num_poisson)

    print("-----------------------------------------------------------")
    print("Valores teoricos de  simulacion: tamaño de muestra = ", cant, 'lambda = ', lam)
    print("Valores de obtenidos de simulacion:")
    print("Esperanza: ", "%.3f" % esps)
    print("Varianza: ", "%.3f" % vars)
    obs, esp = frec_poisson(num_poisson, lam)
    print("Test de bondad Chi cuadrado: ", x2(obs, esp))
    return num_poisson
def conjunto_empirico(cant, prob):
    num_empirico = []
    for i in range(0, cant):
        num_empirico.append(empirico(prob))
    esps = np.mean(num_empirico)
    vars = np.var(num_empirico)

    print("-----------------------------------------------------------")
    print("Valores teoricos de  simulacion: tamaño de muestra = ", cant)
    print(prob)
    print("Valores de obtenidos de simulacion:")
    print("Esperanza: ", "%.3f" % esps)
    print("Varianza: ", "%.3f" % vars)
    obs, esp = frec_empirica(num_empirico, prob)
    print("Test de bondad Chi cuadrado: ", x2(obs, esp))
    return num_empirico

#######Graficas
def bins_labels(bins, **kwargs):
    bin_w = (max(bins) - min(bins)) / (len(bins) - 1)
    plt.xticks(np.arange(min(bins)+bin_w/2, max(bins), bin_w), bins, **kwargs)
    plt.xlim(bins[0], bins[-1])
def graf_histograma_uniforme(conjunto, min = 0, max = 50):
    """
    Grafica: Histograma
    """
    custom_xlim = (min-5, max+5)
    custom_ylim = (0, 450)
    plt.xlim(custom_xlim)
    plt.ylim(custom_ylim)
    contenedores = int(max) - int(min)
    plt.hist(conjunto, bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
    plt.title('a = ' + str(min) + '    b = ' + str(max + 1))  # Colocamos el título
    plt.savefig('uniforme')
    plt.show()
def graf_histograma_exponencial(conjunto, alphas = [], min=0, max=50):
     """
     Grafica: 4 Histogramas
     """
     fig, axs = plt.subplots(2, 2)



     contenedores = int(max) - int(min)
     axs[0, 0].set_title('alfa = ' + str(alphas[0]), fontsize=10)  # type: ignore
     #axs[0, 0].hist(conjunto[0], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
     seaborn.distplot(conjunto[0], ax=axs[0, 0], kde=False)  # type: ignore
     axs[0, 1].set_title('alfa = ' + str(alphas[1]), fontsize=10)  # type: ignore
     #axs[0, 1].hist(conjunto[1], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
     seaborn.distplot(conjunto[1], ax=axs[0, 1], kde=False)  # type: ignore
     axs[1, 0].set_title('alfa = ' + str(alphas[2]), fontsize=10)  # type: ignore
     #axs[1, 0].hist(conjunto[2], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
     seaborn.distplot(conjunto[2], ax=axs[1, 0], kde=False)  # type: ignore
     axs[1, 1].set_title('alfa = ' + str(alphas[3]), fontsize=10)  # type: ignore
     #axs[1, 1].hist(conjunto[3], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
     seaborn.distplot(conjunto[3], ax=axs[1, 1], kde=False)  # type: ignore
     fig.tight_layout()
     plt.savefig('exponencial.png')
     plt.show()
def graf_histograma_gamma(conjunto, alphas = [], ks = [], min = 0, max = 50):
    """
    Grafica: 4 Histogramas
    """
    fig, axs = plt.subplots(2, 2)
    contenedores = int(max) - int(min)
    axs[0, 0].set_title('alfa = ' + str(alphas[0])+ '    k = '+ str(ks[0]), fontsize=10)  # type: ignore
    axs[0, 0].hist(conjunto[0], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)  # type: ignore
    #seaborn.distplot(conjunto[0], ax=axs[0, 0], )
    axs[0, 1].set_title('alfa = ' + str(alphas[1]) + '    k = ' + str(ks[1]), fontsize=10)  # type: ignore
    axs[0, 1].hist(conjunto[1], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)  # type: ignore
    #seaborn.distplot(conjunto[1], ax=axs[0, 1], )
    axs[1, 0].set_title('alfa = ' + str(alphas[2]) + '    k = ' + str(ks[2]), fontsize=10)  # type: ignore
    axs[1, 0].hist(conjunto[2], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)  # type: ignore
    #seaborn.distplot(conjunto[2], ax=axs[1, 0], )
    axs[1, 1].set_title('alfa = ' + str(alphas[3]) + '    k = ' + str(ks[3]), fontsize=10)  # type: ignore
    axs[1, 1].hist(conjunto[3], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)  # type: ignore
    #seaborn.distplot(conjunto[3], ax=axs[1, 1], )
    fig.tight_layout()
    plt.savefig('gamma.png')
    plt.show()
def graf_histograma_normal(conjunto, esp = [], var = [], k = [], min = 0, max = 50):
    """
    Grafica: 4 Histogramas
    """
    fig, axs = plt.subplots(2, 2)

    contenedores = int(max) - int(min)
    axs[0, 0].set_title('esperanza = ' + str(esp[0])+ ',varianza = '+ str(var[0])+ ', k = '+ str(k[0]), fontsize=10)  # type: ignore
    #axs[0, 0].hist(conjunto[0], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
    seaborn.distplot(conjunto[0], ax=axs[0, 0])  # type: ignore
    axs[0, 1].set_title('esperanza = ' + str(esp[1])+ ',varianza = '+ str(var[1])+ ', k = '+ str(k[1]), fontsize=10)  # type: ignore
    #axs[0, 1].hist(conjunto[1], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
    seaborn.distplot(conjunto[1], ax=axs[0, 1])  # type: ignore
    axs[1, 0].set_title('esperanza = ' + str(esp[2])+ ',varianza = '+ str(var[2])+ ', k = '+ str(k[2]), fontsize=10)  # type: ignore
    #axs[1, 0].hist(conjunto[2], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
    seaborn.distplot(conjunto[2], ax=axs[1, 0])  # type: ignore
    axs[1, 1].set_title('esperanza = ' + str(esp[3])+ ',varianza = '+ str(var[3])+ ', k = '+ str(k[3]), fontsize=10)  # type: ignore
    #axs[1, 1].hist(conjunto[3], bins=contenedores, alpha=1, edgecolor='black', linewidth=1)
    seaborn.distplot(conjunto[3], ax=axs[1, 1])  # type: ignore
    fig.tight_layout()
    plt.savefig('normal.png')
    plt.show()

def graf_histograma_pascal (conjunto,k ,q):

    x, y = sumas(conjunto)

    plt.title("   k = " + str(k) + "  q = "+ str(q))
    plt.bar(x, y, tick_label = x)
    #plt.hist(conjunto, bins=18,alpha=1, edgecolor='black', linewidth=1)
    plt.savefig('pascal')
    plt.show()

def graf_histograma_binomial(conjunto, n = [], p = [], min = 0, max = 50):
    """
    Grafica: Histograma
    """
    fig, axs = plt.subplots(2, 2)



    axs[0, 0].set_title('n = ' + str(n[0]) + ',p = ' + str(p[0]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[0])

    axs[0,0].bar(x, y)  # type: ignore

    axs[0, 1].set_title('n = ' + str(n[1]) + ',p = ' + str(p[1]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[1])

    axs[0,1].bar(x, y)  # type: ignore

    axs[1, 0].set_title('n = ' + str(n[2]) + ',p = ' + str(p[2]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[2])

    axs[1, 0].bar(x, y)  # type: ignore

    axs[1, 1].set_title('n = ' + str(n[3]) + ',p = ' + str(p[3]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[3])

    axs[1, 1].bar(x, y)  # type: ignore


    fig.tight_layout()
    plt.savefig('binomial')

    plt.show()
def graf_histograma_hypgeo(conjunto, N = [], muestra = [], p = [], min = 0, max = 50):
    """
    Grafica: Histograma
    """

    fig, axs = plt.subplots(2, 2)


    contenedores = int(max) - int(min)
    axs[0, 0].set_title('N = ' + str(N[0]) + 'n = ' + str(muestra[0]) + ',p = ' + str(p[0]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[0])

    axs[0, 0].bar(x, y,tick_label=x)  # type: ignore

    axs[0, 1].set_title('N = ' + str(N[1]) + 'n = ' + str(muestra[1]) + ',p = ' + str(p[1]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[1])

    axs[0, 1].bar(x, y,tick_label=x)  # type: ignore

    axs[1, 0].set_title('N = ' + str(N[2]) + 'n = ' + str(muestra[2]) + ',p = ' + str(p[2]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[2])

    axs[1, 0].bar(x, y,tick_label=x)  # type: ignore

    axs[1, 1].set_title('N = ' + str(N[3]) + 'n = ' + str(muestra[3]) + ',p = ' + str(p[3]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[3])

    axs[1, 1].bar(x, y,tick_label=x)  # type: ignore

    fig.tight_layout()
    plt.savefig('hypergeometrica')
    plt.show()
def graf_histograma_poisson(conjunto, lam = [], min = 0, max = 50):
    """
    Grafica: Histograma
    """
    fig, axs = plt.subplots(2)

    contenedores = int(max) - int(min)
    axs[0].set_title('lambda = ' + str(lam[0]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[0])

    axs[0].bar(x, y, tick_label=x)  # type: ignore

    axs[1].set_title('lambda = ' + str(lam[1]), fontsize=10)  # type: ignore
    x, y = sumas(conjunto[1])

    axs[1].bar(x, y, tick_label=x)  # type: ignore

    fig.tight_layout()

    plt.savefig('poisson')
    plt.show()
def graf_histograma_empirico(conjunto):
    """
        Grafica: Histograma
        """

    x, y = sumas(conjunto)

    plt.bar(x, y, tick_label=x)
    plt.title('distribucion empirico')  # Colocamos el título
    plt.savefig('empirico')
    plt.show()


###### Menu
def menu():
    print("Ingrese una opcion: ")
    print("")
    print("1 - Conjunto distribucion uniforme")
    print("2 - Conjunto distribucion exponencial")
    print("3 - Conjunto distribucion gamma")
    print("4 - Conjunto distribucion normal")
    print("5 - Conjunto distribucion pascal")
    print("6 - Conjunto distribucion binomial")
    print("7 - Conjunto distribucion hipergeometrica")
    print("8 - Conjunto distribucion poisson")
    print("9 - Conjunto distribucion empirica discreta")
    print("0 - Fin del programa")
    opc = input(str())
    return opc

###### programa principal

def main():
    opc = ""
    while opc != "0":
        opc = menu()
        # Conjunto distribucion uniforme
        if opc == "1":

            cant = 5000
            inf = 10
            sup = 30

            resultados = conjunto_uniforme(cant, inf, sup)
            graf_histograma_uniforme(resultados[0], int(resultados[1]), int(resultados[2]))



        # Conjunto distribucion exponencial
        if opc == "2":
            
            resultados=[]
            cant = 5000
            alfa = [0.1,0.5,1,10]
            resultados.append(conjunto_exponencial(cant,alfa[0]))
            resultados.append(conjunto_exponencial(cant,alfa[1]))
            resultados.append(conjunto_exponencial(cant,alfa[2]))
            resultados.append(conjunto_exponencial(cant,alfa[3]))
            graf_histograma_exponencial(resultados,alphas=alfa)


        # Conjunto distribucion Gamma
        if opc == "3":

            cant = 5000
            a = [2, 2, 2, 2]
            k = [1, 3, 7, 22]
            resultados = []
            resultados.append(conjunto_gamma(cant, a[0], k[0]))
            resultados.append(conjunto_gamma(cant, a[1], k[1]))
            resultados.append(conjunto_gamma(cant, a[2], k[2]))
            resultados.append(conjunto_gamma(cant, a[3], k[3]))
            graf_histograma_gamma(resultados, alphas=a, ks=k)

        # Conjunto distribucion normal
        if opc == "4":
            cant = 5000
            esperanza = [5 , 10, 5, 10]
            varianza = [0.5, 2, 2, 2]
            k = [12, 12, 12, 24]

            resultados = []
            resultados.append(conjunto_normal(cant, esperanza[0], varianza[0], k[0]))
            resultados.append(conjunto_normal(cant, esperanza[1], varianza[1], k[1]))
            resultados.append(conjunto_normal(cant, esperanza[2], varianza[2], k[2]))
            resultados.append(conjunto_normal(cant, esperanza[3], varianza[3], k[3]))
            graf_histograma_normal(resultados, esp=esperanza, var=varianza, k=k)
        # Conjunto distribucion pascal
        if opc == "5":
            cant = 5000
            k = [3]
            q = [0.5]
            resultados = []
            resultados.append(conjunto_pascal(cant, k[0], q[0]))
            graf_histograma_pascal(resultados[0], k[0], q[0])
        # Conjunto distribucion binomial
        if opc == "6":
            cant = 5000
            n = [20, 50, 20, 50]
            p = [0.5, 0.5, 0.2, 0.8]
            resultados = []
            for i in range(0, len(n)):
                resultados.append(conjunto_binomial(cant, n[i], p[i]))
            graf_histograma_binomial(resultados, n, p)
        # Conjunto distribucion hipergeometrica
        if opc == "7":
            cant = 5000
            N = [15, 25, 15, 25]
            muestra = [3, 10, 6, 10]
            p = [0.4, 0.2, 0.4, 0.8]
            resultados = []
            for i in range(0, len(N)):
                resultados.append(conjunto_hypgeo(cant, N[i], muestra[i], p[i]))
            graf_histograma_hypgeo(resultados, N, muestra, p)
        # Conjunto distribucion poisson
        if opc == "8":
            cant = 5000
            lamda = [1, 3]
            resultados = []
            for i in range(0, len(lamda)):
                resultados.append(conjunto_poisson(cant, lamda[i]))
            graf_histograma_poisson(resultados, lamda)
        # Conjunto distribucion empirica discreta
        if opc == "9":

            cant = 5000
            prob = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]

            resultados = conjunto_empirico(cant, prob)
            graf_histograma_empirico(resultados)
        #
if __name__ == '__main__':
   main()