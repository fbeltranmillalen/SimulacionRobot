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
PI = math.pi

t_inicial = 0  # seg
t_final = 40  # seg
delta_t = 0.01  # seg
posicion_x_inicial = 0.0
posicion_y_inicial = 0.0
posicion_x_deseada = -6.0
posicion_y_deseada = 7.0
angulo_orientacion_inicial = PI / 4
velocidad_lineal = 0.0  # m/s
velocidad_angular = 1.5  # m/s
desplazamiento_centro_masa = 0.1
ganancia = 0.1
array_size = int(math.ceil(((t_final - t_inicial) / delta_t) + 1))  # tamaño de todos los arreglos de la simulacion
tiempo_array = np.zeros(array_size, float)  # arreglo de tiempo para la grafica

for i in range(array_size - 1):
    tiempo_array[i + 1] = tiempo_array[i] + delta_t  # llenar el arreglo tiempo

# arreglo de tamaño array_size, lleno con el valor de la variable velocidad lineal
# describe la velocidad lineal en el tiempo de la simulacion
velocidad_lineal_array = np.full(array_size, velocidad_lineal)

# arreglo de tamaño array_size, lleno con el valor de la variable velocidad angular
# describe la velocidad angular en el tiempo de la simulacion
velocidad_angular_array = np.full(array_size, velocidad_angular)

# set de arreglos de tamaño array_size, llenos con el valor 0.0
# describen la posicion (x,y) del vector y su orientacion en un momento t de la simulacion
# el vector está asociado al centro de masa del robot cuando se encuentra en el centro del robot
posicion_x_array = np.full(array_size, posicion_x_inicial)
posicion_y_array = np.full(array_size, posicion_y_inicial)
angulo_orientacion_array = np.full(array_size, angulo_orientacion_inicial)

# set de arreglos de tamaño array_size, llenos con el valor 0.0
# describen la posicion (x,y) del vector y su orientacion en un momento t de la simulacion
# el vector está asociado al centro de masa del robot cuando no está en el eje de las ruedas
posicion_x_centro_de_masa_desplazado_array = np.zeros(array_size, float)
posicion_y_centro_de_masa_desplazado_array = np.zeros(array_size, float)

for i in range(array_size):
    posicion_x_centro_de_masa_desplazado_array[i] = posicion_x_array[i] + desplazamiento_centro_masa * cos(
        angulo_orientacion_array[i])
    posicion_y_centro_de_masa_desplazado_array[i] = posicion_y_array[i] + desplazamiento_centro_masa * sin(
        angulo_orientacion_array[i])

velocidad_x_array = np.zeros(array_size, float)  # derivada de la posicion
velocidad_y_array = np.zeros(array_size, float)  # derivada de la posicion
errores_x = np.zeros(array_size, float)
errores_y = np.zeros(array_size, float)

for k in range(array_size):

    errores_x[k] = posicion_x_deseada - posicion_x_array[k]
    errores_y[k] = posicion_y_deseada - posicion_y_array[k]
    errores_matriz = np.array((errores_x[k], errores_y[k]))

    print("errores_matriz")
    print(errores_matriz)
    jacobiana_matriz = np.array(([cos(angulo_orientacion_array[k]), -desplazamiento_centro_masa * sin(angulo_orientacion_array[k])], [sin(angulo_orientacion_array[k]), desplazamiento_centro_masa * cos(angulo_orientacion_array[k])]))

    print("jacobiana_matriz")
    print(jacobiana_matriz)

    ganancia_matriz = np.array(([ganancia, 0],
                                [0, ganancia]))

    print("ganancia_matriz")
    print(ganancia_matriz)

    ganancia_por_error = np.matmul(ganancia_matriz, errores_matriz)
    print("ganancia_por_error")
    print(ganancia_por_error)

    inversa_jacobiana = np.linalg.inv(jacobiana_matriz)
    print("inversa_jacobiana")
    print(inversa_jacobiana)

    ley_de_control = np.matmul(inversa_jacobiana, ganancia_por_error)
    print("ley_de_control")
    print(ley_de_control)
    velocidad_lineal_array[k] = ley_de_control[0]
    velocidad_angular_array[k] = ley_de_control[1]

    velocidad_x_array[k] = velocidad_lineal_array[k] * cos(angulo_orientacion_array[k]) - desplazamiento_centro_masa * \
                           velocidad_angular_array[k] * sin(angulo_orientacion_array[k])
    velocidad_y_array[k] = velocidad_lineal_array[k] * sin(angulo_orientacion_array[k]) + desplazamiento_centro_masa * \
                           velocidad_angular_array[k] * cos(angulo_orientacion_array[k])

    if k + 1 != array_size:  # metodo de integracion euler-cromer, ref: Elementary mechanics using python
        posicion_x_centro_de_masa_desplazado_array[k + 1] = posicion_x_centro_de_masa_desplazado_array[k] + delta_t * \
                                                            velocidad_x_array[k]
        posicion_y_centro_de_masa_desplazado_array[k + 1] = posicion_y_centro_de_masa_desplazado_array[k] + delta_t * \
                                                            velocidad_y_array[k]
        angulo_orientacion_array[k + 1] = angulo_orientacion_array[k] + delta_t * velocidad_angular_array[
            k]
        posicion_x_array[k + 1] = posicion_x_centro_de_masa_desplazado_array[k + 1] - desplazamiento_centro_masa * cos(
            angulo_orientacion_array[k + 1])
        posicion_y_array[k + 1] = posicion_y_centro_de_masa_desplazado_array[k + 1] - desplazamiento_centro_masa * sin(
            angulo_orientacion_array[k + 1])

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
myRobot.opacity = 0.5

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
