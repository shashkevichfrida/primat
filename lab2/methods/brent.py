import numpy as np
import math
from scipy.optimize import minimize_scalar


def f(x):
    return np.sin(x) - np.log(x * x) - 1


def brent(left, right, eps):
    array = []

    fa = f(left)
    fb = f(right)
    #if fa * fb >= 0:
     #   raise ValueError("Brent's method requires f(a) and f(b) to have opposite signs")
    if abs(fa) < abs(fb):
        left, right = right, left
        fa, fb = fb, fa
    c = left
    mflag = True
    s = 0
    d = 0
    while abs(right - left) > eps:
        fc = f(c)
        if fa != fc and fb != fc:
            s = (left*fb*fc)/((fa - fb)*(fa - fc)) + (right*fa*fc)/((fb - fa)*(fb - fc)) + (c*fa*fb)/((fc - fa)*(fc - fb))
            if s > min((3*left + right)/4, (left + 3*right)/4) or s < left or s > right:
                s = (left + right)/2
                mflag = True
        else:
            s = (left + right)/2
            mflag = True
        if mflag:
            d = abs(s - c)
        else:
            d = abs(s - old_s)/2
        old_s = s
        fs = f(s)
        if fs > 0:
            right = s
            fb = fs
        else:
            left = s
            fa = fs
        if abs(fa) < abs(fb):
            left, right = right, left
            fa, fb = fb, fa
        if abs(d) < eps:
            break
        c = s
        mflag = False
    return s, f(s), call, iteration
