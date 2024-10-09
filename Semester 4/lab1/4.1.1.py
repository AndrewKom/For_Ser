import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#Настоящее задание. Значение q ограничено от 0.8, 2.3

#Находим следующие данные и выводим как единную таблицу. Выводим тестовые 5 значений с шагом в 0.5 с отображением графиков
#Далее выводим всю таблицу с шагом в 0.01
# u1=u2 - производная
# Подставляем в f1(u1,u2) f2 (u1,u2)
# F0 - максимум среди F1 и F2
# Финал - ищем минимум среди F0

def v(q):
    return (q**2 * (q - 2)**2)

def f1(u1, u2, q=0.5):
    return 0.2 * (u1 - 7 * v(q))**2 + 0.8 * (u2 - 2 * v(q))**2

def f2(u1, u2, q=0.5):
    return 0.2 * (u1 - v(q))**2 + 0.8 * (u2 - 7 * v(q))**2

def d1(q):
    return 7 * v(q)

def d2(q):
    return 7 * v(q)



def grafprint(q):
    u1_vals = np.linspace(0, 8, 1000)
    u2_vals = np.linspace(0, 8, 1000)
    U1, U2 = np.meshgrid(u1_vals, u2_vals)

    F1 = f1(U1, U2,q)
    F2 = f2(U1, U2,q)

    fig, ax = plt.subplots(figsize=(8, 8))

    # Линии уровня для f1
    contour1 = ax.contour(U1, U2, F1, levels=20, colors = 'red')
    ax.clabel(contour1, inline=True, fontsize=8)

    # Линии уровня для f2
    contour2 = ax.contour(U1, U2, F2, levels=20, colors='green')
    ax.clabel(contour2, inline=True, fontsize=8)
    ax.set_xlabel('u1')
    ax.set_ylabel('u2')
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.grid(color='black', linestyle='-', linewidth=2)
    ax.set_title(f"При q={q}")
    plt.savefig(f"График при q={q}.jpg")
    plt.show()



def f_chit():
    results = []
    q_vals = np.arange(0.8, 2.301, 0.001)

    for q in q_vals:
        u1_nash = d1(q)
        u2_nash = d2(q)
        F1 = f1(u1_nash, u2_nash,q)
        F2 = f2(u1_nash, u2_nash,q)
        F0 = max(F1, F2) + 10 * math.fabs(math.sin(10*q)) + 8
        results.append({'q': q, 'u1': round(u1_nash,4), 'u2': round(u2_nash,4),
                        'F1': F1, 'F2': F2, 'F0': F0})

    df = pd.DataFrame(results)
    pd.set_option('display.max_rows', None)
    print(df)
    min_ch = df["F0"].min()
    print(f"Минимальное значение по F0 = {round(min_ch,4)}")
    plt.style.use('ggplot')
    df.plot(x="q",y="F0")
    plt.suptitle(f"Зависимость F0 от различных q")
    plt.savefig(f"Зависимость F0 от различных q")
    plt.show()




def printer(start=0.8,fin=2.31,sh=0.2):
    q_vals = np.arange(start, fin, sh)
    for q in q_vals:
        grafprint(round(q,2))


#printer()
f_chit()
