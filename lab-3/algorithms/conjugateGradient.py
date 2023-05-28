import numpy as np
from functionality import dec, my_func, draw

def conjugate_gradient(point, A, b, eps):
    x = point
    r = A.dot(point) + b
    p = -r
    counter = 0
    points_x = []
    points_y = []
    points_x.append(x[0])
    points_y.append(x[1])
    while np.linalg.norm(r) > eps:
        counter += 1
        alpha = r.dot(r) / p.dot(A.dot(p))
        x = x + alpha * p
        r_next = r + alpha * A.dot(p)
        beta = r_next.dot(r_next) / r.dot(r)
        p = -r_next + beta * p
        points_x.append(x[0])
        points_y.append(x[1])
        r = r_next
    draw(-2, 2, my_func, points_x, points_y, 'Conjugate gradient method')
    print('cojugate_gradient: func_value = ', my_func(x[0], x[1]), 'x = ', x[0], 'y = ', x[1], 'iterations = ', counter)