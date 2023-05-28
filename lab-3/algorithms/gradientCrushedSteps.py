from math import fabs


from functionality import dec, my_func, draw

h = dec(0.000001)


def gradientCrushedSteps(eps, point):
    next_point = point.copy()
    count = 0
    alfa = dec(0.1)
    points_x = []
    points_y = []
    while True:
        count = count + 1
        points_x.append(next_point[0])
        points_y.append(next_point[1])
        f = my_func(point[0], point[1])
        grad_x = (my_func(point[0] + h, point[1]) - my_func(point[0] - h, point[1])) / (2 * h)
        grad_y = (my_func(point[0], point[1] + h) - my_func(point[0], point[1] - h)) / (2 * h)
        f_next = my_func(point[0] - alfa * grad_x, point[1] - alfa * grad_y)
        if f_next < f:
            next_point[0] = point[0] - grad_x * alfa
            next_point[1] = point[1] - grad_y * alfa
        else:
            alfa = dec(alfa/2)
            next_point[0] = point[0] - grad_x * alfa
            next_point[1] = point[1] - grad_y * alfa
        if fabs(point[0] - next_point[0]) <= eps and fabs(point[1] - next_point[1]) <= eps and fabs(f - f_next) <= eps:
            break
        point = next_point.copy()
    draw(-2, 2, my_func, points_x, points_y, 'Gradient with level sets method')
    print('gradient_crushed_step:', 'func_value = ', my_func(point[0], point[1]), 'x = ', point[0], ' y = ', point[1], 'iterations =  ', count)

