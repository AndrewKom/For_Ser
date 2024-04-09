import matplotlib.pyplot as plt
fig, axes = plt.subplots()
A = [[1,2,4,6],[8,7,3,2]]
k = 10000
A1 = 0
A2 = 0
pltk = []
pltvk = []
pp1 = []
pp2 = []
q1 = []
q2 = []
q3 = []
q4 = []
b1 = b2 = b3 = b4 = summp1 = summp2 = sq1 = sq2 = sq3 = sq4 = pl1 = pl2 = ql = ql2  = ql3 = ql4  = 0
i = 1
delp1 = [0]
delp2 = [0]
delp3 = [0]
delp4 = [0]
delq1 = [0]
delq4 = [0]
for k in range(1,k):
    if(i == 1):
         b1 += A[0][0]
         b2 += A[0][1]
         b3 += A[0][2]
         b4 += A[0][3]
         if (min(b1,b2,b3,b4) == b1):
              key = 0
         elif(min(b1,b2,b3,b4) == b2):
              key = 1
         elif(min(b1,b2,b3,b4) == b3):
              key = 2
         else:
              key = 3
    else:
         b1 += A[1][0]
         b2 += A[1][1]
         b3 += A[1][2]
         b4 += A[1][3]
         if (min(b1,b2,b3,b4) == b1):
              key = 0
         elif(min(b1,b2,b3,b4) == b2):
              key = 1
         elif(min(b1,b2,b3,b4) == b3):
              key = 2
         else:
              key = 3
    ak = min(b1,b2,b3,b4)/k
    j = key
    if (key == 0):
         sq1 += 1
    elif (key == 1):
         sq2 += 1
    elif (key == 2):
         sq3 += 1
    else:
         sq4 += 1
    q1.append(sq1/k)
    q2.append(sq2/k)
    q3.append(sq3/k)
    q4.append(sq4/k)
    A1 += A[0][j]
    A2 += A[1][j]
    bk = max(A1,A2)/k
    vk = (ak+bk)/2
    pltk.append(k)
    pltvk.append(round(vk,2))
    print('k = ',k,'|','i = ',i,'|','b1 = ',b1,'|','b2 = ',b2,'|','b3 = ',b3,'|', 'b4 = ',b4,'|','a(k) = ',round(ak,2),'|' ,'j = ',j+1,'|','A1 = ',A1,'|', 'A2 = ',A2,'|', 'b(k) = ',round(bk,2),'|', 'v(k) = ',round(vk,2))
    if(A1 > A2):
        i = 1
        summp1 += 1
    else:
        i = 2
        summp2 += 1
    pp1.append(summp1/k)
    pp2.append(summp2/k)
avgv = 3.625
for i in range (1,k):
     if(abs((pp1[i]-pp1[i-1] == 0))):
          delp1.append(0)
     else:
        delp1.append(abs((pp1[i]-pp1[i-1]))/pp1[i])
     if(abs((pp2[i]-pp2[i-1] == 0))):
          delp2.append(0)
     else:
        delp2.append(abs((pp2[i]-pp2[i-1]))/pp1[i])
     if(abs((q1[i]-q1[i-1] == 0))):
          delq1.append(0)
     else:
        delq1.append(abs((q1[i]-q1[i-1]))/q1[i])
     if(abs((q4[i]-q4[i-1] == 0))):
          delq4.append(0)
     else:
        delq4.append(abs((q4[i]-q4[i-1]))/q4[i])
plt.suptitle("Цена игры")
plt.plot(pltk,pltvk,'r', color = 'blue')
plt.plot(pltk,[avgv for i in range(len(pltk))], color = 'red')


fix, ax = plt.subplots(nrows = 2, ncols = 1)
#ax.set_ylim(ymin = 0, ymax = 1)
#plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1],[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])

#ax[1].yticks([0.0])
pl1 = summp1/len(pltk)
pl2 = summp2/len(pltk)
ql1 = sq1/len(pltk)
ql2 = sq2/len(pltk)
ql3 = sq3/len(pltk)
ql4 = sq4/len(pltk)
print ('p1 = ', round(pl1,3))
print ('p2 = ', round(pl2,3))
print ('q1 = ', round(ql1,3))
print ('q2 = ', round(ql2,3))
print ('q3 = ', round(ql3,3))
print ('q4 = ', round(ql4,3))

#plt.plot(pltk,[p1 for i in range(len(pltk))], color = 'red', label = 'p1')
#plt.plot(pltk,[p1 for i in range(len(pltk))], color = 'red', label = 'p1')

ax[0].set_title("Значения по активным стратегиям в зависимости от итерации")
ax[0].plot(pltk,pp1, color = 'red', label = 'p1')
ax[0].plot(pltk,pp2, color = 'blue', label = 'p2')
ax[0].legend()

#plt.yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])
ax[1].plot(pltk,q1, color = 'green', label = 'q1')
ax[1].plot(pltk,q3, color = 'cyan', label = 'q3')
ax[1].legend()
#plt.legend()

fixx, axx = plt.subplots(nrows = 2, ncols = 2)
axx[0,0].plot(pltk,delp1, color = 'red', label = 'p1')
axx[0,1].plot(pltk,delp2, color = 'blue', label = 'p2')
axx[1,0].plot(pltk,delq1, color = 'green', label = 'q1')
axx[1,1].plot(pltk,delq4, color = 'cyan', label = 'q3')
axx[0,0].legend()
axx[0,1].legend()
axx[1,0].legend()
axx[1,1].legend()
plt.show()
