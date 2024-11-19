import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, SGD
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from keras import layers
from keras import initializers
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import math as m




# Загрузка данных
data = pd.read_csv('tr_set_9_2.csv', delimiter=';')
np.random.shuffle(data.values)

# Подготовка данных
X = data[['q1', 'q2']].values
Y = data[['psi 1', 'u1', 'u2']].values

# Разделение данных на тренировочные и тестовые наборы
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Создание модели

model = Sequential()
#initializer = initializers.RandomUniform(minval=-1.0, maxval=1.0)
model.add(Dense(50, input_dim=2,use_bias=True)) #входной слой
#model.add(Dense(50, activation='sigmoid', kernel_initializer=initializer,  use_bias=True))
model.add(Dense(50, activation='sigmoid',  use_bias=True))
model.add(Dense(50, activation='sigmoid',  use_bias=True))
model.add(Dense(50, activation='sigmoid', use_bias=True))
model.add(Dense(3, activation='sigmoid',use_bias=True)) # выходной слой

# Компиляция модели
optimizer = Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-07, amsgrad=False)  # Стохастический градиентный спуск/градиентный спуск адама!
model.compile(loss='mean_squared_error', optimizer=optimizer)

# Обучение модели
history = model.fit(X_train, Y_train,
                    validation_data=(X_test, Y_test),
                    epochs=10, #500,
                    batch_size=21)

# Оценка модели на тестовом наборе
test_loss = model.evaluate(X_test, Y_test)
print(f'Test Loss: {test_loss:.4f}')


print(model.summary())
# Предсказание на тестовой выборке
predictions = model.predict(X_test)

# Создание DataFrame с предсказаниями и входными данными
predictions_df = pd.DataFrame(predictions, columns=['psi1_pred', 'u1_pred', 'u2_pred'])
input_df = pd.DataFrame(X_test, columns=['q1', 'q2'])
true_df = pd.DataFrame(Y_test, columns=['psi1_true', 'u1_true', 'u2_true'])

# Объединение входных данных, истинных значений и предсказаний
result_df = pd.concat([input_df, true_df, predictions_df], axis=1)


maxtime = 0.15
result_df = result_df.drop( result_df[(((result_df['u1_true']) - (result_df['u1_pred'])) >= maxtime) |
                                      (((result_df['u2_true']) - (result_df['u2_pred'])) >= maxtime) |
                                      (((result_df['u1_pred']) - (result_df['u1_true'])) >= maxtime) |
                                      (((result_df['u2_pred']) - (result_df['u2_true'])) >= maxtime)].index)



print("\nPredictions:")
print(result_df)



#Отрисовка графики u1
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_zlim(0, 1)

ax.scatter(result_df["q1"], result_df["q2"], result_df["u1_pred"], c="red")
ax.scatter(result_df["q1"], result_df["q2"], result_df["u1_true"], c="blue")

# Определяем метки и цвета легенды
legend_labels = ['Предсказанные значения', 'Настоящие значения']
legend_colors = ['r', 'b']

# Добавляем легенду к графику
ax.legend(legend_labels, loc='upper right', scatterpoints=1, fontsize=10, markerscale=2)


ax.set_title('U1')
plt.xlabel("q1")
plt.ylabel("q2")
plt.savefig('u1.png')
plt.show()

#Отрисовка графики u1
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_zlim(0, 1)

ax.scatter(result_df["q1"], result_df["q2"], result_df["u2_pred"], c="red")
ax.scatter(result_df["q1"], result_df["q2"], result_df["u2_true"], c="blue")

# Определяем метки и цвета легенды
legend_labels = ['Предсказанные значения', 'Настоящие значения']
legend_colors = ['r', 'b']

# Добавляем легенду к графику
ax.legend(legend_labels, loc='upper right', scatterpoints=1, fontsize=10, markerscale=2)

ax.set_title('U2')
plt.xlabel("q1")
plt.ylabel("q2")
plt.savefig('u2.png')
plt.show()
