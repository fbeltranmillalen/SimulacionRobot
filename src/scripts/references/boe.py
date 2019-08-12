# By Alberto Caro
# Ingeniero Civil Informatico
# Dr.(c) Ciencias de la Ingenieria - PUC
# Laboratorio de MicroControladores
# --------------------------------------

#from __future__ import division
from vpython import *
import math
import random as ra  # ctypes as ct, serial as RS

nMAX_ROBOTS = 5


# -------------------------------------------------------------------------------------------------
# Retorna el Angulo aleatorio del Robot.-
# -------------------------------------------------------------------------------------------------
def Get_Angulo():
    return ra.choice(
        [0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330,
         345])


# -------------------------------------------------------------------------------------------------
# Retorna la Velocidad aleatoria del Robot.-
# -------------------------------------------------------------------------------------------------
def Get_Velocidad():
    return ra.choice([0.1, 1.0, 1.5, 2.0, 2.5, 3.0])


# -------------------------------------------------------------------------------------------------
# Seteo Valores de todos los Robots.-
# -------------------------------------------------------------------------------------------------
def Robot_Init(nPos):
    aRobots[nPos].nAngu = Get_Angulo()
    aRobots[nPos].nVelo = Get_Velocidad()
    aRobots[nPos].nStep = ra.randint(10, 100)
    aRobots[nPos].nPryX = aRobots[nPos].nVelo * sin(math.radians(aRobots[nPos].nAngu))  # cos(.)...
    aRobots[nPos].nPryZ = aRobots[nPos].nVelo * cos(math.radians(aRobots[nPos].nAngu))  # sin(.)...
    return


# -------------------------------------------------------------------------------------------------
# Chequea Bordes.-
# -------------------------------------------------------------------------------------------------
def Check_Out(i):
    if aRobots[i].pos.x <= -870:  # Borde Izquierdo
        aRobots[i].pos.x = -870;
        aRobots[i].nStep = 0
    if aRobots[i].pos.x >= +870:  # Borde Derecho Eje-X
        aRobots[i].pos.x = +870;
        aRobots[i].nStep = 0
    if aRobots[i].pos.z <= -470:  # Borde Inferior Eje-Z
        aRobots[i].pos.z = -470;
        aRobots[i].nStep = 0
    if aRobots[i].pos.z >= +470:  # Borde Superior Eje-Z
        aRobots[i].pos.z = +470;
        aRobots[i].nStep = 0
    return


# -------------------------------------------------------------------------------------------------
# Mueve los Robots.-
# -------------------------------------------------------------------------------------------------
def Robot_Move():
    for i in range(nMAX_ROBOTS):
        aRobots[i].nStep -= 1
        if aRobots[i].nStep <= 0: Robot_Init(i)
        aRobots[i].pos.x += aRobots[i].nPryX;
        aRobots[i].pos.z += aRobots[i].nPryZ
        Check_Out(i)
    return


# -------------------------------------------------------------------------------------------------
# Calcula distancia Euclidiana de los Robots a ambos Aros
# -------------------------------------------------------------------------------------------------
def Robot_Dist():
    aDEaD = [0.0, 0.0, 0.0, 0.0, 0.0];
    aDEaI = [0.0, 0.0, 0.0, 0.0, 0.0]
    for i in range(nMAX_ROBOTS):
        aDEaD[i] = math.sqrt((MyViD.pos.x - aRobots[i].pos.x) ** 2 + (MyViD.pos.z - aRobots[i].pos.z) ** 2)
        aDEaI[i] = math.sqrt((MyViI.pos.x - aRobots[i].pos.x) ** 2 + (MyViI.pos.z - aRobots[i].pos.z) ** 2)
    return aDEaD, aDEaI


# -------------------------------------------------------------------------------------------------
# Definicion del Mundo 3D y sus Objetos.-
# -------------------------------------------------------------------------------------------------
Scene = canvas(title='Demo', x=50, y=0, width=1900, height=600, center=(0, 0, 0), background=(0, 0, 0))
MyMap = box(pos=(0, 0, 0), size=(1800, 3, 1000), color=color.red)
MyBas = box(pos=(0, 2, 0), size=(1780, 5, 980), color=color.gray(0.5))
MyViD = box(pos=(900, 20, 0), size=(3, 40, 6), color=color.green)
MyViI = box(pos=(-900, 20, 0), size=(3, 40, 6), color=color.green)

Rob_1 = cylinder(pos=(000, 7, 0), radius=15, color=color.blue, axis=(0, 15, 0))
Rob_2 = cylinder(pos=(100, 1, 0), radius=15, color=color.green, axis=(0, 15, 0), opacity=1)
Rob_3 = cylinder(pos=(0, 1, 100), radius=15, color=color.yellow, axis=(0, 15, 0), opacity=1)
Rob_4 = cylinder(pos=(200, 1, 0), radius=15, color=color.cyan, axis=(0, 15, 0), opacity=1)
Rob_5 = cylinder(pos=(0, 1, 300), radius=15, color=color.red, axis=(0, 15, 0), opacity=1)


# -------------------------------------------------------------------------------------------------
# Mis Funciones...
# -------------------------------------------------------------------------------------------------
def MyFuny():
    # .. Bla, Bla
    # .. Bla, Bla
    return


# -------------------------------------------------------------------------------------------------
# Logica principal.-
# -------------------------------------------------------------------------------------------------

# MyCom = RS.Serial(1) ; MyCom.timeout = 0.01
aRobots = [Rob_1, Rob_2, Rob_3, Rob_4, Rob_5]
for i in range(nMAX_ROBOTS):
    Robot_Init(i)
while 1:
    # aData = MyCom.readline()
    # ..
    MyFuny()
    # ..
    # ..
    Robot_Move()
    DD, DI = Robot_Dist()
    rate(100)
