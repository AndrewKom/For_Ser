import numpy as np
import sympy
from scipy import optimize
from sympy import symbols, Matrix, Transpose, diff, poly, solve
from sympy.vector import CoordSys3D, gradient

list_f = [[-1,-1],[3,-1],[-1,3]]
lhs_ineq = [[-1,-1],[1,-2],[-3,2],[-1,0],[1,0],[0,-1],[0,1]]
rhs_ineq = [-28,14,28,0,56,0,42]
F_ideal = [];

for i in range(len(list_f)):
    res1 = optimize.linprog(c=list_f[i], A_ub=lhs_ineq, b_ub=rhs_ineq, method='revised simplex')
    print('Решение задачи f{}->max на области D: A{}({} ; {})'.format(i+1,i+1,res1.x[0],res1.x[1]), 'f{}(A{}):'.format(i+1,i+1), round(res1.fun*-1, ndigits=2))
    F_ideal.append(round(res1.fun*-1, ndigits=2))

print("1) Идеальная точка F*:", F_ideal)

k = 0
X0 = Matrix([28,14])
print("2) Начальное приближение: X0= [{} ; {}]".format(X0[0,0],X0[1,0]))
x1, x2 = sympy.symbols('x1 x2')
f1 = x1 + x2
f2 = -3*x1 + x2
f3 = x1 - 3*x2
fi = (f1 - F_ideal[0])**2 + (f2 - F_ideal[1])**2 + (f3 - F_ideal[2])**2
print("3) fi(F(x),F*) = ",fi)
fi_x1 = diff(fi, x1)
fi_x2 = diff(fi, x2)
print("4) Градиент функции fi: [{} ; {}]".format(fi_x1,fi_x2))

X = [X0]
k = 0
fi0 = fi.subs({x1:X[0][0,0],x2:X[0][1,0]})
print("5) Значение функции fi0(X0): ",fi0)

list_fi = [fi0]
fi_k = fi0
fi_k_1 = 0
lam = symbols('lam')
print("--------------------------------------------------------------------")
while True:
    x = X[k][0,0]
    y = X[k][1,0]
    fi_k_X = poly(fi_x1.subs({x1:x,x2:y})*x1 + fi_x2.subs({x1:x,x2:y})*x2)
    print("Вспомогательная функция fi_{}(X{}) = {}".format(k+1, k, fi_k_X))
    print("Решу задачу ЛП: fi_{}(X{})->min".format(k+1,k))
    res1 = optimize.linprog(c=[fi_k_X.coeffs()[0],fi_k_X.coeffs()[1]], A_ub=lhs_ineq, b_ub=rhs_ineq, method='revised simplex')
    print('X{}_: ({} ; {})'.format(k + 1, round(res1.x[0],2), round(res1.x[1],2)))
    Xk_ = Matrix([res1.x[0], res1.x[1]])
    print("Приближение к X{}".format(k+1))
    Xk = Matrix(X[k] + lam * (Xk_ - X[k]))
    fi_Xk_lam = fi.subs({x1:Xk[0,0],x2:Xk[1,0]})
    diff_fi_Xk_lam = diff(fi_Xk_lam,lam)
    l = round(solve(diff_fi_Xk_lam,lam)[0],2)
    Xk = Xk.subs({lam:l})
    print("X{}: ({} ; {})".format(k+1,round(Xk[0,0],2), round(Xk[1,0],2)))
    fi_k_1 = fi.subs({x1:Xk[0,0],x2:Xk[1,0]})
    print("fi(X{}): {}".format(k+1,fi_k_1))
    list_fi.append(fi_k_1)
    X.append(Xk)
    print("--------------------------------------------------------------------")
    if fi_k > fi_k_1:
        fi_k = fi_k_1
        fi_k_1 = 0
        k += 1
    else:
        break
