import numpy as np
import matplotlib.pyplot as plt
import random
import random as r
from prettytable import PrettyTable
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

class tochka:
    def __init__(self, x, y, x1=0,y1=0, status=0, wasactive="-", dele='', bi=0, bname='', findex=0, fstatus=0,fstatus2=0):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.status = status
        self.wasactive = wasactive
        self.dele = dele
        self.bi = bi
        self.bname = bname
        self.findex = findex
        self.fstatus= fstatus
        self.fstatus2 = fstatus2
        self.nash = ((-6 * x1 * y1 + y1 + 3 * x1 + 6) - 6.5) * ((-2 * y1 + 7 * x1 * y1 - 4 * x1 + 5) - 3.857)


numtochek=5000




def zad2():
    for i in range (numtochek):
        for j in range(numtochek):
            if (list2[i].status == 0) and (i != j):
                list2[i].wasactive = '+'
                if (list2[j].x <= list2[i].x) and (list2[j].y <= list2[i].y) and (list2[j].status!=-1) :
                    list2[j].status = -1
                    j1= j+1
                    list2[i].dele = list2[i].dele + str(j1) + ' '
    pt1 = PrettyTable()
    pt1.field_names=["id", "f1", "f2",'Status', 'Use', 'Del']
    for i in range(numtochek):
        pt1.add_row([i + 1, list2[i].x, list2[i].y, list2[i].status, list2[i].wasactive, list2[i].dele])
    print(pt1)

list=[]
count=0

'''
for i in range(numtochek):
        plt.plot(list[i].x, list[i].y, marker=".", color="y")
plt.suptitle('Сетка')
plt.xlabel("p")
plt.ylabel("q")
plt.savefig('Сетка.png')
plt.show()
'''
A=([4,9],
   [7,6])
B=([6,1],
   [3,5])
#f1
list2=[]
for i in range(numtochek):
    mat1=([list[i].x, list[i].x1])
    res=np.dot(mat1,A)
    res1=np.dot(res,[(list[i].y),
                     (list[i].y1)])
    res2 = np.dot(mat1, B)
    res3 = np.dot(res2, [(list[i].y),
                        (list[i].y1)])
    list2.append(tochka(res1, res3))

zad2()



for i in range(numtochek):
    plt.plot(list2[i].x, list2[i].y, marker=".", color="y")
    if (list2[i].status == 0):
        plt.plot(list2[i].x, list2[i].y, marker=".", color="r")
        if (list2[i].x>=6.5 and list2[i].y>=3.86):
            list2[i].fstatus2=1
            plt.plot(list2[i].x, list2[i].y, marker=".", color="blue",zorder=2)
plt.suptitle('Множество Парето')
plt.xlabel("F1")
plt.ylabel("F2")
plt.savefig('Парето.png')
plt.show()

# Создаем матрицы выигрышей
A = np.array([[4, 9], [7, 6]])
B = np.array([[6, 1], [3, 5]])

print('A:')
[print(f'{item}') for item in A]
print('B:')
[print(f'{item}') for item in B]

# Ищем решения в чистых стратегиях
res_flag = False

for index, item in enumerate(A):
    max_column = A.T[index].argmax()
    max_row = B[index].argmax()
    if max_row == max_column:
        print(f'Решения в чистых стратегиях: A{max_column}{index} B{max_row}{index}')
        res_flag = True

if not res_flag:
    print('\nРешений в чистых стратегиях нет')

# Ищем решения в смешанных стратегиях
C = A[0][0] + A[1][1] - A[0][1] - A[1][0]
alpha = A[1][1] - A[0][1]
D = B[0][0] + B[1][1] - B[0][1] - B[1][0]
beta = B[1][1] - B[1][0]
uni_array = np.array([0, 0, 1, 1])
p_nesh = np.array([beta / D, 1 - beta / D])
q_nesh = np.array([alpha / C, 1 - alpha / C])
print(f'\nC= {C}\nalpha= {alpha}\nD= {D}\nbeta= {beta}')
print(f'\n[(p-1)*({C}q-{alpha})>=0\n[p*({C}q-{alpha})>=0')
print(f'\n[(q-1)*({D}p-{beta})>=0\n[q*({D}p-{alpha})>=0')
print(f'\n0<p<1 q=-{alpha}/{C}={alpha / C}')
print(f'0<q<1 p=-{beta}/{D}={beta / D}')
print('\np*=', p_nesh)
print('q*=', q_nesh)
buf_array = np.dot(p_nesh.T, A)
fa = np.dot(buf_array, q_nesh)
print('\nfA(p*,q*)=', fa)
buf_array = np.dot(p_nesh.T, B)
fb = np.dot(buf_array, q_nesh)
print('fB(p*,q*)=', fb)

# Ищем Парето оптимальное
array = []
best_point = [A[1][1], B[1][1]]
line_a = []
line_b = []
for i in range(len(A)):
    for j in range(len(A[0])):
        line_a.append(A[i][j])
        line_b.append(B[i][j])

print(line_a)
print(line_b)

# Ищем гарантированные решения
buf_array = np.dot(np.array([1/2, 1/2]).T, A)
fagarant = np.dot(buf_array, np.array([[1/2], [1/2]]))
print('\nfA_гарант=', fagarant)
buf_array = np.dot(np.array([2/7, 5/7]).T, B)
fbgarant = np.dot(buf_array, np.array([[2/7], [5/7]]))
print('fB_гарант=', fbgarant)


















