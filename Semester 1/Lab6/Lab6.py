import random as r
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt

numtochek = 21
n = 14
count = 0
list = []
list_p = []


class tochka:
    def __init__(self, x, y, id=0, status=0, wasactive="-", dele=''):
        self.x = x
        self.y = y
        self.id = id
        self.status = status
        self.wasactive = wasactive
        self.dele = dele


def idletochka(min=10000000, maxx=28, maxy=26.522):
    for i in range(len(list_p)):
        if (min > ((maxx - list_p[i].x) ** 2 + (maxy - list_p[i].y) ** 2)):
            min = ((maxx - list_p[i].x) ** 2 + (maxy - list_p[i].y) ** 2)
            maxl = list_p[i].id
    print(f"Оптимальная точка по методу Идеальной точки: {maxl}")
    printl()


def GlKr(max=0, y1=19.6, y2=25.2):
    for i in range(len(list_p)):
        if (list_p[i].y >= y2) and (max <= list_p[i].x):
            max = list_p[i].x
            maxc = list_p[i].id
    print(f"Решение по главному критерию а) точка {maxc}")
    max = 0
    for i in range(len(list_p)):
        if (list_p[i].x >= y1) and (max <= list_p[i].y):
            max = list_p[i].y
            maxc = list_p[i].id
    print(f"Решение по главному критерию б) точка {maxc}")


def printl():
    print("-" * 50)


def sumu(u1, u2, max=0):
    for i in range(len(list_p)):
        lmax = round(list_p[i].x * u1 + list_p[i].y * u2, 2)
        print(lmax)
        if max <= (lmax):
            max = lmax
            maxc = list_p[i].id
    print(f"При u1= {u1} и u2= {u2} \n Решение точка {maxc}")


def Germer(max=0):
    for i in range(len(list_p)):
        if (list_p[i].x < list_p[i].y) and (max < list_p[i].x):
            max = list_p[i].x
            maxc = list_p[i].id
        elif ((list_p[i].x >= list_p[i].y) and (max < list_p[i].y)):
            max = list_p[i].y
            maxc = list_p[i].id
    print(f"По Гермейеру оптимальная точка: {maxc}")
    for i in range(len(list_p)):
        if list_p[i].id == maxc:
            plt.plot(list_p[i].x, list_p[i].y, marker="*", color="b")


def zad2():
    for i in range(numtochek):
        for j in range(numtochek):
            if (list[i].status == 0) and (i != j):
                list[i].wasactive = '+'
                if (list[j].x <= list[i].x) and (list[j].y <= list[i].y) and (list[j].status != -1):
                    list[j].status = -1
                    j1 = j + 1
                    list[i].dele = list[i].dele + str(j1) + ' '

    pt1 = PrettyTable()
    pt2 = PrettyTable()
    pt1.field_names = ["id", "f1", "f2", 'Status', 'Use', 'Del']
    pt2.field_names = ["id", "f1", "f2"]
    for i in range(numtochek):
        pt1.add_row([i + 1, list[i].x, list[i].y, list[i].status, list[i].wasactive, list[i].dele])
        if list[i].status == 0:
            list_p.append(tochka(list[i].x, list[i].y, i + 1))
    for i in range(len(list_p)):
        pt2.add_row([list_p[i].id, list_p[i].x, list_p[i].y])
    print(pt1)
    print("Оптимальные по Парето\n", pt2)
    printl()
    sumu(0.2, 0.8)
    printl()
    sumu(0.3, 0.7)
    printl()
    sumu(0.7, 0.3)
    printl()
    GlKr()
    printl()
    idletochka()
    #for i in np.arange(0.1,0.9,0.1):
    #    sumu(round(i,1), round(1-i,1))
    for i in range(numtochek):
        if (list[i].status == 0):
            plt.plot(list[i].x, list[i].y, marker=".", color="g")
        else:
            plt.plot(list[i].x, list[i].y, marker=".", color="r")
    Germer()
    printl()
    plt.suptitle('Множество Парето')
    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.legend(['Множество Парето'], frameon=False)
    plt.savefig('Figure2.png')
    plt.show()


numtochek = int(input("Введите количество"))
if numtochek == 21:
    list.append(tochka(20, 20))
    list.append(tochka(25, 18))
    list.append(tochka(19, 23))
    list.append(tochka(24, 14))
    list.append(tochka(19, 15))
    list.append(tochka(15, 19))
    list.append(tochka(15, 25))
    list.append(tochka(13, 23))
    list.append(tochka(11, 21))
    list.append(tochka(13, 17))
    list.append(tochka(21, 10))
    list.append(tochka(27, 15))
    list.append(tochka(25, 10))
    list.append(tochka(22, 22))
    list.append(tochka(22, 17))
    list.append(tochka(18, 17))
    list.append(tochka(26, 12))
    list.append(tochka(16, 22))
    list.append(tochka(17, 20))
    list.append(tochka(16, 15))
    list.append(tochka(12.522, 26.521))
else:
    while count < numtochek:  # Заполнение случайными числами
        y = r.uniform(5.6, 26.523)
        x = r.uniform(7, 28.1)
        if (y - x <= n) and (x + y >= n * 2) and ((x ** 2) / (4 * (n ** 2)) + ((y - n) ** 2) / (n ** 2) <= 1):
            list.append(tochka(x, y))
            count = count + 1
zad2()
