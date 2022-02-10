import numpy as np
import matplotlib.pylab as plt

def ReLu_func(x):
    # return np.maximun(0, x)
    if x > 0:
        return x
    else :
        return 0

x = np.arange(-5.0, 5.0, 0.1)

y = ReLu_func(x)

plt.plot(x,y)
plt.ylim(-0.1, 1.1) 
plt.show()

