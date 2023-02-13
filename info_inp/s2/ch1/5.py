import matplotlib.pyplot as plt
import numpy as np

x_r = np.linspace(0,4,500)
x_c = np.linspace(0,2,500)
x_s = np.linspace(0,3,500)

y_r = np.sqrt(x_r)
y_c = np.square(x_c) # ou np.power(x_c, 2)
y_s = x_s #inutile mais "elegant"


plt.plot(x_r,y_r,"r")
plt.plot(x_c,y_c,"b")
plt.plot(x_s,y_s,"black")
plt.plot([0,1],[0,1],"o", color="black")

plt.axhline(color="black")
plt.axvline(color="black")

plt.show()