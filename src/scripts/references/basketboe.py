#Ingeniero Civil Informatico
#Dr.(c) Ciencias de la Ingenieria - PUC
#Laboratorio de MicroControladores
#--------------------------------------

#   from __future__ import division
from vpython import *
import math, random as ra # ctypes as ct, serial as RS

nMAX_ROBOTS = 11

#------------------------------------------------------------------------------
# Retorna el Angulo aleatorio del Robot.-
#------------------------------------------------------------------------------
def Get_Angulo():
    return ra.choice([0,15,30,45,60,75,90,105,120,135,150,65,180,195,
                      210,225,240,255,270,285,300,315,330,345])

#------------------------------------------------------------------------------
# Retorna la Velocidad aleatoria del Robot.-
#------------------------------------------------------------------------------
def Get_Velocidad():
    return ra.choice([0.1,1.0,1.5,2.0,2.5,10.0])

#------------------------------------------------------------------------------
# Seteo Valores de todos los Robots.-
#------------------------------------------------------------------------------
def Robot_Init(nPos):
 aRobots[nPos].nAngu = Get_Angulo() ; aRobots[nPos].nVelo = Get_Velocidad()
 aRobots[nPos].nStep = ra.randint(10,100)
 aRobots[nPos].nPryX=aRobots[nPos].nVelo*sin(math.radians(aRobots[nPos].nAngu))
 aRobots[nPos].nPryZ=aRobots[nPos].nVelo*cos(math.radians(aRobots[nPos].nAngu))
 return

#------------------------------------------------------------------------------
# Chequea Bordes.-
#------------------------------------------------------------------------------
def Check_Out(i):
    if aRobots[i].pos.x <= -870:
       aRobots[i].pos.x =  -870 ; aRobots[i].nStep = 0
    if aRobots[i].pos.x >= +870:
       aRobots[i].pos.x =  +870 ; aRobots[i].nStep = 0
    if aRobots[i].pos.z <= -470:
       aRobots[i].pos.z =  -470 ; aRobots[i].nStep = 0
    if aRobots[i].pos.z >= +470:
       aRobots[i].pos.z =  +470 ; aRobots[i].nStep = 0
    return

#------------------------------------------------------------------------------
# Mueve los Robots.-
#------------------------------------------------------------------------------
def Robot_Move():
    for i in range(nMAX_ROBOTS):
     aRobots[i].nStep -= 1
     if aRobots[i].nStep <= 0: Robot_Init(i)
     aRobots[i].pos.x += aRobots[i].nPryX
     aRobots[i].pos.z += aRobots[i].nPryZ
     Check_Out(i)
    return

#------------------------------------------------------------------------------
# Mueve los Robots.-
#------------------------------------------------------------------------------
def Robot_Rota():
 #aRobots[9].rotate(angle = radians(0.5),axis=(0,1,0))
 #aRobots[10].rotate(angle = -1*radians(2),axis=(0,1,0),origin=(50,0,0))
 aRobots[9].rotate(angle = radians(5),axis=vector(0,1,0))
 #aRobots[10].rotate(angle=-1*radians(1.0),axis=(0,1,0),origin=(aRobots[9].pos))
 aRobots[10].rotate(angle = -1*radians(1.0),axis=vector(0,1,0))

#------------------------------------------------------------------------------
# Definicion del Mundo 3D y sus Objetos.-
#------------------------------------------------------------------------------
Scene = canvas(title='Demo',x=50,y=0,width=1900,height=600,center=vector(0,0,0),background=vector(0,0,0))
Base  = box(pos=vector(0,0,0),size=vector(1800,3,1000),color=color.red)
Mapa  = box(pos=vector(0,2,0),size=vector(1780,5,980),color=color.gray(0.3))

