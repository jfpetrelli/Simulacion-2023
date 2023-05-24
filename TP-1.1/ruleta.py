# TP de Simulacion (25/03/2023)

import random
import numpy as np
import matplotlib.pyplot as plt

n = 5000
 


def generaNumeros(tiradas):
   resultados = []
   for i in range(tiradas):
      resultados.append(random.randrange(37))
   return resultados



def mostrarFrecuenciaRelativa(lista):
   lista_frelat=[]
   for i in range(37):
      cant_nrorep = lista.count(i)/n
      lista_frelat.append(cant_nrorep)
   
   plt.plot(lista_frelat)



def mostrarVarianza(lista, varianza_esperada):
   lista_numeros=[]
   lista_vari=[]
   for i in lista:
      lista_numeros.append(i)
      lista_vari.append(np.var(lista_numeros))
   print(lista_vari,'\n')

   plt.axhline(varianza_esperada, color='red')
   plt.plot(lista_vari)




def mostrarMedia(lista, media_esperada):
   prom=[]
   acumi = 0
   pos=1

   for i in lista:
      acumi += i
      prom.append(acumi/pos)
      pos+=1
   
   plt.axhline(media_esperada, color='red')
   plt.plot(prom)
    



def mostrarDesvio(lista, desvio_esperado):

  numerosSum =[]
  desvios =[]
  tiradas = []
  for i, numero in enumerate(lista, start=1):   
    numerosSum.append(numero)
    des = np.sqrt(np.var(numerosSum))    
    tiradas.append(i)
    desvios.append(des)
    
  plt.axhline(desvio_esperado, color='r', linestyle='-')
  plt.plot(tiradas,desvios)









# programa ===================================================================

resultados_obtenidos = generaNumeros(n)

varianza_esperada = np.var(resultados_obtenidos)
media_esperada = np.mean(resultados_obtenidos)
desvio_esperado = np.sqrt(varianza_esperada)  

mostrarFrecuenciaRelativa(resultados_obtenidos)
plt.title("Frecuencias relativas")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Frecuencia")
plt.legend(["Frecuencia"], loc ="lower right")
plt.show()
mostrarVarianza(resultados_obtenidos, varianza_esperada)
plt.title("Tabla de varianzas ")
plt.xlabel("Tiradas")
plt.ylabel("Varianza")
plt.legend(["Varianza esperada", "Numeros obtenidos"], loc ="lower right")
plt.show()
mostrarMedia(resultados_obtenidos, media_esperada)
plt.title('Promedio Media ')
plt.xlabel('Tiradas')
plt.ylabel('Promedio Media')
plt.legend(["Media Esperada", "Resultado obtenido"], loc ="lower right")
plt.show()
mostrarDesvio(resultados_obtenidos, desvio_esperado)
plt.title("Desvío del número obtenido")
plt.xlabel("Tiradas")
plt.ylabel("Desvío")
plt.legend(["Desvío esperado", "Número de tiradas"], loc ="lower right")
plt.show()

#==============================================================================#



# repetir
resultados = []

for i in range(10):
   resultados.append(generaNumeros(n))

varianza_esperada = np.var(resultados)
media_esperada = np.mean(resultados)
desvio_esperado = np.sqrt(varianza_esperada)

# frecuencias
for i in range(len(resultados)):
   mostrarFrecuenciaRelativa(resultados[i])
plt.title("Frecuencias relativas en 10 tiradas")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Frecuencia")
plt.show()

# varianza
for i in range(len(resultados)):
   mostrarVarianza(resultados[i], varianza_esperada)
plt.title("Varianzas en 10 tiradas")
plt.xlabel("Tiradas")
plt.ylabel("Varianza")
plt.show()

# media
for i in range(len(resultados)):
   mostrarMedia(resultados[i], media_esperada)
plt.title('Promedio Media en 10 tiradas')
plt.xlabel('Tiradas')
plt.ylabel('Promedio Media')
plt.show()

# desvio
for i in range(len(resultados)):
   mostrarDesvio(resultados[i], desvio_esperado)
plt.title("Desvío del número obtenido en 10 tiradas")
plt.xlabel("Tiradas")
plt.ylabel("Desvío")
plt.show()


