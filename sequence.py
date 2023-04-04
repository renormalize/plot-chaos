import numpy as np

def logistic_iter(r: np.float64, x_0: np.float64, N: int):
    x = np.zeros(N)
    x[0] = x_0
    for i in range(N-1):
        x[i+1] = r*x[i]*(1. - x[i])
    return x

# r         : the growth rate
# x_0       : the inital seed
# init_iter : index before which the transient behaviour is discarded
# N         : the number of iterations
def logistic(r: np.float64, x_0: np.float64, init_iter : int, N_iter: int):
    # the value of the init_iter-th iteration is stored in init_iter (0 indexed)
    return logistic_iter(r, x_0, N_iter)[init_iter:]