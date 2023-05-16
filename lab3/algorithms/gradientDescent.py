import numpy as np


def Decent(R:np.array, functional):
    # print ("Decent")
    antigradient = -functional.grad(R)
    X0 = R
    # print("Decent0")
    Xi = X0 + functional.stepFunc(X0, -antigradient, functional) * functional.getDfDx(X0)
    # print ("Decent1")
    coordinates = np.array(np.array([X0]))
    c = 0
    while (abs(functional.func(Xi) - functional.func(X0)) > functional.tolerance) and (np.linalg.norm(Xi) > functional.tolerance):
        # print("Decent33")
        c+=1
        X0 = Xi
        Xi = X0 + functional.stepFunc(X0,  -antigradient, functional) * functional.getDfDx(X0)
        coordinates = np.append(coordinates, np.array([Xi]), axis=0)
        #print("ook ")
        #print("Xi" , Xi)
    print(c)
    #print("ok")
    return coordinates

