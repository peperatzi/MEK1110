import numpy as np
import matplotlib.pyplot as plt

NY = 50
ymin = -2.
ymax = 2.
dy = (ymax -ymin )/(NY-1.)

NX = NY
xmin = -2.
xmax = 2.
dx = (xmax -xmin)/(NX-1.)

def divergence(f):
    num_dims = len(f)
    return np.ufunc.reduce(np.add, [np.gradient(f[i], axis=i) for i in range(num_dims)])

y = np.array([ ymin + float(i)*dy for i in range(NY)])
x = np.array([ xmin + float(i)*dx for i in range(NX)])

x, y = np.meshgrid( x, y, indexing = 'ij', sparse = False)

Fx  = np.cos(x + 2*y)
Fy  = np.sin(x - 2*y)

F = [Fx, Fy]
g = divergence(F)

plt.pcolormesh(x, y, g)
plt.colorbar()
plt.savefig( 'Div' + str(NY) +'.png', format = 'png')
plt.show()
