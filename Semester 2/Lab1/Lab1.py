a=[[3,6,4,10],[6,7,9,8],[9,7,5,11],[4,5,6,13],[4,5,6,12],[10,6,5,11],[7,8,9,13],[9,10,8,3]]
min =[0]*8
w=[0]*5
z=0
print('исходная матрица ')
for i in range(8):
    for j in range(4):
        print(a[i][j], end=' ')
    print()
print ('----------------------------------------------------------')
print('Критерий Вальда')
print('минимальный элемент по строке')
for i in range(8):
     min[i] = a[i][0]
     for j in range(4):
         if (a[i][j]< min[i]) :
             min[i] = a[i][j]
             j=j+1
     print('a[',i+1,']=',min[i])
     i=i+1
max=min[0]
for i in range (8):
    if max< min[i]:
        max=min[i]
        k1=i+1
    i=i+1
print ('максимальный элемент по столбцу а=max a[',k1,']=',max)
print('оптимальное решение по критерию Вальда х',k1)
w[z]=k1
z=z+1
print ('----------------------------------------------------------')
print('Критерий Сэвиджа')
print('матрица рисков')
ax=[[0]*4]*8
b=[0]*4
b=[8,9,6,5]
i=0
j=0
max1 =[0]*8
for i in range(8):
    max1[i]=0
    for j in range(4):
        ax[i][j]=b[j]-a[i][j]
        print(ax[i][j], end=' ')
        if (max1[i]<ax[i][j]):
            max1[i]=ax[i][j]
    print()
print('максимальный элемент по строке')
for ii in range (8):
    print('b[',ii+1,']=',max1[ii])
min1=max1[0]
for i in range (8):
    if min1> max1[i]:
        min1=max1[i]
        k2=i+1
    i=i+1
print ('минимальный элемент по столбцу b=min b[', k2,']=',min1)
print('оптимальное решение по критерию Сэвиджа х',k2)
w[z]=k2
z=z+1
print ('----------------------------------------------------------')
print('Критерий Гурвица')
y=0.6
max2 =[0]*8
min2 =[0]*8
g =([0]*8)
for i in range(8):
    max2[i]=a[i][0]
    min2[i]=a[i][0]
    for j in range(4):
        if (max2[i]<a[i][j]):
            max2[i]=a[i][j]
        if(min2[i]>a[i][j]):
            min2[i]=a[i][j]
    g[i]=y*min2[i]+(1-y)*max2[i]
print('максимальный элемент по строке')
for i in range (8):
    print('g[',i+1,']=',round(g[i],1))
max3=g[0]
for i in range (8):
    if max3< g[i]:
        max3=g[i]
        k3=i+1
    i=i+1
print ('максимальный эленмент с=max g[', k3,']=',max3)
print('оптимальное решение по критерию гурвица х',k3)
w[z]=k3
z=z+1
print ('----------------------------------------------------------')
print('Критерий Байеса')
p=[0.1,0.4,0.4,0.1]
d =([0]*8)
for i in range(8):
    for j in range(4):
        d[i]=d[i]+a[i][j]*p[j]
    print(round(d[i],1))
max4=d[0]
for i in range (8):
    if max4< d[i]:
        max4=d[i]
        k4=i+1
    i=i+1
print ('максимальный эленмент g=max g[', k4,']=',round(max4,1))
print('оптимальное решение по критерию Байеса х',k4)
w[z]=k4
z=z+1
print ('----------------------------------------------------------')
print('Критерий Лапласа')
n=4
f =([0]*8)
for i in range(8):
    for j in range(4):
        f[i]=f[i]+a[i][j]*(1/n)
    print(round(f[i],2))
max5=f[0]
for i in range (8):
    if max5< f[i]:
        max5=f[i]
        k5=i+1
    i=i+1
print ('максимальный эленмент f=max f[', k5,']=',round(max5,2))
print('оптимальное решение по критерию Лапласа х',k5)
w[z]=k5
print ('----------------------------------------------------------')
print(' Матрица голосования')
t=[[0]*5]*8
x=[0]*8
for i in range(8):
    for j in range (5):
        if (i==w[j]-1):
            print ('+', end=' ')
            x[i]=x[i]+1
        else:
            print ('-', end=' ')
    print (x[i])
    print()
max6=x[0]
for i in range (8):
    if max6<x[i]:
        max6=x[i]
        kg=i+1
print ('оптимальное решение Х', kg)
