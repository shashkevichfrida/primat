import numpy as np

def unimodal(R: np.array, gradient: np.array,functional):
    alpha = 0
    step = functional.tolerance
    while (1):
        #print("whl")
        if (functional.funcWithStep(R, alpha - step, gradient) > functional.funcWithStep(R, alpha, gradient)) and ((functional.funcWithStep(R, alpha, gradient) < functional.funcWithStep(R, alpha + step, gradient))):
            break
        elif (functional.funcWithStep(R, alpha - step, gradient) > functional.funcWithStep(R, alpha + step, gradient)):
            alpha += step/2
        elif (alpha > -step/2):
            alpha -= step/2
    #print("UnimodalEnd ", alpha)
    return alpha

def Dihotomy(a0, b0, R: np.array,functional):
    lk = 0
    mk = 0
    delta = 0.5 * functional.tolerance
    ak = a0
    bk = b0
    antiGrad = -functional.grad(R)
    while(1):
        lk = (ak + bk - delta) / 2
        mk = (ak + bk + delta) / 2
     #   print ("lk", lk)
     #   print ("mk", mk)

        if ( functional.funcWithStep(R, lk, antiGrad) <= functional.funcWithStep(R, mk, antiGrad)):
            bk = mk
        else:
            ak = lk
        if ((bk - ak) >= functional.tolerance): break

    xMin = (ak + bk) / 2;
    #print("xMin: ", xMin)
    #print(" End Dihotomy")

    return xMin

def dihotomyStep(R, gradient, functional):
    u = unimodal(R, -gradient, functional)
    #print(f'Unimodal = {u}')
    return Dihotomy(u - 0.025, u + 0.025, R, functional)

def dihotomyStep2(R, gradient, functional):
    u = unimodal(R, -gradient, functional)
    #print(f'Unimodal = {u}')
    return Dihotomy(u - functional.tolerance, u + functional.tolerance, R, functional)