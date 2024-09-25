from fractions import Fraction
from decimal import Decimal

A = [[9,1],[3,2]]
B = [[5,15],[4,5]]

C = A[0][0] - A[1][0] - A[0][1] + A[1][1]
alpha = A[1][1] - A[0][1]
D = B[0][0] - B[1][0] - B[0][1] + B[1][1]
beta = B[1][1] - B[1][0]

print(f'C = {C}')
print(f'alpha = {alpha}')
print(f'D = {D}')
print(f'beta = {beta}')


point1 = Fraction(Decimal(alpha)/Decimal(C)).limit_denominator()
point2 = Fraction(Decimal(beta)/Decimal(D)).limit_denominator()
print(f'p* = [{point2}, {1-point2}]')
print(f'q* = [{point1}, {1-point1}]')


def nblue(x):
    return 0*x + point1
def nred(x):
    return 0*x + point2


class Point:
    def __init__(self, x, y, p, q):
        self.x = x
        self.y = y
        self.p = p
        self.q = q
        self.optimal = None
        self.slater = None
        self.nash = ((-6 * p * q + q + 3 * p + 6) - 6.5) * ((-2 * q + 7 * p * q - 4 * p + 5) - 3.857)


def exclude_unoptimal(points):
    for i in points:
        if i.optimal == False:
            continue
        for j in points:
            if j == i:
                continue
            if i.x <= j.x and i.y <= j.y:
                i.optimal = False
                break
    for i in points:
        if i.optimal == None:
            i.optimal = True


def slater(points, x, y):
    for i in points:
        if i.x <= x or i.y <= y:
            i.slater = False
        else:
            i.slater = True


import numpy as np
def getPoint(p,q):
    f1 = np.array([p,1-p]) @ A @ np.array([[q],[1-q]])
    f2 = np.array([p,1-p]) @ B @ np.array([[q],[1-q]])
    return Point(f1[0],f2[0],p,q)


import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import numpy as np

x = np.linspace(0,10)
import random
points = []

for i in range(5000):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    points.append(getPoint(x,y))

exclude_unoptimal(points)
nash = getPoint(point2,point1)

slater(points,nash.x,nash.y)

opt = [point for point in points if point.optimal == True and point.slater == False]
slater = [point for point in points if point.slater == True and point.optimal == True]
unopt = [point for point in points if point.optimal == False]
max_nash = max(slater, key = lambda x: x.nash)
plt.scatter([point.x for point in opt],[point.y for point in opt], color='red', zorder=1)
plt.scatter([point.x for point in slater],[point.y for point in slater], color='blue', zorder=2)
plt.scatter([point.x for point in unopt],[point.y for point in unopt], color='y',zorder=0)

plt.scatter(max_nash.x, max_nash.y, color='cyan', zorder=2)
plt.scatter(nash.x,nash.y,color='blue', marker="*",zorder=2)
print(f"Максимум в точке {max_nash.x} {max_nash.y}")

plt.suptitle('Множество Парето')
plt.xlabel("F1")
plt.ylabel("F2")
plt.savefig('Парето.png')


plt.show()


def model(p, q, a, cnt, summ):
    print(f'{cnt}', end='\t\t\t')
    pStrat = random.uniform(0, 1)
    qStrat = random.uniform(0, 1)
    choiceP = 0
    choiceQ = 0
    if (pStrat > p[0]):
        print('2', end='\t\t\t')
        choiceP = 1
    else:
        print('1', end='\t\t\t')
    if (qStrat > q[0]):
        print('2', end='\t\t\t')
        choiceQ = 1
    else:
        print('1', end='\t\t\t')
    choice = a[choiceP][choiceQ]
    summ += choice
    print(choice)
    return choice, summ


def draw_model(q, p, a, cnt):
    summ = 0
    print('Номер итерации  \t Стратегия игрока 1 \t Стратегия игрока 2 \t Выбранный эл-т')
    x = [i + 1 for i in range(cnt)]
    y = []
    for i in range(cnt):
        res, summ = model(q, p, a, i + 1, summ)
        y.append(res)
    figure, axes = plt.subplots()
    axes.set_xlim(xmin=0, xmax=cnt)
    axes.set_ylim(ymin=min(y) - 0.01, ymax=max(y) + 0.01)
    axes.grid(which='major', color='#CCCCCC', linestyle='--')
    axes.grid(which='minor', color='#CCCCCC', linestyle=':')
    v = summ / cnt
    v = [v for i in range(cnt)]
    plt.xlabel('n')
    plt.plot(x, y)
    plt.plot(x, v)
    plt.text(cnt, summ / cnt + 0.05, summ / cnt, zorder=0)
    print(summ / cnt)
    return plt


def imitation_model(p_res, q_res, df):
    cnt = 50000
    plot = draw_model(p_res, np.array([0.4, 0.657]), df, cnt)
    plot.show()
    print(f"Эксперимент 2: p*, q1 = 0.5, q2= 0.5")
    plot = draw_model(p_res, np.array([0.495, 0.505]), df, cnt)
    plot.show()




print('Первый игрок')
imitation_model(np.array([[1 / 2], [1 / 2]]), np.array([[4 / 7], [3 / 7]]), np.array(A))

