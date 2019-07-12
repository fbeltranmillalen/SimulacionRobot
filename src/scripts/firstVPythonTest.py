from vpython import *
from src.scripts.R3 import R3
from src.scripts.Robot import Robot
from src.scripts.Coordenada import Coordenada
import math
import numpy as np


# TODO
# guardar todos los valores de posicion, velocidad y aceleracion en arreglos para poder hacer calculos con ellos
# mejorar la escena
# crear una flecha que describa la direccion del robot en tiempo real
# cambiar el orden de simulacion por obtencion de datos primero, despues graficar y despues renderizar
# mejorar el aspecto del robot

# agregar un label con el metodo numerico o analítico usado en la simulación


# Hacer un mejor plano R3, con tiles transparentes y cordenadas discretas
# iterar sobre estos pasos para ir mejorando la simulación

"""
velocidad = vector(1, 0, 1)
# creacion del espacio de coordenadas
r3 = R3()
r3.draw_r3()

# creacion de robot
robot = Robot(initial_position=vector(10, 1, 10), size=vector(4, 2, 2), color=color.red)
myRobot = robot.draw_robot()

# creacion de label que contiene a las coordenadas
coordenada = Coordenada(myRobot)
ncoordenada = coordenada.dibujar_coordenada()

# Crear una clase para darle una misión al robot, un objetivo
varr = arrow(pos=myRobot.pos, axis=vector(10, 0, 10), color=color.yellow)

# grafico
positionGraph = graph(xtitle="time", ytitle="position")
xPosCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
zPosCoord = gcurve(color=color.red, label="z-coord")  # a graphics curve

# grafico
velocityGraph = graph(xtitle="time", ytitle="velocity")
xVelCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
zVelCoord = gcurve(color=color.red, label="z-coord")  # a graphics curve

# grafico
accelerationGraph = graph(xtitle="time", ytitle="acceleration")
xAccCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
zAccCoord = gcurve(color=color.red, label="z-coord")  # a graphics curve
"""

#   problema : que posicion y orientacion
#   tiene nuestro robot despues de 20 seg
#   de aplicar velocidad lineal y angular
#   0,6 y 0

#   array tiempo
t_inicial = 0       # seg
t_final = 20        # seg
delta_t = 0.1     # seg
velocidad_lineal = 0.7  # m/s
velocidad_angular = 0.5  # m/s
array_size = int(math.ceil(((t_final - t_inicial) / delta_t) + 1))
tiempo_array = np.zeros(array_size, float)

for i in range(array_size-1):
    tiempo_array[i+1] = tiempo_array[i] + delta_t

velocidad_lineal_array = np.full(array_size, velocidad_lineal)
velocidad_angular_array = np.full(array_size, velocidad_angular)

posicion_x_array = np.zeros(array_size, float)
posicion_y_array = np.zeros(array_size, float)
angulo_orientacion_array = np.zeros(array_size, float)

velocidad_x_array = np.zeros(array_size, float)     # derivada de la posicion
velocidad_y_array = np.zeros(array_size, float)     # derivada de la posicion

for k in range(array_size):
    velocidad_x_array[k] = velocidad_lineal_array[k] * cos(angulo_orientacion_array[k])
    velocidad_y_array[k] = velocidad_lineal_array[k] * sin(angulo_orientacion_array[k])

    if k + 1 != array_size:
        posicion_x_array[k+1] = posicion_x_array[k] + delta_t*velocidad_x_array[k]
        posicion_y_array[k+1] = posicion_y_array[k] + delta_t*velocidad_y_array[k]
        angulo_orientacion_array[k+1] = angulo_orientacion_array[k] + delta_t*velocidad_angular_array[k]

print("velocidad_lineal_array")
print(velocidad_lineal_array)
print("velocidad_angular_array")
print(velocidad_angular_array)
print("posicion_x_array")
print(posicion_x_array)
print("posicion_y_array")
print(posicion_y_array)
print("angulo_orientacion_array")
print(angulo_orientacion_array)
print("velocidad_x_array")
print(velocidad_x_array)
print("velocidad_y_array")
print(velocidad_y_array)
print("tiempo_array")
print(tiempo_array)
#   =================================================================================================

# grafico
positionGraph = graph(xtitle="time", ytitle="position")
xPosCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
zPosCoord = gcurve(color=color.red, label="z-coord")  # a graphics curve
anguloCoord = gcurve(color=color.green, label="angulo")

for i in range(array_size):
    xPosCoord.plot(tiempo_array[i], posicion_x_array[i])
    zPosCoord.plot(tiempo_array[i], posicion_y_array[i])
    anguloCoord.plot(tiempo_array[i], angulo_orientacion_array[i])

# grafico
velocityGraph = graph(xtitle="time", ytitle="velocity")
xVelCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
zVelCoord = gcurve(color=color.red, label="z-coord")  # a graphics curve
velocidad_lineal_coord = gcurve(color=color.blue, label="velocidad-lineal")
velocidad_angular_coord = gcurve(color=color.green, label="velocidad-angular")

for i in range(array_size):
    xVelCoord.plot(tiempo_array[i], velocidad_x_array[i])
    zVelCoord.plot(tiempo_array[i], velocidad_y_array[i])
    velocidad_lineal_coord.plot(tiempo_array[i], velocidad_lineal_array[i])
    velocidad_angular_coord.plot(tiempo_array[i], velocidad_angular_array[i])

#   =================================================================================================

# creacion del espacio de coordenadas
r3 = R3()
r3.draw_r3()

# creacion de robot
robot = Robot(initial_position=vector(posicion_x_array[0], 1, posicion_y_array[0]), size=vector(4, 2, 2), color=color.red)
myRobot = robot.draw_robot()
attach_trail(myRobot)
# creacion de label que contiene a las coordenadas
coordenada = Coordenada(myRobot)
ncoordenada = coordenada.dibujar_coordenada()

#   =================================================================================================

posicion_y_correcta = 1
orientacion_referencia = vector(0, 1, 0)
origen = vector(0, 0, 0)

for i in range(array_size):
    rate(10)
    myRobot.pos = vector(posicion_x_array[i], posicion_y_correcta, posicion_y_array[i])
    myRobot.rotate(angle=radians(angulo_orientacion_array[i]), axis=orientacion_referencia, origin=origen)
    coordenada.actualizar_coordenada(ncoordenada, myRobot.pos)

"""
i = 0
delta = 0.005
while i < 100:
    rate(100)
    # mover
    velocidad = vector(cos(i), 0, sin(i))
    myRobot.pos = myRobot.pos + velocidad * delta
    aceleracion = velocidad
    coordenada.actualizar_coordenada(ncoordenada, myRobot.pos)
    # graph pos
    xPosCoord.plot(i, myRobot.pos.x)
    zPosCoord.plot(i, myRobot.pos.z)
    # vel grph integrar
    xVelCoord.plot(i, velocidad.x)
    zVelCoord.plot(i, velocidad.z)

    varr.pos = myRobot.pos
    i = i + delta
"""