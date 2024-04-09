import random as r
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
numtochek=20
print("Введите количество точек")
numtochek= int(input())
n=14
k1=1
k2=0.85
k3=0.75
count=0
list=[]


class tochka:
    def __init__(self, x, y, status=0, wasactive="-", dele='', bi=0, bname='', findex=0, fstatus=0):
        self.x = x
        self.y = y
        self.status = status
        self.wasactive = wasactive
        self.dele = dele
        self.bi = bi
        self.bname = bname
        self.findex = findex
        self.fstatus= fstatus

#Создание исходного графика с точками
def graficshow():

    y1=lambda x: n+x
    y2 = lambda x: (n*2)-x
    fig, axes = plt.subplots()
    x = np.linspace(0, 30, 2)
    Drawing_uncolored_circle = plt.Circle((n, n), n, color='r', fill=False, label='(f1-n)^2+(f2-n)^2<=n^2')
    axes.set_aspect(1)
    axes.add_artist(Drawing_uncolored_circle)
    plt.plot(x, y1(x), label='-f1+f2<=n')
    plt.plot(x, y2(x), label='f1+f2>=2n')
    for i in range(numtochek):
        plt.plot(list[i].x, list[i].y, marker=".", color="r")
    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.legend(fontsize='xx-small',frameon = False)
    plt.suptitle('График')
    plt.savefig('Figure.png')

    plt.show()


#Выполнение задания 2 с помощью алгоритма исключения заведомо неэффективных решений
def zad2():
    for i in range (numtochek):
        for j in range(numtochek):
            if (list[i].status == 0) and (i != j):
                list[i].wasactive = '+'
                if (list[j].x >= list[i].x) and (list[j].y >= list[i].y) and (list[j].status!=-1) :
                    list[j].status = -1
                    j1= j+1
                    list[i].dele = list[i].dele + str(j1) + ' '

    pt1 = PrettyTable()
    pt1.field_names=["id", "f1", "f2",'Status', 'Use', 'Del']
    for i in range(numtochek):
        pt1.add_row([i + 1, list[i].x, list[i].y, list[i].status, list[i].wasactive, list[i].dele])
    print(pt1)


#3 задание и кластеризация
def zad3():
    for i in range (numtochek):
        for j in range(numtochek):
            if (i != j):
                if (list[j].x >= list[i].x) and (list[j].y >= list[i].y) :
                    list[i].bi=list[i].bi+1
                    j1= j+1
                    list[i].bname = list[i].bname + str(j1) + ' '
        list[i].findex = 1/(1+(list[i].bi/(numtochek-1)))
        if (abs(k1 - list[i].findex) < abs(k2 - list[i].findex)) and (abs(k1 - list[i].findex) < abs(k3 - list[i].findex)):
            list[i].fstatus = 1
        elif (abs(k2 - list[i].findex) < abs(k1 - list[i].findex)) and (abs(k2 - list[i].findex) < abs(k3 - list[i].findex)):
            list[i].fstatus = 2
        elif (abs(k3 - list[i].findex) < abs(k1 - list[i].findex)) and (abs(k3 - list[i].findex) < abs(k2 - list[i].findex)):
            list[i].fstatus = 3
    #for i in range(numtochek):
    #    print("id:",i+1," f1:",list[i].x," f2:", list[i].y, " bi:",list[i].bi," bi():",list[i].bname," Ф:",list[i].findex," Ki:",list[i].fstatus)
    #print("-"*100)
    pt2 = PrettyTable()
    pt2.field_names = ["id", "f1","f2", "bi", 'bi()', 'Ф', 'Ki']
    for i in range(numtochek):
        pt2.add_row([i + 1, list[i].x, list[i].y, list[i].bi, list[i].bname, list[i].findex,list[i].fstatus])
    print(pt2)

    #Вывод кластеров по индексам эффективности
    count1=0
    count2=0
    count3=0
    for i in range(numtochek):
        if list[i].fstatus == 1 and (count1==0):
            plt.plot(list[i].x, list[i].y, marker="s", color="r")
            count1=count1+1
    for i in range(numtochek):
        if list[i].fstatus == 2 and (count2==0):
            plt.plot(list[i].x, list[i].y, marker="^", color="g")
            count2 = count2 + 1
    for i in range(numtochek):
        if list[i].fstatus == 3 and (count3==0):
            plt.plot(list[i].x, list[i].y, marker="*", color="m")
            count3 = count3 + 1
    for i in range(numtochek):
        if list[i].fstatus == 1:
            plt.plot(list[i].x, list[i].y, marker="s", color="r")
        if list[i].fstatus == 2:
            plt.plot(list[i].x, list[i].y, marker="^", color="g")
        if list[i].fstatus == 3:
            plt.plot(list[i].x, list[i].y, marker="*", color="m")
    plt.suptitle('Кластеры')
    plt.xlabel("F1")
    plt.ylabel("F2")
    plt.legend(['1','2','3'],fontsize='xx-small')
    plt.savefig('Figure3.png')
    plt.show()

