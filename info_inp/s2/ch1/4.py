import matplotlib.pyplot as plt

for i in range(4):
    x = [-4+2*i,-4+2*i]
    y= [0,1]
    plt.plot(x,y,"b")
    
    x =[-4+2*i,-3+2*i]
    y = [1,1]
    plt.plot(x,y,"b")
    
    x=[-3+2*i,-3+2*i]
    y= [1,0]
    plt.plot(x,y,"b")
    
    x= [-3+2*i,-2+2*i]
    y = [0,0]
    plt.plot(x,y,"b")

plt.show()