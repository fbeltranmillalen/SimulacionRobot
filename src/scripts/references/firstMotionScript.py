import math
import matplotlib.pyplot as plt
import numpy as np

""""""""" 
Para plotear una funcion, tengo que tener un numero de valores para plotear 
para hacerlo se usa esta formula:
 
 [(El máximo número a mostrar) - (el menor numero a mostrar)
 ----------------------------------------------------------- + 1
       (del menor al máximo numero en pasos de...)
       
esa formula va a retornar de qué tamaño tiene que ser el array para que quepan todos los numeros del menor al mayor
en intervalos constantes.
             
minimo = 0
maximo = 10
intervalo = 0.1
n = math.ceil(((maximo - minimo) / intervalo) + 1)
print(n) # = 101
"""""""""

minimo = 0.0
maximo = 0.5
intervalo = 0.1
n = math.ceil(((maximo - minimo) / intervalo) + 1)
arrayTiempo = [] # s
arrayPosicionEnFuncionDelTiempo = [] # m
diccionarioTiempoPosicion = []

for i in range(int(n)):
    arrayTiempo.append(i*intervalo)

gravedad = 9.8 # m/s2
posicionInicial = 1.6 # m
for i in range(len(arrayTiempo)):
    posicionEnFuncionDelTiempo = posicionInicial - 0.5 * gravedad * arrayTiempo[i] ** 2
    arrayPosicionEnFuncionDelTiempo.append(posicionEnFuncionDelTiempo)
diccionarioTiempoPosicion = dict(zip(arrayTiempo, arrayPosicionEnFuncionDelTiempo))
print(diccionarioTiempoPosicion)


