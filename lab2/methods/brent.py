import numpy as np
import math

from numpy import size


def f(x):
    return np.sin(x) - np.log(x * x) - 1


def parabolaFormula(x1, x2, x3, f1, f2, f3):
    return x2 - ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) / (
                2 * (x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))


def brent(a, c, epsilon):
    iteration = 0
    call = 1

    goldenRatio = (3 - np.sqrt(5)) / 2
    x = (a + c) / 2
    w = v = x
    d = e = c - a
    fx = fw = fv = f(x)


    while (c - a) > epsilon:
        call += 1
        iteration += 1

        g = e
        e = d
        flag = False
        if (x != w) and (w != v) and (x != v):
            u = parabolaFormula(x, w, v, fx, fw, fv)
            if (u >= a + epsilon) and (u <= c - epsilon) and (abs(u - x) < g / 2):
                flag = True

        if flag == False:
            if x < (a + c) / 2:
                u = x + goldenRatio * (c - x)
            else:
                u = a + goldenRatio * (x - a)

        d = abs(u - x)

        fu = f(u)
        if (fu <= fx):
            if (u >= x):
                a = x
            else:
                c = x
            v = w
            w = x
            x = u
            fv = fw
            fw = fx
            fx = fu
        else:
            if (u >= x):
                c = u
            else:
                a = u
            if (fu <= fw):
                v = w
                w = u
                fv = fw
                fw = fu
            elif (fu <= fv) or (v == x) or (v == w):
                v = u
                fv = fu
    middle = (a + c) / 2

    return [middle, f(middle), call, iteration]

