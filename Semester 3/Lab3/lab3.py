from sympy.combinatorics.graycode import random_bitstring
from sympy.combinatorics.graycode import gray_to_bin
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")





#25 для 100
# 4 для 24
qz=0
qi=1
bi = []
f = []
m = 32
number_gen = int(input("Введите количество генотипов: "))
divider = int(input("Количество групп: "))
counter_generation = int(input("Количество поколений: "))


df = pd.DataFrame({
    'bkgx1': [],
    'bkgx2': [],
    'l1': [],
    'l2': [],
    'x1': [],
    'x2': [],
    'f1': [],
    'f2': [],
})

dftime = pd.DataFrame({
    'bkgx1': [],
    'bkgx2': [],
    'l1': [],
    'l2': [],
    'x1': [],
    'x2': [],
    'f1': [],
    'f2': [],
    'b': [],
    'fitness': []
})

for i in range(number_gen):
    bkgx1 = random_bitstring(m)
    bkgx2 = random_bitstring(m)
    l1 = int(gray_to_bin(bkgx1),2)
    l2 = int(gray_to_bin(bkgx2),2)
    x1 = l1 * (79 / (2 ** m - 1))
    x2 = l2 * (79 / (2 ** m - 1))
    f1 = 0.2 * (x1 - 70) ** 2 + 0.8 * (x2 - 20) ** 2
    f2 = 0.2 * (x1 - 10) ** 2 + 0.8 * (x2 - 70) ** 2
    row = {'bkgx1':bkgx1,'bkgx2':bkgx2,'l1':l1,'l2':l2,'x1':x1,'x2':x2,'f1':f1,'f2':f2}
    df.loc[len(df.index)] = row






# Вычисление фитнес-функции
def calculate_fitness_function(dataframe):
    bi_counter = []
    values_function = []
    for index1, row1 in dataframe[['f1', 'f2']].iterrows():
        count = 0
        for index2, row2 in dataframe[['f1', 'f2']].iterrows():
            if (row1[0] > row2[0] and row1[1] > row2[1]):
                count += 1
        bi_counter.append(count)
        values_function.append((number_gen - 1) / (number_gen - 1 + count))
        qz=(1/(1+(count)/(number_gen-1)))**qi
    return bi_counter, values_function



bi, f = calculate_fitness_function(df)

df.insert(8,'b',bi)
df.insert(9,'fitness',f)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.options.display.expand_frame_repr = False

print("Родители")
print(df.to_string())
print()

fig, ax = plt.subplots()
plt.ion()
line, = ax.plot(df['x1'].tolist(), df['x2'].tolist(), 'o',color='y')
for j1 in range(number_gen):
    plt.text(df['x1'][j1], df['x2'][j1], j1, fontsize=8)

plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Множество допустимых альтернативных решений D')
line.set_xdata(df['x1'].tolist())
line.set_ydata(df['x2'].tolist())
x1, y1 = [79, 79], [0, 79]
x2, y2 = [0, 79], [79, 79]
x3, y3 = [0, 79], [0, 0]
x4, y4 = [0, 0], [0, 79]
plt.plot(x1, y1, x2, y2, x3, y3,x4, y4, color='red')
plt.draw()
plt.pause(0.001)

df_parents = pd.DataFrame({
    'bkgx1': [],
    'bkgx2': [],
    'l1': [],
    'l2': [],
    'x1': [],
    'x2': [],
    'f1': [],
    'f2': [],
    'b': [],
    'fitness': []
})

# 3 шаг
# турнирная схема
# разбить на группы
# пока не накопится 24 лучших

