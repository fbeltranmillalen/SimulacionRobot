import numpy as np
import matplotlib.pyplot as plt

D = 0.0245  # la dimesion de la pelota de tenis en m^-1
g = 9.8  # m/s^2 gravedad
posicionInicial = 2.0  # metros
velocidadInicial = 0.0   # m/s
time = 0.7  # seg
dt = 0.00001    # seg

#   Variables de la simulación
n = np.ceil(time/dt)
n = int(n)
posicionArray = np.zeros(n, float)
velocidadArray = np.zeros(n, float)
aceleracionArray = np.zeros(n, float)
tiempoArray = np.zeros(n, float)

#Inicialización de la variables importantes

posicionArray[0] = posicionInicial
velocidadArray[0] = velocidadInicial

#Ciclo de integración Euler-Cromer
flag = True

for i in range(n-1):
    aceleracionArray[i] = -g-D*velocidadArray[i]*abs(velocidadArray[i])
    velocidadArray[i+1] = velocidadArray[i] + aceleracionArray[i]*dt
    posicionArray[i+1] = posicionArray[i] + velocidadArray[i+1]*dt
    if(posicionArray[i+1] < 0 and flag):
        print(tiempoArray[i])
        flag = False
    tiempoArray[i+1] = tiempoArray[i] + dt

aceleracionArray[n-1] = aceleracionArray[n-2]
print(aceleracionArray)

#plt.scatter(time, velocity)
plt.figure()
plt.subplot(311)
plt.scatter(tiempoArray, posicionArray)
plt.subplot(312)
plt.scatter(tiempoArray, velocidadArray)
plt.subplot(313)
plt.scatter(tiempoArray, aceleracionArray)
plt.show()



