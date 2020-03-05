""" bisection search
for finding the square root
"""

# TODO: add plot
# Attribution: based on Guttag "Introduction to Computation and Programming Using Python" pp. 33


def square_root(target: float, max_error = 0.001):
    low: float = 0
    high: float = target
    attempt: float = (low + high) / 2
    while abs(attempt ** 2 - target) > max_error:
        if attempt**2 > target:
            high = attempt
        else:
            low = attempt
        attempt = (low + high)/2
    return attempt

print(square_root(0.5))

# PLOT

# bisection search

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
""" matplotlib backend for interactive use. Tkinter is the Tkinter is Python's
de-facto standard GUI (Graphical User Interface) package.
It is a thin object-oriented layer on top of Tcl/Tk. """

# todo 1: use seaborn
# TODO: make animated

X = 5
FFLOW = 0
FFHIGH = X
LAMBDA = 0.0001
ATTEMPT = (FFLOW + FFHIGH)/2
#print(ATTEMPT**2 - X)
iteration = 0
ITERATIONS = [0] # TODO: convert to numpy
FFLOWS = [FFLOW] # TODO: convert to numpy
FFHIGHS = [FFHIGH] # TODO: convert to numpy
while abs(ATTEMPT**2 - X) > LAMBDA:
    #print(f'error ={ATTEMPT**2 - X}')
    if ATTEMPT ** 2 > X:
        FFHIGH = ATTEMPT
    else:
        FFLOW = ATTEMPT
    FFLOWS.append(FFLOW)
    FFHIGHS.append(FFHIGH)
    iteration += 1
    ITERATIONS.append(iteration)
    ATTEMPT = (FFLOW + FFHIGH)/2
print(ATTEMPT)
print(ATTEMPT**2)
print(f'iterations {ITERATIONS}')
print(FFLOWS)
print(FFHIGHS)
fig, ax = plt.subplots()
plt.plot(ITERATIONS,FFLOWS)
plt.plot(ITERATIONS,FFHIGHS)
plt.show()