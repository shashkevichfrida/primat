import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1

def gold_section(left, right, eps):
    middle = (right + left) / 2
    array = np.array([left, right, middle, f(middle)])

    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi
    x1 = left + resphi * (right - left)
    x2 = right - resphi * (right - left)
    f1 = f(x1)
    f2 = f(x2)
    while abs(right - left) >= eps:
        if f1 < f2:
            right = x2
            x2 = x1
            f2 = f1
            x1 = left + resphi * (right - left)
            f1 = f(x1)
        else:
            left = x1
            x1 = x2
            f1 = f2
            x2 = right - resphi * (right - left)
            f2 = f(x2)
        middle1 = (x1 + x2) / 2

    array = np.append(array, [left, right, middle, middle1])
    return middle, f(middle), array

