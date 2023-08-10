# main file to generate the bifurcation diagrams, and the cobweb diagrams
from plot import *

print('Enter 1 for Bifurcation Diagram for the Logistic Map')
print('Enter 2 for Liapunov Exponent as a function of growth parameter for the Logistic Map')
print('Enter 3 for Cobweb Diagram for the Logistic map')
print('Change the required parameters in the respective parameter.py file')

not_valid_input = True
option = -1 # Option holds which plot the user requires

while not_valid_input:
    option = int(input())
    if option in range(4):
        break
    print('Enter a valid input')

if option == 1:
    plot_bifurcation()
elif option == 2:
    plot_liapunov()
else:
    plot_cobweb()
