# Default parameters for the liapunov exponent diagram
import numpy as np

# inital_iterations     : the number of iterations which encapsulate the transient behaviour
initial_iterations = 2000
# consider_iterations   : the number of iterations which are to be considered
consider_iterations = 30000
# r_start               : minimum growth rate
r_start = np.float64(3.0)
# r_end                 : maximum growth rate
r_end = np.float64(4.0)
# r_gran_no             : the granularity of r with which r is changed
r_gran_no = 5000
# x_seed                : the inital seed
x_seed = np.float64(0.7)
