import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1


def dichotomy(left, right, epsilon):
    iteration = 0
    call = 0

    middle = (right + left) / 2
    delta = epsilon * 0.1

    while right - left >= epsilon:
        call += 2
        iteration += 1

        a = (left + right) / 2 - delta
        b = (left + right) / 2 + delta

        if f(a) < f(b):
            right = b
        elif f(a) > f(b):
            left = a
        elif f(a) == f(b):
            right = a
            left = b

    middle = (a + b) / 2
    return middle, f(middle), call, iteration



