import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from cycler import cycler
from matplotlib import collections as mc
from sequence import *


# Plots the Logistic Map sequence for the parameters set in bifurcation_params.py
def plot_logistic():

    from params import bifurcation_params as b
    
    seq = logistic((b.r_start + b.r_end)/2, b.x_seed, b.initial_iterations, b.consider_iterations)
    plt.plot(seq, 'o:b')
    plt.show()


# Plots the Bifurcation diagram for the Logistic map for the parameters set in bifurcation_params.py
def plot_bifurcation():

    from params import bifurcation_params as b

    plt.xlabel('r')
    plt.ylabel('x')
    plt.title(f'\nBifurcation diagram of the logistic map\n{b.r_start} < r < {b.r_end}\nx_0 = {b.x_seed}\n')

    r_vals = np.linspace(b.r_start, b.r_end, b.r_gran_no)
    for r in r_vals:
        sequence = logistic(r, b.x_seed, b.initial_iterations, b.consider_iterations)
        r_duplicates = np.empty(b.consider_iterations)
        r_duplicates.fill(r)
        plt.scatter(r_duplicates, sequence, color='red', s=0.01)

    plt.xlim((b.r_start, b.r_end))
    plt.ylim((0.0, 1.0))
    plt.show()


# Plots the Liapunov Exponent for the Logistic map as a function of growth rate for the parameters 
# set in bifurcation_params.py
def plot_liapunov():
    
    from params import liapunov_params as l

    plt.xlabel('r')
    plt.ylabel('Liapunov Exponent')
    plt.title('Liapunov exponent as a function of growth parameter r')

    r_vals = np.linspace(l.r_start, l.r_end, num=l.r_gran_no)
    for r in r_vals:
        exponent = liapunov(r, l.x_seed, l.initial_iterations, l.consider_iterations)
        plt.scatter(r, exponent, color='black', s=0.1)
        plt.scatter(r, (0.0), color='red', s=0.01)
    
    plt.xlim(l.r_start, l.r_end)
    plt.ylim(-2.0, 1.0)
    plt.show()


# Plots the Cobweb diagram for the Logistic map for the parameters set in bifurcation_params.py
def plot_cobweb():

    from params import cobweb_params as c

    mpl.rcParams['axes.prop_cycle'] = cycler(color=['g'])

    fig, ax = plt.subplots()
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 1.0)
    ax.set_aspect(1)
    red_patch = mpatches.Patch(color='red', label='y = x')
    blue_patch = mpatches.Patch(color='blue', label='Logistic Map')
    green_patch = mpatches.Patch(color='green', label='Cobweb')
    ax.legend(handles=[red_patch, blue_patch, green_patch])
    plt.xlabel('ith iteration')
    plt.ylabel('i+1th iteration')
    plt.title(f'\nCobweb diagram from the growth parameter {c.r}\n')

    y_eqs_x = np.linspace(0.0, 1.0, c.number_iterations*10)
    ax.scatter(y_eqs_x, y_eqs_x, color='red', s = 0.05)

    mapVectorized = np.vectorize(logistic_map)
    r_duplicates = np.empty(c.number_iterations*10)
    r_duplicates.fill(c.r)
    logistic_parabola = mapVectorized(r_duplicates, y_eqs_x)
    ax.scatter(y_eqs_x, logistic_parabola, color='blue', s=0.05)

    sequence = logistic_iter(c.r, c.x_seed, c.number_iterations)
    # horizontal then vertical
    lines = []
    lines.append([[sequence[0],0], [sequence[0], sequence[0]]])
    for i in range(c.number_iterations-1):
        lines.append([[sequence[i], sequence[i]], [sequence[i], sequence[i+1]]])
        lines.append([[sequence[i], sequence[i+1]], [sequence[i+1], sequence[i+1]]])
        
    lc = mc.LineCollection(lines, linewidth=0.1)
    ax.add_collection(lc)

    plt.show()
