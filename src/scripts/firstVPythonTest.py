from vpython import *
from src.scripts.R3 import R3
from src.scripts.Robot import Robot
from src.scripts.Coordenada import Coordenada

# TODO
# guardar todos los valores de posicion, velocidad y aceleracion en arreglos para poder hacer calculos con ellos
# mejorar la escena
# crear una flecha que describa la direccion del robot en tiempo real
# cambiar el orden de simulacion por obtencion de datos primero, despues graficar y despues renderizar
# mejorar el aspecto del robot

# agregar un label con el metodo numerico o analítico usado en la simulación


# Hacer un mejor plano R3, con tiles transparentes y cordenadas discretas
# iterar sobre estos pasos para ir mejorando la simulación

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
