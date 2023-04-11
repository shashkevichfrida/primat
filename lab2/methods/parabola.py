import numpy as np

def f(x):
    return np.sin(x) - np.log(x * x) - 1

def parabola(a, b, eps):
    x0, x1, x2 = a, (a + b) / 2, b
    for i in range(100):
        f0, f1, f2 = f(x0), f(x1), f(x2)
        if f1 < f0 and f1 < f2:
            xm = x1 - 0.5 * ((x1 - x0)**2 * (f1 - f2) - (x1 - x2)**2 * (f1 - f0)) / ((x1 - x0) * (f1 - f2) - (x1 - x2) * (f1 - f0))
            if xm < x1:
                x2 = x1
            else:
                x0 = x1
            x1 = xm
        else:
            if f0 < f2:
                xm = 0.5 * (x0 + x1)
                x2 = x1
                x1 = xm
            else:
                xm = 0.5 * (x1 + x2)
                x0 = x1
                x1 = xm
        if abs(x2 - x0) < eps:
            xmin = (x0 + x2) / 2
            return xmin
    raise Exception("Не удалось найти минимум за заданное число итераций(")
