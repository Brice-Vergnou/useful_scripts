import matplotlib.pyplot as plt
import numpy as np

n=7
plot_x = [0.1]
plot_y= [0.1]
x = np.linspace(0,1,500)
plt.plot(x,x)
f = np.cos
y = f(x)
plt.plot(x,y,"b")

for _ in range(n):
    plot_x.append(plot_x[-1])
    plot_y.append(f(plot_x[-1]))
    
    plt.plot([plot_x[-1],plot_x[-1]],
            [0,plot_y[-1]],
             "--k",color="red")
    
    plot_x.append(plot_y[-1])
    plot_y.append(plot_y[-1])
    
plt.plot([plot_x[-1],plot_x[-1]],
            [0,plot_y[-1]],
             "--k",color="red")

plt.axhline(color='black')
plt.axvline(color='black')
plt.plot(plot_x,plot_y,"red")
plt.plot(plot_x,[0]*len(plot_x),"rs")

plt.show()

################################################################

n=7
plot_x = [0.1]
plot_y= [0.1]
x = np.linspace(0,1,500)
plt.plot(x,x)
f = lambda t:np.sqrt((t+1)/2)
y = f(x)
plt.plot(x,y,"b")

for _ in range(n):
    plot_x.append(plot_x[-1])
    plot_y.append(f(plot_x[-1]))
    
    plt.plot([plot_x[-1],plot_x[-1]],
            [0,plot_y[-1]],
             "--k",color="red")
    
    plot_x.append(plot_y[-1])
    plot_y.append(plot_y[-1])
    
    
plt.axhline(color='black')
plt.axvline(color='black')
plt.plot(plot_x,plot_y,"red")
plt.plot(plot_x,[0]*len(plot_x),"rs")

plt.show()