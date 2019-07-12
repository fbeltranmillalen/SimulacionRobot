import math
import matplotlib.pyplot as plt
import numpy as np

pathFile = "D:/Fun things/datosMecanicaPython/fallingtennisball02.d"
time, position = np.loadtxt(pathFile, usecols=[0, 1], unpack=True)
velocity = []
acceleration = []
for i in range(len(position) - 1):
    velocity.append((position[i+1] - position[i]) / (time[1] - time[0]))
velocity.append(velocity[len(velocity) - 1])

for i in range(1, len(position) - 1):
    acceleration.append((velocity[i] - velocity[i-1]) / (time[1] - time[0]))
acceleration.append(acceleration[len(acceleration) - 1])
acceleration.append(acceleration[len(acceleration) - 1])

print(len(time), len(acceleration))



#plt.scatter(time, velocity)
plt.figure()
plt.subplot(131)
plt.scatter(time, position)
plt.subplot(132)
plt.scatter(time, velocity)
plt.subplot(133)
plt.scatter(time, acceleration)
plt.show()
