import random as r
import matplotlib.pyplot as plt
import numpy as np
import math




class tochka:
    def __init__(self, x, y, f1=0,f2=0, status=0):
        self.x = x
        self.y = y
        self.f1 = f1
        self.f2 = f2
        self.status = status


numtochek=100
fix_x=3


#Создание точек
list = []
for i in range(numtochek):
    x1=r.uniform(0,2)
    x2=r.uniform(0,2)
    list.append(tochka(x1,x2))
    plt.plot(list[i].x, list[i].y, marker=".", color="y")

plt.figure(1)
plt.suptitle('Сетка')
plt.xlabel("x1")
plt.ylabel("x2")
plt.savefig('Сетка.png')





def make_data_1(x1,x2):
    x = np.arange(0, 2, 0.001)
    y = np.arange(0, 2, 0.001)
    xgrid, ygrid = np.meshgrid(x, y)

    z1 = math.pow(x1,2)+math.pow(x2,2)-math.pow(x2,2)*(xgrid*xgrid-ygrid*ygrid)
    return xgrid, ygrid, z1

def make_data_2(x1,x2):
    x = np.arange(0, 2, 0.001)
    y = np.arange(0, 2, 0.001)
    xgrid, ygrid = np.meshgrid(x, y)

    z1 = math.pow(x1,2)+math.pow(x2,2)-math.pow(x1,2)*(xgrid*xgrid+ygrid*ygrid)
    return xgrid, ygrid, z1

plt.figure(2)
#Отрисовка линий уровня
for i in range(fix_x):
    random_x=r.randint(0,numtochek-1)
    fix_t = list[random_x]
    print(f'Фиксированная точка: x1={fix_t.x} x2={fix_t.y}')
    x,y,z = make_data_1(fix_t.x,fix_t.y)

    cs1 = plt.contour(x, y, z, colors='black',levels=20, linestyles='dashed')
    plt.clabel(cs1)

    x, y, z = make_data_2(fix_t.x, fix_t.y)
    cs = plt.contour(x, y, z, levels=20, cmap='viridis')
    plt.clabel(cs, inline=True, fontsize=8)
    plt.xlim(0, 2)
    plt.ylim(0, 2)

    plt.show()










