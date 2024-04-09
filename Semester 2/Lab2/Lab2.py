import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

X1 = [[3, 6, 4, 10], [9, 7, 5, 11], [4,5,6, 12], [7, 8, 9, 13], [6, 7, 9, 8], [4, 5, 6, 13], [10, 6, 5, 11], [9, 10, 8, 3]]
X2 = [[6, 7, 9, 8], [4, 5, 2, 14], [12, 8, 2, 8], [10, 11, 9, 4], [1, 2, 1, 2], [2, 6, 7, 4], [3, 3, 2, 3], [4, 2, 5, 3]]
c = [[0] * 4 for i in range(8)]
d = [[0] * 4 for i in range(8)]
print('исходная матрица ')
print('    |    z1   | ', '    z2   |', '    z3   |', '    z4   |')
print('----------------------------------------------')
for i in range(8):
    print('x', i + 1, '|', end=' '),
    for j in range(4):
        print(X1[i][j], ',', X2[i][j], "  | ", end=' ')
    print()

print('Принцип векторного максимина:')
a = []
for i in range(8):
    a.append(min(X1[i]))
b = []
for i in range(8):
    b.append(min(X2[i]))

print('  |x1 | x2| x3| x4| x5| x6| x7| x8')
print('v1|', end=' ')
for i in range(8):
    print(a[i], '|', end=' ')
print()
print('v2|', end=' ')
for j in range(8):
    print(b[j], '|', end=' ')
print()

p = [-1] * 8
for i in range(0, 8):
    for j in range(0, 8):
        if ((a[i] <= a[j]) & (b[i] <= b[j])):
            p[i] = p[i] + 1
ans1 = []
for i in range(0, 8):
    if (p[i] == 0) | (p[i] == 1):
        print(f'Множество эффективных решений задачи: V{i + 1}')
        print(f'Множество оптимальных проектов x{i + 1}')
        ans1.append(i)
fig = plt.figure()
for i in range(8):
    scatter([a[i]], [b[i]])
###################################

print('\nПринцип векторного минимаксного сожаления')

for j in range(4):
    for i in range(8):
        if (X1[i][j] > a[j]):
            a[j] = X1[i][j]
for j in range(4):
    for i in range(8):
        if (X2[i][j] > b[j]):
            b[j] = X2[i][j]

print(' множество идеальных точек')
print('  | z1  |z2    |z3     |z4')
print('w1|', end=' ')
for i in range(4):
    print(a[i], ' | ', end=' ')
print()
print('w2|', end=' ')
for j in range(4):
    print(b[j], ' | ', end=' ')
print()
print('\nТаблица значений функций векторных рисков')
print('    |     z1   | ', ' z2    |', '  z3    |', ' z4   |')
print('----------------------------------------------')
for i in range(8):
    print('x', i + 1, '|', end=' '),
    for j in range(4):
        c[i][j] = a[j] - X1[i][j]
        d[i][j] = b[j] - X2[i][j]
        print(' ', (c[i][j]), ',', (d[i][j]), ' |', end=' ')
    print()

print('\nмножество точек крайнего пессимизма')
a = []
for i in range(8):
    a.append(max(c[i]))
b = []
for i in range(8):
    b.append(max(d[i]))
print('  |x1 | x2| x3| x4| x5| x6| x7| x8')
print('v1|', end=' ')
for i in range(8):
    print(a[i], '|', end=' ')
print()
print('v2|', end=' ')
for j in range(8):
    print(b[j], '|', end=' ')
print()

p = [-1] * 8
for i in range(0, 8):
    for j in range(0, 8):
        if ((a[i] >= a[j]) & (b[i] >= b[j])):
            p[i] = p[i] + 1
ans2 = []
for i in range(0, 8):
    if p[i] == 0:
        print(f'Множество эффективных решений задачи: V{i + 1}')
        print(f'Множество оптимальных проектов x{i + 1}')
        ans2.append(i)
fig = plt.figure()
for i in range(8):
    scatter([a[i]], [b[i]])


################################### F
def C(X):
    Xt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0],
          [0, 0, 0, 0]]
    print('________________________')
    print('     |', '  z1 - z4', ' |')
    print('________________________')
    for i in range(8):
        print('x', i, ' ', X[i])
    a = []
    for i in range(8):
        a.append(min(X[i]))
    print('1)Вальд\nматрица ai: \n', a)
    for i in range(8):
        if (a[i] == max(a)):
            print('оптимальное решение: x', i + 1)
            Xt[i][0] = 1

    b = []
    bt = []
    for i in range(4):
        for j in range(8):
            bt.append(X[j][i])
        b.append(max(bt))
        bt = []
    print('\n2)Сэвидж\nматрица b: \n', b)

    r = [[], [], [], [], [], [], [], []]
    print('матрица r: ')
    for i in range(8):
        for j in range(4):
            r[i].append(b[j] - X[i][j])
        print(r[i])
    r1 = []
    for i in range(8):
        r1.append(max(r[i]))
    print('матрица bi: \n', r1)
    for i in range(8):
        if (r1[i] == min(r1)):
            print('оптимальное решение: x', i + 1)
            Xt[i][1] = 1

    g = []
    for i in range(8):
        g.append(0.6 * (min(X[i])) + 0.4 * (max(X[i])))
    G = g.index(max(g))
    print('\n3)Гурвиц')
    print('matrix G: \n', np.round(g, 1))
    print('оптимальное решение: x', G + 1)
    Xt[G][2] = 1

    f = []
    for i in range(8):
        f.append(0.25 * sum(X[i]))
    print('\n4)Лаплас\nматрица fi: \n', f)
    F = f.index(max(f))
    print('оптимальное решение: x', F + 1)
    Xt[F][3] = 1

    print('Матрица голосования')
    for i in range(8):
        print('x', i, ' ', Xt[i])
    fin = []
    for i in range(8):
        fin.append(sum(Xt[i]))
    Fin = fin.index(max(fin))
    print('\nоптимальный проект: x', Fin + 1)
    return Fin


F1 = C(X1)
F2 = C(X2)
Xt = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(ans1)):
    Xt[ans1[i]][0] = 1
for i in range(len(ans2)):
    Xt[ans2[i]][1] = 1
Xt[F1][2] = 1
Xt[F2][3] = 1
print('Итоговая матрица голосования')
for i in range(8):
    print('x', i+1, ' ', Xt[i])
fin = []
for i in range(8):
    fin.append(sum(Xt[i]))
for i in range(8):
    if fin[i] == max(fin):
        print('\nоптимальный проект: x', i + 1)
