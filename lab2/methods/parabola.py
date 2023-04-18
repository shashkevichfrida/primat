import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1

def parabola(left, right, epsilon):
    iteration = 0
    call = 3

    a = left
    b = (left + right) / 2
    c = right

    f1 = f(a)
    f2 = f(b)
    f3 = f(c)


    for i in range(100):
        iteration += 1
        call += 1

        if f2 < f1 and f2 < f3:
            x = b - 0.5 * ((b - a)**2 * (f2 - f3) - (b - c)**2 * (f2 - f1)) / ((b - a) * (f2 - f3) - (b - c) * (f2 - f1))
            if x < b:
                c = b
            else:
                a = b
            b = x
        else:
            if f1 < f3:
                x = 0.5 * (a + b)
                c = b
                b = x
            else:
                x = 0.5 * (b + c)
                a = b
                b = x

        if abs(c - a) < epsilon:
            middle = (a + c) / 2
            return middle, f(middle), call, iteration
    raise Exception("Не удалось найти минимум за заданное число итераций(")
