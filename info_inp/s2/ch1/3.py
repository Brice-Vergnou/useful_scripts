import matplotlib.pyplot as plt

x_g = [-1,-1]
y_g = [-2,2]
plt.plot(x_g, y_g,'b')

x_m = [-1,1]
y_m = [0,0]
plt.plot(x_m, y_m,'b')

x_d = [1,1]
y_d = [-2,2]
plt.plot(x_d, y_d, 'b')

plt.axis([-2,2,-3,3])
plt.show()