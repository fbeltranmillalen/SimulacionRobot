#By Alberto Caro
#Ingeniero Civil Informatico
#Dr.(c) Ciencias de la Ingenieria - PUC
#--------------------------------------
#from __future__ import division
from vpython import *
import math, time as ti, random as ra

nANG_1 = -1.0 ; nANG_2 = +1.0 ;nMAX_BOE = 5

#------------------------------------------------------------------------------
# Definicion del Mundo 3D y sus Objetos.-
#------------------------------------------------------------------------------
WinM  = canvas(title='Demo',x=50,y=0,width=1900,height=600,center=(0,0,0))
Base1 = box(pos=(0,0,0),size=(1300,3,1000),color=color.gray(0.5))
#Base2 = box(pos=(0,150,0),size=(1300,300,1000),color=color.blue,opacity = 0.5)

#------------------------------------------------------------------------------
# Definicion de Objeto Brazo
#------------------------------------------------------------------------------
def Get_Arm(oFrm,tFXYZ,tXYZ,tWHD,nClr,nAng):
    oFrame     = frame(frame=oFrm,pos=tFXYZ)
    oFrame.oB0 = box(frame=oFrame,pos=tXYZ,size=tWHD,color=nClr)
    oFrame.oR0 = nAng
    return oFrame

#------------------------------------------------------------------------------
# Definicion de Objeto Robot
#------------------------------------------------------------------------------
def Get_Boe(tFXYZ,nClr1,nClr2):
    oFrame     = frame(pos=tFXYZ)
    oFrame.oC0 = cylinder(frame=oFrame,pos=(0,1,0),radius=20,axis=(0,40,0),color=nClr1)
    oFrame.oB1 = box(frame=oFrame,pos=(0,40,0),size=(15,15,15),color=color.blue)
    oFrame.oB2 = box(frame=oFrame,pos=(0,70,0),size=(2,50,2),color=color.white)
    oFrame.oB3 = box(frame=oFrame,pos=(20,40,0),size=(48,10,4),color=color.white)
    oFrame.oB4 = box(frame=oFrame,pos=(40,130,0),size=(10,200,200),color=nClr2,opacity = 1)
    return oFrame

#------------------------------------------------------------------------------
# Rotacion de los Robots.-
#------------------------------------------------------------------------------
def Robot_Rotate():
    aBoe[0].rotate(angle=radians(-1.2),axis=(0,1,0))
    aBoe[1].rotate(angle=radians(+2.1),axis=(0,1,0))
    aBoe[2].rotate(angle=radians(+1.4),axis=(0,1,0))
    aBoe[3].rotate(angle=radians(-2.2),axis=(0,1,0))
    aBoe[4].rotate(angle=radians(-1.3),axis=(0,1,0))
    return

#------------------------------------------------------------------------------
# Rotacion de los Robots.-
#------------------------------------------------------------------------------
def Arm_Rotate():
    for i in range(nMAX_BOE):
     aArm[i].rotate(angle=radians(aArm[i].oR0),axis=(1,0,0),origin=(0,130,0))
    return

#------------------------------------------------------------------------------
# Logica principal.-
#------------------------------------------------------------------------------

aBoe = [
         Get_Boe((-550,0,0),color.red,color.yellow),Get_Boe((-300,0,0),color.green,color.blue),\
         Get_Boe((-50,0,0),color.yellow,color.red),Get_Boe((+250,0,0),color.blue,color.cyan),\
         Get_Boe((+550,0,0),color.cyan,color.white)
       ]

aArm = [
         Get_Arm(aBoe[0],(53,0,00),(0,130,0),(8,8,200),color.red,+1.5),
         Get_Arm(aBoe[1],(53,0,-20),(0,130,0),(8,8,100),color.yellow,-1.7),
         Get_Arm(aBoe[2],(53,0,40),(0,130,0),(8,8,100),color.white,+0.5),
         Get_Arm(aBoe[3],(53,0,40),(0,130,0),(8,8,100),color.blue,-1.0),
         Get_Arm(aBoe[4],(53,0,40),(0,130,0),(8,8,100),color.green,+1.3)
       ]
c = 0
while 1:
 if WinM.kb.keys:
    k = WinM.kb.getkey()
    print(k)
 c += 1
 rate(100)
 Robot_Rotate()
 Arm_Rotate()
 if c > 500:
    c = 0
   # aArm[0].oB0.color = color.yellow
 print(aBoe[0].pos)

