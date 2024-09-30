import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


#Настоящее задание. Значение q ограничено от

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
    contour1 = ax.contour(U1, U2, F1, levels=20, cmap = 'CMRmap')
    ax.clabel(contour1, inline=True, fontsize=8)

    # Линии уровня для f2
    contour2 = ax.contour(U1, U2, F2, levels=20, cmap='autumn')
    ax.clabel(contour2, inline=True, fontsize=8)
    ax.set_xlabel('u1')
    ax.set_ylabel('u2')
    ax.set_aspect('equal')
    plt.tight_layout()
    plt.grid(color='black', linestyle='-', linewidth=2)
    ax.set_title(f"При q={q}")
    plt.show()



def f_chit():
    results = []
    q_vals = np.arange(0.8, 1.61, 0.01)

    for q in q_vals:
        u1_nash = d1(q)
        u2_nash = d2(q)
        F1 = f1(u1_nash, u2_nash,q)
        F2 = f2(u1_nash, u2_nash,q)
        F0 = max(F1, F2)
        results.append({'q': q, 'u1': u1_nash, 'u2': u2_nash,
                        'F1': F1, 'F2': F2, 'F0': F0})

    df = pd.DataFrame(results)
    pd.set_option('display.max_rows', None)
    print(df)



def printer(start=0.8,fin=1.61,sh=0.2):
    q_vals = np.arange(start, fin, sh)
    for q in q_vals:
        grafprint(round(q,2))


printer()
f_chit()
