import numpy as np

from scipy.optimize import linprog

qf1=3
qf2=2

A = np.array([[1, 2], [-2, -1],[-1, 0],[1, 0], [0, -1], [0, 1]])
b = np.array([56, -14, 0, 28, 0, 21])
c = np.array([3, -1])
res = linprog(c, A_ub=A, b_ub=b)
print('Первая максимизация по f2:', res.fun*-1, '\n f2-qf2=', res.fun*-1-qf2)

f1 = round(res.fun*-1-qf2,3)
A1 = np.array([[1, 2], [-2, -1], [-1, 0], [1, 0], [0, -1], [0, 1], [3, -1]])
b1 = np.array([56, -14, 0, 28, 0, 21, -f1])
c1 = np.array([-1, -1])
res1 = linprog(c1, A_ub=A1, b_ub=b1)
print('Вторая максимизация по f1:', round(res1.fun*-1, 3), '\n f1-qf1=', round(res1.fun*-1-qf1, 3))

f2=round(res1.fun*-1-qf1,3)
A2 = np.array([[1, 2], [-2, -1], [-1, 0], [1, 0], [0, -1], [0, 1], [3, -1], [-1, -1]])
b2 = np.array([56, -14, 0, 28, 0, 21, -f1, -f2])
c2 = np.array([-1, 3])
res2 = linprog(c2, A_ub=A2, b_ub=b2)
print('Третья максимизация по f3:', res2.fun*-1, '\nТочка максимума:', res2.x)
