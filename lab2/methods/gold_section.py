import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1

def gold_section(left, right, epsilon):
    iteration = 0
    call = 2

    middle = (right + left) / 2
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi

    a = left + resphi * (right - left)
    b = right - resphi * (right - left)
    f1 = f(a)
    f2 = f(b)

    while right - left >= epsilon:
        call += 1
        iteration += 1

        if f1 < f2:
            right = b
            b = a
            f2 = f1
            a = left + resphi * (right - left)
            f1 = f(a)
        else:
            left = a
            a = b
            f1 = f2
            b = right - resphi * (right - left)
            f2 = f(b)

        middle = (a + b) / 2
    return middle, f(middle), call, iteration