def find_best_parents(all_parents):
    best_parents = pd.DataFrame({
        'bkgx1': [],
        'bkgx2': [],
        'l1': [],
        'l2': [],
        'x1': [],
        'x2': [],
        'f1': [],
        'f2': [],
        'b': [],
        'fitness': []
    })
    count = 0
    counter = 0
    while count != number_gen:
        temp_df = all_parents.copy(deep=True)
        for i in range(divider):
            group = pd.DataFrame({
                'bkgx1': [],
                'bkgx2': [],
                'l1': [],
                'l2': [],
                'x1': [],
                'x2': [],
                'f1': [],
                'f2': [],
                'b': [],
                'fitness': []
            })
            number_parents = number_gen // divider
            for j in range(number_parents):
                random = randint(0, number_gen - 1 - i * number_parents - j)
                parent = temp_df.iloc[random]
                temp_df.drop(labels=random, axis=0, inplace=True)
                temp_df.reset_index(drop=True, inplace=True)
                group.loc[len(group.index)] = parent
            group = group.sort_values(by='fitness', ascending=False)
            group.reset_index(drop=True,inplace=True)
            if counter!=divider:
                print("Группа:")
                print(group)
                counter+=1
            best_parents.loc[len(best_parents.index)] = group.iloc[0]
            best_parents.loc[len(best_parents.index)] = group.iloc[1]
            count += 2
            row = {'bkgx1': group.iloc[0].bkgx1, 'bkgx2': group.iloc[0].bkgx2, 'l1': group.iloc[0].l1, 'l2': group.iloc[0].l2, 'x1': group.iloc[0].x1, 'x2': group.iloc[0].x2, 'f1': group.iloc[0].f1, 'f2': group.iloc[0].f2,'b': group.iloc[0].b,'fitness': group.iloc[0].fitness}
            dftime.loc[len(dftime.index)] = row
            row = {'bkgx1': group.iloc[1].bkgx1, 'bkgx2': group.iloc[1].bkgx2, 'l1': group.iloc[1].l1,
                   'l2': group.iloc[1].l2, 'x1': group.iloc[1].x1, 'x2': group.iloc[1].x2, 'f1': group.iloc[1].f1,
                   'f2': group.iloc[1].f2, 'b': group.iloc[1].b, 'fitness': group.iloc[1].fitness}
            dftime.loc[len(dftime.index)] = row
    return best_parents

def new_generation(best_parents):
    # 4 шаг
    df_childs = pd.DataFrame({
        'bkgx1': [],
        'bkgx2': [],
        'l1': [],
        'l2': [],
        'x1': [],
        'x2': [],
        'f1': [],
        'f2': [],
    })

    # разбить на пары
    # кроссовер
    # обмен хромосомами
    counter = 0
    while counter != number_gen:
        # Выбор случайных пар родителей
        random = randint(0, number_gen - 1 - counter)
        parent1 = best_parents.iloc[random]
        best_parents.drop(labels=random, axis=0, inplace=True)
        best_parents.reset_index(drop=True, inplace=True)
        counter += 1
        random = randint(0, number_gen - 1 - counter)
        parent2 = best_parents.iloc[random]
        best_parents.drop(labels=random, axis=0, inplace=True)
        best_parents.reset_index(drop=True, inplace=True)
        counter += 1

        # Кроссовер
        # Выбор 3 точек
        left = randint(1, number_gen - 1)
        right = randint(1, number_gen - 1)

        # Разделение хромосомы на участки
        sectors1 = []
        sectors1.append(parent1['bkgx1'][:left])
        sectors1.append(parent1['bkgx1'][left:])
        sectors1.append(parent1['bkgx2'][:right])
        sectors1.append(parent1['bkgx2'][right:])
        sectors2 = []
        sectors2.append(parent2['bkgx1'][:left])
        sectors2.append(parent2['bkgx1'][left:])
        sectors2.append(parent2['bkgx2'][:right])
        sectors2.append(parent2['bkgx2'][right:])

        temp = ''
        for i in range(1, 4, 2):
            temp = sectors1[i]
            sectors1[i] = sectors2[i]
            sectors2[i] = temp

        # Получение потомков
        child1_bkgx1 = sectors1[0] + sectors1[1]
        child1_bkgx2 = sectors1[2] + sectors1[3]

        child2_bkgx1 = sectors2[0] + sectors2[1]
        child2_bkgx2 = sectors2[2] + sectors2[3]



        # Мутация
        '''
        mutate = randint(1, 100)
        if mutate == 1:
            choice = randint(1, 2)
            if choice == 1:
                child1_bkgx1 = mutation(child1_bkgx1)
            else:
                child1_bkgx2 = mutation(child1_bkgx2)

        mutate = randint(1, 100)
        if mutate == 1:
            choice = randint(1, 2)
            if choice == 1:
                child2_bkgx1 = mutation(child2_bkgx1)
            else:
                child2_bkgx2 = mutation(child2_bkgx2)
        '''


        l1 = int(gray_to_bin(child1_bkgx1), 2)
        l2 = int(gray_to_bin(child1_bkgx2), 2)
        x1 = l1 * (79 / (2 ** m - 1))
        x2 = l2 * (79 / (2 ** m - 1))
        f1 = 0.2 * (x1 - 70) ** 2 + 0.8 * (x2 - 20) ** 2
        f2 = 0.2 * (x1 - 10) ** 2 + 0.8 * (x2 - 70) ** 2
        row = {'bkgx1': child1_bkgx1, 'bkgx2': child1_bkgx2, 'l1': l1, 'l2': l2, 'x1': x1, 'x2': x2, 'f1': f1, 'f2': f2}
        df_childs.loc[len(df_childs.index)] = row

        l1 = int(gray_to_bin(child2_bkgx1), 2)
        l2 = int(gray_to_bin(child2_bkgx2), 2)
        x1 = l1 * (79 / (2 ** m - 1))
        x2 = l2 * (79 / (2 ** m - 1))
        f1 = 0.2 * (x1 - 70) ** 2 + 0.8 * (x2 - 20) ** 2
        f2 = 0.2 * (x1 - 10) ** 2 + 0.8 * (x2 - 70) ** 2
        row = {'bkgx1': child2_bkgx1, 'bkgx2': child2_bkgx2, 'l1': l1, 'l2': l2, 'x1': x1, 'x2': x2, 'f1': f1, 'f2': f2}
        df_childs.loc[len(df_childs.index)] = row
    b, fitness_value = calculate_fitness_function(df_childs)
    df_childs.insert(8, 'b', b)
    df_childs.insert(9, 'fitness', fitness_value)
    return df_childs


plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(df['f1'].tolist(), df['f2'].tolist(), 'o',color='black')
for j2 in range(number_gen):
    plt.text(df['f1'][j2], df['f2'][j2], j2, fontsize=8,color='red')
plt.xlabel('f1')
plt.ylabel('f2')
plt.title('Все родители')
line.set_xdata(df['f1'].tolist())
line.set_ydata(df['f2'].tolist())
plt.draw()
plt.gcf().canvas.flush_events()
plt.pause(4)

def mutation(bkgx):
    x = bkgx
    random = randint(0, len(bkgx) - 1)
    if bkgx[random] == '0':
        x = bkgx[:random] + '1' + bkgx[random + 1:]
    else:
        x = bkgx[:random] + '0' + bkgx[random + 1:]
    return x
def counter_elite_points(dataframe):
    coun_elite = 0
    fitness_list = dataframe['fitness'].tolist()
    for fitness in fitness_list:
        if (fitness == 1):
            coun_elite += 1
    return coun_elite


def counter_elite_pointss(dataframe):
    list=[]
    count=0
    fitness_list = dataframe['fitness'].tolist()
    for fitness in fitness_list:
        if (fitness == 1):
            list.append(count)
        count += 1
    return list




ostanovka = number_gen * 0.7
for i in range(counter_generation):
    df_parents = find_best_parents(df)
    df = new_generation(df_parents)

    count_elite = counter_elite_points(df)
    stime=counter_elite_pointss(df)
    print(f'Поколение {i+1}, элитных точек: {count_elite} {stime}')
    print(df)
    print()

    fig, ax = plt.subplots()
    plt.ion()
    line, = ax.plot(df['x1'].tolist(), df['x2'].tolist(), 'o', color='y')
    j3=0
    for j3 in range(number_gen):
        plt.text(df['x1'][j3], df['x2'][j3], j3, fontsize=8)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title(f'Множество допустимых альтернативных решений D, Поколение: {i+1}')
    line.set_xdata(df['x1'].tolist())
    line.set_ydata(df['x2'].tolist())
    x1, y1 = [79, 79], [0, 79]
    x2, y2 = [0, 79], [79, 79]
    x3, y3 = [0, 79], [0, 0]
    x4, y4 = [0, 0], [0, 79]
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, color='red')
    plt.draw()
    plt.pause(0.001)


    fig, ax = plt.subplots()
    line, = ax.plot(df['f1'].tolist(), df['f2'].tolist(), 'o', color='red')
    for j in range(number_gen):
        plt.text(df['f1'][j], df['f2'][j], j, fontsize=8)


    #plt.title(f'Поколение {i+1}, элитных точек: {count_elite}')
    plt.title(f'Поколение {i + 1}')

    plt.draw()
    plt.gcf().canvas.flush_events()

    plt.pause(2)

#Если требуется процент
'''
    # Если накопится больше 70% элитных точек программа завершается
    if count_elite >= ostanovka:
        break
'''
dftime=dftime.drop_duplicates()
print("Общий массив")
print(dftime.to_string(index=False))
print()


#Если требуется сортировать только по 1
dftime = dftime[dftime.fitness == 1]


dftime=dftime.sort_values(by='fitness', ascending=False)
print("Сортированный массив")
print(dftime.to_string(index=False))
print()
plt.ioff()
plt.show()