import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def conjugate_gradient(A, b, x0, tol=1e-10, max_iter=1000):
    x = x0
    r = b - np.dot(A, x)
    p = r
    rs_old = np.dot(np.transpose(r), r)

    # create empty lists to store values for plotting
    xs = [x[0]]
    ys = [x[1]]
    zs = [np.dot(np.dot(x, A), np.transpose(x)) - np.dot(np.transpose(b), x)]

    for _ in range(max_iter):
        Ap = np.dot(A, p)
        alpha = rs_old / np.dot(np.transpose(p), Ap)
        x = x + alpha * p
        r = r - alpha * Ap
        rs_new = np.dot(np.transpose(r), r)

        if np.sqrt(rs_new) < tol:
            break

        p = r + (rs_new / rs_old) * p
        rs_old = rs_new

        # store intermediate values of x and z
        xs.append(x[0])
        ys.append(x[1])
        zs.append(np.dot(np.dot(x, A), np.transpose(x)) - np.dot(np.transpose(b), x))

    # plot the optimization path in a 3D graph
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    xvals = np.linspace(-5, 5, 100)
    yvals = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(xvals, yvals)
    Z = X**2 + Y**2

    ax.plot(xs, ys, zs, 'ro-')
    ax.plot_surface(X, Y, Z, cmap='Blues')

    plt.show()

    return x
