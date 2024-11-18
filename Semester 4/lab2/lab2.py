import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Activation
from tensorflow.keras.optimizers import SGD
import pandas as pd



df = pd.read_csv("input.csv",names=['q1','q2','psi','u1','u2','tau'])
#рандомизировать выборку
np.random.shuffle(df.values)

#Вход
x_train = df[['q1', 'q2']].head(200)
x_test = df[['q1', 'q2']].tail(56)

#Выход
y_train = df[['psi','u1','u2']].head(200)
y_test = df[['psi','u1','u2']].tail(56)

print(df)

# ПЕГАСЛОЙНЫЙ МЕГАТРОН
#5 слоёв, 50 нейронов, сигмоидальная функция, функция ошибки ср. кв. psi,u1,u2, стохастический градиент, мультистарт (из разных нач. приближений),

model = Sequential()
model.add(Dense(50, activation='sigmoid', input_dim=2)) #входной слой

# скрытые слои
model.add(Dense(50, activation='sigmoid'))
model.add(Dense(50, activation='sigmoid'))
model.add(Dense(50, activation='sigmoid'))
model.add(Dense(50, activation='sigmoid'))
model.add(Dense(50, activation='sigmoid'))

model.add(Dense(3)) # выходной слой

optimizer = SGD()  # Стохастический градиентный спуск
model.compile(loss='mean_squared_error', optimizer=optimizer)

history = model.fit(x_train, y_train, validation_data = (x_test,y_test), epochs=100, batch_size=1)



data = ([2.4],[1.4])
df1 = pd.DataFrame(data).T
df1.columns = ['q1','q2']

print(model.predict(df1))