#Guia  = box(pos=(0,4,0),size=(1800,10,10),color=color.blue,opacity=0.09)
Cara1 = box(pos=vector(0,0,+500),size=vector(1800,20,10),color=color.blue)
Cara2 = box(pos=vector(0,0,-500),size=vector(1800,20,10),color=color.blue)
Cara3 = box(pos=vector(+900,0,0),size=vector(10,20,1000),color=color.blue)
Cara4 = box(pos=vector(-900,0,0),size=vector(10,20,1000),color=color.blue)
#------------------------------------------------------------------------------
# Definicion de los Robots-
#------------------------------------------------------------------------------
Rob_1 = cylinder(pos=vector(000,1,0),radius=15,color=color.blue,axis=vector(0,15,0),opacity=1)
Rob_2 = cylinder(pos=vector(100,1,0),radius=15,color=color.blue,axis=vector(0,15,0),opacity=1)
Rob_3 = cylinder(pos=vector(0,1,100),radius=15,color=color.blue,axis=vector(0,15,0),opacity=1)

Rob_4 = cylinder(pos=vector(000,1,0),radius=15,color=color.red,axis=vector(0,15,0),opacity=1)
Rob_5 = cylinder(pos=vector(100,1,0),radius=15,color=color.red,axis=vector(0,15,0),opacity=1)
Rob_6 = cylinder(pos=vector(0,1,100),radius=15,color=color.red,axis=vector(0,15,0),opacity=1)

Rob_7 = cylinder(pos=vector(000,1,0),radius=15,color=color.yellow,axis=vector(0,15,0),opacity=1)
Rob_8 = cylinder(pos=vector(100,1,0),radius=15,color=color.yellow,axis=vector(0,15,0),opacity=1)
Rob_9 = cylinder(pos=vector(0,1,100),radius=15,color=color.yellow,axis=vector(0,15,0),opacity=1)

#MyBoe1 = frame()
Rob_x = cylinder(pos=vector(0,1,0),radius=20,color=color.blue,axis=vector(0,80,0))
MyBox = box(pos=vector(0,40,0),size=vector(15,15,15),color=color.red)
Ante  = box(pos=vector(0,70,0),size=vector(2,50,2),color=color.white)
Brazo = box(pos=vector(0,40,0),size=vector(70,10,4),color=color.white)
MyBoe1 = compound([Rob_x, MyBox, Ante, Brazo])

#MyBoe2 = frame(pos=(-450,0,0))
Rob_x = cylinder(pos=vector(0,1,0),radius=20,color=color.red,axis=vector(0,80,0))
MyBox = box(pos=vector(0,40,0),size=vector(15,15,15),color=color.blue)
Ante  = box(pos=vector(0,70,0),size=vector(2,50,2),color=color.white)
Brazo = box(pos=vector(0,40,0),size=vector(70,10,4),color=color.white)
MyBoe2 = compound([Rob_x, MyBox, Ante, Brazo])
MyBoe2.pos = vector(-450,0,0)

#------------------------------------------------------------------------------
# Logica principal.-
#------------------------------------------------------------------------------
#s = RS.Serial(1) ; s.baudrate = 9600 ; s.timeout = 0.01
aRobots = [Rob_1,Rob_2,Rob_3,Rob_4,Rob_5,Rob_6,Rob_7,Rob_8,Rob_9,MyBoe1,MyBoe2]
aClrBoe = [color.red,color.green,color.cyan]
for i in range(nMAX_ROBOTS):
 Robot_Init(i)

Data = 'FLIP'
while 1:
 #Data = s.readline()[:-1] # Leemos data serial y quitamos ENTER(New Line)
 print(Data) # Data a Pantalla...
 if Data == 'CHGCOLOR': Rob_2.color = ra.choice(aClrBoe) # Chage Color Boe.-
 if Data == 'FLIP':
    MyBox.visible = False
    Data = 'FLOP'
 if Data == 'FLOP':
    MyBox.visible = True
    Data = 'FLIP'
 Robot_Move() # Movemos.....
 Robot_Rota()
 rate(100)
s.close()

