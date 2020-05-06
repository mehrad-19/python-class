import numpy as np
import matplotlib.pyplot as plt
x=np.array([3,])
print(np.square(x))
y=int(input('theta:'))
'''y bar hasbe radian'''
print(np.sin(y))
print(np.cos(y))
meshPoint=np.linspace(-1,1,500)
print(meshPoint)
#
x=np.linspace(-1,1,500)
plt.plot(meshPoint,np.sin(2*np.pi*meshPoint))
plt.show()

