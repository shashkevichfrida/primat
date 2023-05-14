import numpy as np
import matplotlib.pyplot as plt

# функция потерь
def objective(w1, w2):
    return w1 ** 2 + w2 ** 2

# производную по первой
def partial_1(w1):
    return 2.0 * w1

# и второй переменной
def partial_2(w2):
    return 2.0 * w2

def gradient_desc_const_step():
    # изначальные веса
    w1, w2 = 3, 4

    # количество итераций
    iter = 100

    # скорость обучения
    learning_rate = 0.05

    w1_list, w2_list, l_list = [], [], []

    # в цикле с заданным количеством итераций
    # будем добавлять текущие веса в соответствующие списки
    # и рассчитывать и добавлять в список текущий уровень ошибки
    # также рассчитаем значение частных производных при текущих весах
    # будем обновлять веса в направлении,
    # обратном направлению градиента, умноженному на скорость обучения
    for i in range(iter):

        w1_list.append(w1)
        w2_list.append(w2)

        l_list.append(objective(w1, w2))

        par_1 = partial_1(w1)
        par_2 = partial_2(w2)

        w1 = w1 - learning_rate * par_1
        w2 = w2 - learning_rate * par_2

    # итоговые веса модели и значение функции потерь
    w1, w2, objective(w1, w2)

    fig = plt.figure(figsize=(14, 12))

    w1 = np.linspace(-5, 5, 1000)
    w2 = np.linspace(-5, 5, 1000)

    w1, w2 = np.meshgrid(w1, w2)
    f = w1 ** 2 + w2 ** 2

    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(w1, w2, f, alpha=0.4, cmap='Blues')

    ax.text(3, 3.5, 28, 'A', size=25)
    ax.text(0, -0.4, 4, 'B', size=25)

    ax.set_xlabel('w1', fontsize=15)
    ax.set_ylabel('w2', fontsize=15)
    ax.set_zlabel('f(w1, w2)', fontsize=15)

    ax.plot(w1_list, w2_list, l_list, '.-', c='red')
    plt.show()