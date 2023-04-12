import numpy as np
import math

def f(x):
    return np.sin(x) - np.log(x * x) - 1


def brent(left, right, epsilon):
    iteration = 0
    call = 1

    golden_section = (3 - math.sqrt(5)) / 2


    x = w = v = (left + right) / 2
    fx = fw = fv = f(x)
    d = e = right - left


    while iteration < 10000000:
        call += 1
        iteration += 1

        m = 0.5 * (right + left)
        precision1 = epsilon * abs(x) + epsilon
        precision2 = 2 * precision1

        if abs(x - m) <= precision2 - 0.5 * (right - left):
            break

        r = q = p = 0

        if abs(e) > precision1:
            r = (x - w) * (fx - fv)
            q = (x - v) * (fx - fw)
            p = (x - v) * q - (x - w) * r
            q = 2 * (q - r)
            if q > 0:
                p = -p
            q = abs(q)
            r = e
            e = d


        if abs(p) < abs(0.5 * q * r) and p > q * (left - x) and p < q * (right - x):
            d = p / q
            u = x + d

            if u - left < precision2 or right - u < precision2:
                d = precision1 if x < m else -precision1
        else:
            d = golden_section * (e if x < m else -e)
            u = x + d

            if u - left < precision2 or right - u < precision2:
                d = precision1 if x < m else -precision1


        fu = f(u)
        if fu <= fx:
            if u >= x:
                left = x
            else:
                right = x
            v, w, x = w, x, u
            fv, fw, fx = fw, fx, fu
        else:
            if u >= x:
                right = u
            else:
                left = u
            if fu <= fw or w == x:
                v, w, fv, fw = w, u, fw, fu
            elif fu <= fv or v == x or v == w:
                v, fv = u, fu

    return x, f(x), iteration, call

