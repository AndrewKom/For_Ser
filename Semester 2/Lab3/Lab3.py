import random
import numpy as np

A = np.array([[1, 2, 4, 6], [8, 7, 3, 2]])


iter = 100000
sum = 0



def rand_p_q():
    q1_1 = round(random.uniform(0., 1.0), 3)
    q2_1 = round(random.uniform(0., 1.0), 3)
    q3_1 = round(random.uniform(0., 1.0), 3)
    q4_1 = round(random.uniform(0., 1.0), 3)
    q1 = q1_1/(q1_1+q2_1+q3_1+q4_1)
    q2 = q2_1/(q1_1+q2_1+q3_1+q4_1)
    q3 = q3_1/(q1_1+q2_1+q3_1+q4_1)
    q4 = q4_1/(q1_1+q2_1+q3_1+q4_1)
    return q1, q2, q3, q4

def rand_p_q2():
    q1_1 = round(random.uniform(0., 1.0), 3)
    q2_1 = round(random.uniform(0., 1.0), 3)
    q1 = q1_1/(q1_1+q2_1)
    q2 = q2_1/(q1_1+q2_1)
    return q1, q2

def rand_p_q_0():
    q1_1 = round(random.uniform(0., 1.0), 2)
    q2_1 = round(random.uniform(0.1, 1.0), 2)
    q1=q1_1/(q1_1+q2_1)
    q2 = 0
    q3 = q2_1/(q1_1+q2_1)
    q4 = 0
    return q1, q2, q3, q4




def A1(A):
    return A[0, :]


def A2(A):
    return A[1, :]


p1_zv = 0.625  # найти аналитически
p2_zv = 0.375
vibor = input("ВВОД: 1 - Аналитически; 2-Для активных стратегий 1,3; 3 - q*,p*случайные ")
if (vibor == "1"):
    q1_zv = 0.125
    q2_zv = 0
    q3_zv = 0.875
    q4_zv = 0
    print("q1=", q1_zv, "q2=", q2_zv, "q3=", q3_zv, "q4=", q4_zv, )

elif(vibor == "2"):
    q1_zv, q2_zv, q3_zv, q4_zv = rand_p_q_0()
    print("q1=", q1_zv, "q2=", q2_zv, "q3=", q3_zv, "q4=", q4_zv, )
else:
    q1_zv, q2_zv, q3_zv, q4_zv = rand_p_q()
    print("q1=", q1_zv, "q2=", q2_zv, "q3=", q3_zv, "q4=", q4_zv, )

for i in range(iter):
    # p
    sluch_p = random.random()

    strat_A = []

    if sluch_p < p1_zv:
        strat_A = A1(A)
        print("Стратегия A1", A1(A))
    elif sluch_p >= p1_zv:
        strat_A = A2(A)
        print("Стратегия A2", A2(A))

    sluch_q = random.random()

    # q
    if (sluch_q >= 0) and (sluch_q < q1_zv):
        ind_B = 0
    elif (sluch_q >= q1_zv) and (sluch_q < q1_zv + q2_zv):
        ind_B = 1
    elif (sluch_q >= q1_zv + q2_zv) and (sluch_q < q1_zv + q2_zv + q3_zv):
        ind_B = 2
    elif (sluch_q >= q1_zv + q2_zv + q3_zv) and (sluch_q < 1):
        ind_B = 3
    stratB = strat_A[ind_B]
    print("Стратегия B", ind_B + 1,' Значение:', stratB, '\n' ,sep='')

    sum += stratB

print("Победа 1 игрока: Имитационный выигрыш  ", round(sum / iter,2))
