import numpy as np

def armijoStep(R, gradient, functional):
    if functional.funcWithStep(R, functional.alpha, -gradient) > functional.func(R):
        functional.alpha *= 0.5
        return functional.alpha
    
    return functional.alpha