#Заполнение случайными числами

while count < numtochek:
    y = r.uniform(4.101, 29)
    x = r.uniform(7, 29)
    if (y <= n+x) and (y >= 2*n-x) and ((x-n)**2+(y-n)**2 <= n**2):
        list.append(tochka(x, y))
        count = count+1

#list.append(tochka(7, 6))
#list.append(tochka(4, 8))
#list.append(tochka(6, 7))
#list.append(tochka(3, 10))
#list.append(tochka(5, 12))
#list.append(tochka(6, 10))
#list.append(tochka(4, 11))
#list.append(tochka(10, 11))
#list.append(tochka(25, 10))
#list.append(tochka(26, 20))
#list.append(tochka(23, 23))
#list.append(tochka(23, 11))
#list.append(tochka(25, 8))
#list.append(tochka(22, 14))
#list.append(tochka(19, 24))
#list.append(tochka(14, 18))
#list.append(tochka(9, 21))
#list.append(tochka(18, 14))
#list.append(tochka(19, 23))
#list.append(tochka(23, 22))


graficshow()
zad2()
for i in range(numtochek):
    if (list[i].status == 0):
        plt.plot(list[i].x, list[i].y, marker=".", color="y")
    else:
        plt.plot(list[i].x, list[i].y, marker=".", color="r")
plt.suptitle('Множество Парето')
plt.xlabel("F1")
plt.ylabel("F2")
plt.legend(['Множество Парето'], frameon=False)
plt.savefig('Figure2.png')
plt.show()

zad3()


test_number=0
while test_number != 4:
    test_text = input("Введите число: \n 1-Общий график \n 2-Парето \n 3-Кластеры \n 4-Конец ")
    test_number = int(test_text)
    if test_number == 1:
        graficshow()
    elif (test_number == 2):
        # График множества Парето
        for i in range(numtochek):
            if (list[i].status == 0):
                plt.plot(list[i].x, list[i].y, marker=".", color="y")
        plt.suptitle('Множество Парето')
        plt.xlabel("F1")
        plt.ylabel("F2")
        plt.legend(['Множество Парето'], frameon=False)
        plt.savefig('Figure2.png')
        plt.show()
    elif (test_number == 3):
        # Вывод кластеров по индексам эффективности
        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(numtochek):
            if list[i].fstatus == 1 and (count1 == 0):
                plt.plot(list[i].x, list[i].y, marker="s", color="r")
                count1 = count1 + 1
        for i in range(numtochek):
            if list[i].fstatus == 2 and (count2 == 0):
                plt.plot(list[i].x, list[i].y, marker="^", color="g")
                count2 = count2 + 1
        for i in range(numtochek):
            if list[i].fstatus == 3 and (count3 == 0):
                plt.plot(list[i].x, list[i].y, marker="*", color="m")
                count3 = count3 + 1
        for i in range(numtochek):
            if list[i].fstatus == 1:
                plt.plot(list[i].x, list[i].y, marker="s", color="r")
            if list[i].fstatus == 2:
                plt.plot(list[i].x, list[i].y, marker="^", color="g")
            if list[i].fstatus == 3:
                plt.plot(list[i].x, list[i].y, marker="*", color="m")
        plt.suptitle('Кластеры')
        plt.xlabel("F1")
        plt.ylabel("F2")
        plt.legend(['1', '2', '3'], fontsize='xx-small')
        plt.savefig('Figure3.png')
        plt.show()
    elif (test_number == 4):print("До свидания!")
    else:print("Неверное число")