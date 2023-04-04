import numpy as np


def logistic_map(r: np.float64, x: np.float64):
    return r*x*(1. - x)


# generates the logistic map sequence for N iterations
def logistic_iter(r: np.float64, x_0: np.float64, N: int):
    x = np.zeros(N+1)
    x[0] = x_0
    for i in range(N):
        x[i+1] = logistic_map(r, x[i])
    return x



# r         : the growth rate
# x_0       : the inital seed
# init_iter : the number of iterations which encapsulate the transient behaviour
# con_iter  : the number of iterations which are to be considered
def logistic(r: np.float64, x_0: np.float64, init_iter: int, con_iter: int):
    # the value of the first iteration that is considered is stored in init_iter+1
    return logistic_iter(r, x_0, init_iter + con_iter)[init_iter+1:]


# r         : the growth rate
# x_0       : the inital seed
# init_iter : the number of iterations which encapsulate the transient behaviour
# con_iter  : the number of iterations which are to be considered
def liapunov(r: np.float64, x_0: np.float64, init_iter: int, con_iter: int):
    x_i = x_0
    for i in np.arange(0, init_iter):
       x_i = logistic_map(r, x_i)
    
    sum = np.float64(0.)
    for i in np.arange(0, con_iter):
       x_i = logistic_map(r, x_i)
       sum += np.log(np.abs(r - 2*r*x_i))
    
    return sum/con_iter

