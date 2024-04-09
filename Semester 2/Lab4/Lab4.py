import numpy as np
from scipy.optimize import linprog


##РЕШЕНИЕ ДВОЙСТВЕННОЙ ЗАДАЧИ
def simplex_method(c, A, b):
    result = linprog(c, A_ub=A, b_ub=b, method='simplex')

    return result.x, result.fun


c = np.array([-1, -1, -1, -1])

A = np.array([[1, 2, 4, 6],
              [8, 7, 3, 2]])
b = np.array([1, 1])

y, z = simplex_method(c, A, b)

print(f"Решение двойственной задачи: y = {y}, Z(y) = {-z}")


##РЕШЕНИЕ ПРЯМОЙ ЗАДАЧИ

def simplex_method_1(c_1, A_1, b_1):
    result = linprog(c=c_1, A_ub=A_1, b_ub=b_1, method='simplex')

    return result.x, result.fun


c_1 = np.array([1, 1])

A_1 = np.array([[-1, -8],
                [-2, -7, ],
                [-4, -3],
                [-6, -2]])

b_1 = np.array([-1, -1, -1, -1])

x, f = simplex_method_1(c_1, A_1, b_1)
print("_________________________________________")
print(f"Решение двойственной задачи: y = {y}, Z(y) = {-z}")
print(f"Решение прямой задачи: x = {x}, F(x) = {f}")
print("_________________________________________")


V_1 = 1 / (x[0] + x[1])
V_2 = 1 / (y[0] + y[1] + y[2] + y[3])

p1 = x[0] * V_1
p2 = x[1] * V_1

q1 = y[0] * V_2
q2 = y[1] * V_2
q3 = y[2] * V_2
q4 = y[3] * V_2

print("РЕШЕНИЕ ИГРЫ")
print("Оптимальные стратегии игры:")
print("p*=[", round(p1, 2), ";", round(p2, 2), "] q*=[", round(q1, 2), ";", round(q2, 2), ";", round(q3, 2), ";",
      round(q4, 2), "]")
print("Цена игры V = ", round(V_1, 2))