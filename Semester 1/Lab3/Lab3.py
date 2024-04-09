from scipy.optimize import linprog
import matplotlib.pyplot as plt
import numpy as np


a = np.array([[-1, -1], [1, -2], [-3, 2], [-1, 0],[1, 0], [0, -1],[0, 1],[-1,-1],[-1,3]])
b = np.array([-28, 14, 28, 0, 56, 0, 42, -70, 84])
c = np.array([3, -1])
res = linprog(c, A_ub=a, b_ub=b)

print('Значения по x1 x2:', res.x,
      '\nОптимальное значение f2:', round(res.fun*-1, ndigits=2),
      '\nОптимальное значение f1:', round(res.x[0]+res.x[1], ndigits=2),
      '\nОптимальное значение f3:', round(res.x[0]-3 * res.x[1], ndigits=2))

fig = plt.figure()
grid1 = plt.grid(True)
graph1 = plt.plot([56, 56], [42, 21])
graph2 = plt.plot([51.3, 56], [18.7, 21])
graph3 = plt.plot([32.25, 51.3], [37.75, 18.7])
graph4 = plt.plot([32.25, 45], [37.75, 42])
graph5 = plt.plot([45, 56], [42, 42])
plt.suptitle('График представления D~')
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig('Grafic')
plt.show()
