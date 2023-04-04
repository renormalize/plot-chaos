import numpy as np
import matplotlib.pyplot as plt
from sequence import logistic
from plot_params import number_iterations, initial_iterations, x_seed


def plot_logistic():

    from plot_params import r_start, r_end
    
    seq = logistic((r_start+r_end)/2, x_seed, initial_iterations, number_iterations)
    plt.plot(seq, 'o:b')
    plt.show()


def plot_bifurcation():

    from plot_params import r_start, r_end, r_gran_no

    r_vals = np.linspace(r_start, r_end, r_gran_no)
    for r in r_vals:
        sequence = logistic(r, x_seed, initial_iterations, number_iterations)
        r_duplicates = np.empty(number_iterations - initial_iterations)
        r_duplicates.fill(r)
        plt.scatter(r_duplicates, sequence, color='red', s=0.01)
    plt.show()

