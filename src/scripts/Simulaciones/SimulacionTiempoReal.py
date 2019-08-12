from vpython import *

from src.scripts.Clases.R3 import R3
from src.scripts.Clases.Robot import Robot
from src.scripts.Clases.Coordenada import Coordenada
import math
import numpy as np

VECTOR_UNITARIO_I_TONGO_HORIZONTAL = vector(1, 0, 0)
VECTOR_UNITARIO_J_TONGO_VERTICAL = vector(0, 1, 0)
VECTOR_UNITARIO_Z_TONGO_PROFUNDIDAD = vector(0, 0, 1)
ORIGEN = vector(0, 0, 0)
SEGUIR_AL_ROBOT_CON_LA_CAMARA = False
# TODO
# mejorar la escena
# agregar un label con el metodo numerico o analítico usado en la simulación
# Hacer un mejor plano R3, grid, no es prioridad
# iterar sobre estos pasos para ir mejorando la simulación
# crear un arreglo con coordenada z para hacer más universal el código


#   problema : que posicion y orientacion
#   tiene nuestro robot despues de 20 seg
#   de aplicar velocidad lineal y angular
#   0,6 y 0

t_inicial = 0  # seg
t_final = 20  # seg
delta_t = 0.01  # seg
velocidad_lineal = 5.0  # m/s
velocidad_angular = 10.5  # m/s
array_size = int(math.ceil(((t_final - t_inicial) / delta_t) + 1))
tiempo_array = np.zeros(array_size, float)

for i in range(array_size - 1):
    tiempo_array[i + 1] = tiempo_array[i] + delta_t

velocidad_lineal_array = np.full(array_size, velocidad_lineal)
velocidad_angular_array = np.full(array_size, velocidad_angular)

posicion_x_array = np.zeros(array_size, float)
posicion_y_array = np.zeros(array_size, float)
angulo_orientacion_array = np.zeros(array_size, float)

velocidad_x_array = np.zeros(array_size, float)  # derivada de la posicion
velocidad_y_array = np.zeros(array_size, float)  # derivada de la posicion

for k in range(array_size):  # metodo de integracion euler-cromer, ref: Elementary mechanics using python
    velocidad_x_array[k] = velocidad_lineal_array[k] * cos(angulo_orientacion_array[k])
    velocidad_y_array[k] = velocidad_lineal_array[k] * sin(angulo_orientacion_array[k])

    if k + 1 != array_size:
        posicion_x_array[k + 1] = posicion_x_array[k] + delta_t * velocidad_x_array[k]
        posicion_y_array[k + 1] = posicion_y_array[k] + delta_t * velocidad_y_array[k]
        angulo_orientacion_array[k + 1] = angulo_orientacion_array[k] + delta_t * radians(
            velocidad_angular_array[k])  # uso radianes, pero no estoy seguro si es así o no

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

scene = canvas(width=800, height=600, center=vector(25, 25, -10),
               background=color.black, align="left")

# grafico
positionGraph = graph(xtitle="time", ytitle="position", align="right")
xPosCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
yPosCoord = gcurve(color=color.red, label="y-coord")  # a graphics curve
anguloCoord = gcurve(color=color.green, label="angulo")

for i in range(array_size):
    xPosCoord.plot(tiempo_array[i], posicion_x_array[i])
    yPosCoord.plot(tiempo_array[i], posicion_y_array[i])
    anguloCoord.plot(tiempo_array[i], angulo_orientacion_array[i])

# grafico
velocityGraph = graph(xtitle="time", ytitle="velocity", align="right")
xVelCoord = gcurve(color=color.cyan, label="x-coord")  # a graphics curve
yVelCoord = gcurve(color=color.red, label="y-coord")  # a graphics curve
velocidad_lineal_coord = gcurve(color=color.blue, label="velocidad-lineal")
velocidad_angular_coord = gcurve(color=color.green, label="velocidad-angular")

for i in range(array_size):
    xVelCoord.plot(tiempo_array[i], velocidad_x_array[i])
    yVelCoord.plot(tiempo_array[i], velocidad_y_array[i])
    velocidad_lineal_coord.plot(tiempo_array[i], velocidad_lineal_array[i])
    velocidad_angular_coord.plot(tiempo_array[i], velocidad_angular_array[i])

#   =================================================================================================


# creacion del espacio de coordenadas
r3 = R3()
r3.draw_r3()

ROBOT_SIZE_X = 4.0
ROBOT_SIZE_Y = 2.0
ROBOT_SIZE_Z = 1.0

# creacion de robot
robot = Robot(initial_position=vector(posicion_x_array[0], posicion_y_array[0], 0),
              size=vector(ROBOT_SIZE_X, ROBOT_SIZE_Y, ROBOT_SIZE_Z), color=color.red)
myRobot = robot.draw_robot()
attach_trail(myRobot)

pointer = arrow(pos=vector(5, 5, 0), axis=VECTOR_UNITARIO_I_TONGO_HORIZONTAL, shaftwidth=0.5)

# creacion de label que contiene a las coordenadas
coordenada = Coordenada(myRobot)
ncoordenada = coordenada.dibujar_coordenada()

#   =================================================================================================

posicion_z_correcta = ROBOT_SIZE_Z / 2
escala_de_la_flecha = 2

if SEGUIR_AL_ROBOT_CON_LA_CAMARA:
    scene.camera.follow(myRobot)

for i in range(array_size - 1):
    rate(30)
    myRobot.pos = vector(posicion_x_array[i], posicion_y_array[i], posicion_z_correcta)
    pointer.pos = myRobot.pos
    pointer.axis = escala_de_la_flecha * vector(velocidad_x_array[i + 1], velocidad_y_array[i + 1], 0.0)
    myRobot.axis = pointer.axis
    coordenada.actualizar_coordenada(ncoordenada, myRobot.pos)
