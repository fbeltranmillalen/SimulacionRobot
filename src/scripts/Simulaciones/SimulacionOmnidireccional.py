from vpython import *

from src.scripts.Clases.R3 import R3
from src.scripts.Clases.Robot import Robot
from src.scripts.Clases.Coordenada import Coordenada
from src.scripts.Clases.RobotOmnidireccional import RobotOmnidireccional

import math
import numpy as np
import random as ra

VECTOR_UNITARIO_I_TONGO_HORIZONTAL = vector(1, 0, 0)
VECTOR_UNITARIO_J_TONGO_VERTICAL = vector(0, 1, 0)
VECTOR_UNITARIO_Z_TONGO_PROFUNDIDAD = vector(0, 0, 1)
ORIGEN = vector(0, 0, 0)
SEGUIR_AL_ROBOT_CON_LA_CAMARA = False

def get_angulo_random():
    return ra.choice(
        [0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0, 105.0, 120.0, 135.0, 150.0, 165.0, 180.0, 195.0, 210.0, 225.0, 240.0,
         255.0, 270.0, 285.0, 300.0, 315.0, 330.0,
         345.0])
def get_velocidad_lineal_random():
    return ra.uniform(5.0, 15.0)
def get_velocidad_angular_random():
    return ra.choice(
        [1.0, 5.0, 10.0, 15.0, 25.0, 30.0, 40.0, 50.0, 100.0, -1.0, -5.0, -10.0, -15.0, -25.0, -30.0, -40.0, -50.0,
         -100.0])
def get_posicion_inicial_random():
    return vector(ra.uniform(-30.0, 30.0), ra.uniform(-30.0, 30.0), 1.0)

#def inicializar_variables():


#Inicializacion de variables
n_robots = 1
t_inicial = 0  # seg
t_final = 20  # seg
delta_t = 0.01  # seg

array_size = int(math.ceil(((t_final - t_inicial) / delta_t) + 1))
tiempo_array = np.zeros(array_size, float)
scene = canvas(width=1366, height=768, center=vector(25, 25, -10),
               background=color.black, align="left")


#=======================================================================
# esto va en un otro ciclo que lo separa para hacerlo con varios robots
for i in range(array_size - 1):
    tiempo_array[i + 1] = tiempo_array[i] + delta_t



lista_robots = []



# creacion del espacio de coordenadas
r3 = R3()
r3.draw_r3()

ROBOT_SIZE_X = 4.0
ROBOT_SIZE_Y = 2.0
ROBOT_SIZE_Z = 1.0

# instanciar varios

for contador in range(n_robots):
    velocidad_lineal_frontal = 1.0  #get_velocidad_lineal_random()  # m/s
    velocidad_lineal_lateral = -1.0  #get_velocidad_lineal_random()
    velocidad_angular = 0.0 #get_velocidad_angular_random()  # m/s
    angulo_orientación_inicial = 0.0  #get_angulo_random()
    posicion_inicial = vector(0,0,0)    #get_posicion_inicial_random()

    velocidad_lineal_frontal_array = np.full(array_size, velocidad_lineal_frontal)
    velocidad_lineal_lateral_array = np.full(array_size, velocidad_lineal_lateral)
    velocidad_angular_array = np.full(array_size, velocidad_angular)
    angulo_orientacion_array = np.full(array_size, angulo_orientación_inicial)

    posicion_x_array = np.full(array_size, posicion_inicial.x)
    posicion_y_array = np.full(array_size, posicion_inicial.y)
    posicion_z_array = np.full(array_size, posicion_inicial.z)

    velocidad_x_array = np.zeros(array_size, float)  # derivada de la posicion
    velocidad_y_array = np.zeros(array_size, float)  # derivada de la posicion
    velocidad_z_array = np.zeros(array_size, float)




    for k in range(array_size):  # metodo de integracion euler-cromer, ref: Elementary mechanics using python
        velocidad_x_array[k] = velocidad_lineal_frontal_array[k] * cos(radians(angulo_orientacion_array[k])) - velocidad_lineal_lateral_array[k] * sin(radians(angulo_orientacion_array[k]))
        velocidad_y_array[k] = velocidad_lineal_frontal_array[k] * sin(radians(angulo_orientacion_array[k])) + velocidad_lineal_lateral_array[k] * cos(radians(angulo_orientacion_array[k]))

        if k + 1 != array_size:
            posicion_x_array[k + 1] = posicion_x_array[k] + delta_t * velocidad_x_array[k]
            posicion_y_array[k + 1] = posicion_y_array[k] + delta_t * velocidad_y_array[k]
            angulo_orientacion_array[k + 1] = angulo_orientacion_array[k] + delta_t * velocidad_angular_array[k]  # uso radianes, pero no estoy seguro si es así o no

    '''
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
    '''

    robot = Robot(initial_position=vector(posicion_x_array[0], posicion_y_array[0], 0),
                  size=vector(ROBOT_SIZE_X, ROBOT_SIZE_Y, ROBOT_SIZE_Z), color=color.red, robot_type=0)
    myRobot = robot.draw_robot()
    attach_trail(myRobot)
    flecha = arrow(pos=myRobot.pos, axis=VECTOR_UNITARIO_I_TONGO_HORIZONTAL, shaftwidth=0.5)
    # creacion de label que contiene a las coordenadas
    coordenada = Coordenada(myRobot)
    label_coordenada = coordenada.dibujar_coordenada()

    robotec = RobotOmnidireccional(myRobot, posicion_x_array, posicion_y_array, posicion_z_array, velocidad_x_array, velocidad_y_array, velocidad_z_array, velocidad_lineal_frontal_array, velocidad_lineal_lateral_array, velocidad_angular_array, angulo_orientacion_array, flecha, label_coordenada)

    lista_robots.append(robotec)

print(lista_robots)
#   =================================================================================================
#   ================================
'''


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


'''


#   =================================================================================================

escala_de_la_flecha = 2

if SEGUIR_AL_ROBOT_CON_LA_CAMARA:
    scene.camera.follow(myRobot)

for i in range(array_size - 1):
    rate(60)
    for robot in lista_robots:
        robot.vPythonRobot.pos = vector(robot.posicion_x_array[i], robot.posicion_y_array[i], robot.posicion_z_array[i])
        robot.flecha.pos = robot.vPythonRobot.pos
        robot.flecha.axis = escala_de_la_flecha * vector(robot.velocidad_x_array[i + 1], robot.velocidad_y_array[i + 1], robot.velocidad_z_array[i +1])
        robot.vPythonRobot.axis = vector(robot.angulo_orientacion_array[i], 0, 0)
        rotate(robot.vPythonRobot, angle=robot.angulo_orientacion_array[i + 1] - robot.angulo_orientacion_array[i], axis=vector(0, 0, 1))
        coordenada.actualizar_coordenada(robot.label_coordenada, robot.vPythonRobot.pos)

