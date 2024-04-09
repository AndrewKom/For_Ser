import random as r
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import webbrowser

numtochek = 100
print("Введите количество точек")
numtochek = int(input())

count = 0
list = []


class tochka:
    def __init__(self, x, y, j1=0, j2=0, status=0, wasactive="-", dele=''):
        self.x = x
        self.y = y
        self.j1 = j1
        self.j2= j2
        self.status = status
        self.wasactive = wasactive
        self.dele = dele
        self.point = "+"


def ABCD(nu_x_beg, nu_x_end, nu_y_beg, nu_y_end):
    l = []
    if nu_y_end >= -nu_x_end + 1 and nu_y_beg <= -nu_x_beg + 1:
        if nu_y_end <= -nu_x_beg + 1:
            if nu_y_beg <= -nu_x_end + 1:
                xbeg = 1 - nu_y_end
                xend = nu_x_end
                ybeg = -nu_x_end + 1
                yend = nu_y_end

            else:
                xbeg = 1 - nu_y_end
                xend = 1 - nu_y_beg
                ybeg = nu_y_beg
                yend = nu_y_end
        else:
            if nu_y_beg >= -nu_x_beg + 1:
                xbeg = nu_x_beg
                xend = 1 - nu_y_beg
                ybeg = nu_y_beg
                yend = -nu_x_beg + 1
            else:
                xbeg = nu_x_beg
                xend = nu_x_end
                ybeg = 1 - nu_x_end
                yend = 1 - nu_x_beg
    l.append(xbeg)
    l.append(xend)
    l.append(ybeg)
    l.append(yend)
    return l

def Omega():
    list2=[]
    l = ABCD(0.3, 0.6, 0.4, 0.7)
    print("Матрица B : \n", l[0], l[3], "\n", l[1], l[2])
    for i in range(numtochek):
        if list[i].point != "-":
            for k in range(numtochek):
                if k != i and list[k].point != "-":
                    if list[k].j1 <= list[i].j1 and list[k].j2 <= list[i].j2:
                        list[k].point = "-"
    for i in range(numtochek):
        list2.append(tochka(list[i].x, list[i].y))
        list2[i].j1 = list[i].j1
        list2[i].j2 = list[i].j2
    for i in range(numtochek):
        if list2[i].point != "-":
            for k in range(numtochek):
                if k != i:
                    if ((list2[i].j1 - list2[k].j1) * l[0] + (
                            list2[i].j2 - list2[k].j2) * l[1]) > 0 and (
                            (list2[i].j1 - list2[k].j1) * l[3] + (
                            list2[i].j2 - list2[k].j2) * l[2]) > 0:
                        list2[i].point = "-"
    for i in range(numtochek):
        if list2[i].point == "+":
            plt.plot(list2[i].j1, list2[i].j2, ".", color="y")
    plt.suptitle('Омега-оптимальные точки')
    plt.xlabel("j1")
    plt.ylabel("j2")
    plt.legend(['Омега точки'], frameon=False)
    plt.savefig('Omega.png')
    plt.show()

    for i in range(numtochek):
        plt.plot(list[i].j1, list[i].j2, marker=".", color="r")
    for i in range(numtochek):
        if (list[i].status == 0):
            plt.plot(list[i].j1, list[i].j2, marker=".", color="g")
    for i in range(numtochek):
        if list2[i].point == "+":
            plt.plot(list2[i].j1, list2[i].j2, ".", color="y")
    plt.suptitle('Омега-оптимальные точки')
    plt.xlabel("j1")
    plt.ylabel("j2")
    plt.savefig('Omega2.png')
    plt.show()

# Выполнение задания 2 с помощью алгоритма исключения заведомо неэффективных решений
def zad2():
    for i in range(numtochek):
        for j in range(numtochek):
            if (list[i].status == 0) and (i != j):
                list[i].wasactive = '+'
                if (list[j].j1 >= list[i].j1) and (list[j].j2 >= list[i].j2) and (list[j].status != -1):
                    list[j].status = -1
                    j1 = j + 1
                    list[i].dele = list[i].dele + str(j1) + ' '
    webbrowser.open_new_tab("https://clck.ru/33mmCQ")
    for i in range(5):
        webbrowser.open_new_tab("https://clck.ru/AXQBP")
    pt1 = PrettyTable()
    pt1.field_names = ["id", "u1", "u2", "j1", "j2", 'Status', 'Use', 'Del']
    for i in range(numtochek):
        pt1.add_row([i + 1, list[i].x, list[i].y, list[i].j1, list[i].j2, list[i].status, list[i].wasactive, list[i].dele])
    print(pt1)







# Заполнение случайными числами или личными значениями

if numtochek==10:
    list.append(tochka(5, 12))
    list.append(tochka(10, 10))
    list.append(tochka(22, 22))
    list.append(tochka(15, 12))
    list.append(tochka(11, 40))
    list.append(tochka(78, 60))
    list.append(tochka(45, 75))
    list.append(tochka(30, 32))
    list.append(tochka(4, 18))
    list.append(tochka(2, 30))
else:
    while count < numtochek:
        y = r.uniform(0, 79.1)
        x = r.uniform(0, 79.1)
        if (x >= 0) and (x <= 79) and (y >= 0) and (y <= 79):
            list.append(tochka(x, y))
            count = count + 1

for i in range(numtochek):
    list[i].j1 = 0.2*(list[i].x-70)**2+0.8*(list[i].y-20)**2
    list[i].j2 = 0.2 * (list[i].x - 10) ** 2 + 0.8*(list[i].y - 70) ** 2



zad2()
for i in range(numtochek):
    plt.plot(list[i].x, list[i].y, marker=".", color="y")
plt.suptitle('Точки на множестве D')
plt.xlabel("u1")
plt.ylabel("u2")
plt.legend(['Точки на множестве D'], frameon=False)
plt.savefig('Tochki D.png')
plt.show()


for i in range(numtochek):
    plt.plot(list[i].j1, list[i].j2, marker=".", color="r")
plt.suptitle('Точки на множестве J1(u) J2(u)')
plt.xlabel("J1")
plt.ylabel("J2")
plt.legend(['Точки'], frameon=False)
plt.savefig('Tochki J1(u) J2(u).png')
plt.show()


for i in range(numtochek):
    if (list[i].status == 0):
        plt.plot(list[i].j1, list[i].j2, marker=".", color="r")
plt.suptitle('Множество Парето')
plt.xlabel("J1")
plt.ylabel("J2")
plt.legend(['Множество Парето'], frameon=False)
plt.savefig('Parreto.png')
plt.show()

Omega()


