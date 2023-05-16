import numpy as np

def conjugate_grad(R, functiomal):
    coordinates = np.array(np.array([R]))
    #coordinates = np.append(coordinates, R)
    grad = functiomal.grad(R)
    pk = -grad
    Xi = R
    gradNorm = np.amax(np.abs(grad))
    c = 0
    while gradNorm > functiomal.tolerance:
        alphaK = - np.dot(grad, pk) / np.dot(np.dot(pk, functiomal.grad(Xi).T), pk)
        Xi = Xi + alphaK * pk
        gradK = functiomal.grad(Xi)
        betaK = max(0, np.dot(gradK, gradK)/ np.dot(grad, grad))
        pk = -gradK * betaK * pk
        grad = gradK
        gradNorm = np.amax(np.abs(grad))
        coordinates = np.append(coordinates, np.array([Xi]), axis=0)
        c+=1

    print("c ", c)
    
    return coordinates

