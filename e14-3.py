import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
y1=(np.sin(np.pi*x))*(np.e**(-x/10))
y2=(np.e**(-x/10))*x
fig,axes=plt.subplots(nrows=2 ,ncols=2)
axes[0,0].plot(x,y1)
axes[1,0].plot(x,y2)
plt.show()

#
import numpy as np
import matplotlib.pyplot as plt
r0=1
t = np.linspace(0,2* np.pi, 100)
r=r0+np.cos(t)
x=r*np.sin(t)
y=r*np.cos(t)
plt.plot(x,y)

r0=0.8
t = np.linspace(0,2* np.pi, 100)
r=r0+np.cos(t)
x=r*np.sin(t)
y=r*np.cos(t)
plt.plot(x,y)


r0=1.2
t = np.linspace(0,2* np.pi, 100)
r=r0+np.cos(t)
x=r*np.sin(t)
y=r*np.cos(t)
plt.plot(x,y)


plt.show()
