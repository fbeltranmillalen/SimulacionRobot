import math
import matplotlib.pyplot as plt
# import numpy

n = math.ceil(((10.0 - 0.0) / 0.1) + 1)
print(n)
arrayX = []
arrayY = []

for i in range(n):
    arrayX.append(i*0.1)
    arrayY.append(math.sin(arrayX[i]))
print(arrayX, arrayY)
plt.scatter(arrayX, arrayY)
plt.show()
