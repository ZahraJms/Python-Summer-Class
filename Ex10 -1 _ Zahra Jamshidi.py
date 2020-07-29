import numpy as np
import matplotlib.pyplot as plt
x=10
print(pow(x,2)," - ",pow(x,3))
theta=np.pi
print("Sin : " ,np.sin(theta)," Cos : ",np.cos(theta)) #Radians
meshpoints=np.linspace(-1,1,500)
print(meshpoints[52]) #-0.7915831663326653
plt.plot(meshpoints,np.sin(2*np.pi*meshpoints))
plt.show()