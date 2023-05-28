import decimal
import numpy as np
from matplotlib import pyplot as plt

def dec(x):
    return decimal.Decimal(x)


def my_func(x, y):
    # return x ** 2 + y ** 2 - x
    #return (3 * x + 2) ** 2 + (6 + y) ** 2 - 5 * x * y
    return (2 * x + 1) ** 2 + y ** 2 + x * y


def draw(a, b, func, points_x, points_y, title):
    fig, ax = plt.subplots()
    x, y = np.mgrid[a:b:100j, a:b:100j]
    ax.contour(x, y, func(x, y), levels=100, colors='skyblue')
    ax.set_title(title)
    for i in range(len(points_x)):
        ax.scatter(points_x[i], points_y[i], c='black')
    ax.plot([points_x[i] for i in range(len(points_x))], [points_y[i] for i in range(len(points_y))], c='black')
    plt.show()


def draw_func(func, a, b):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    x, y = np.mgrid[a:b:100j, a:b:100j]
    ax.contour(x, y, func(x, y), levels=100, colors='firebrick')
    plt.show()