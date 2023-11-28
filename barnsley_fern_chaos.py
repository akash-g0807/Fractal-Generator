import numpy as np
import matplotlib.pyplot as plt
import math

# initial x and y coordinates of the barnsley fern leaf
x = 0
y = 0

# probability of choosing a particular function
# The probabilities must add up to 1
p = [0.01, 0.85, 0.07, 0.07]

# Return the initial coordinates of the barnsley fern leaf


def initial_points():
    return x, y


# Transformation functions


def f1(x, y):
    x1 = 0
    y1 = 0.16 * y
    return x1, y1


def f2(x, y):
    x2 = 0.85 * x + 0.04 * y
    y2 = -0.04 * x + 0.85 * y + 1.6
    return x2, y2


def f3(x, y):
    x3 = 0.2 * x - 0.26 * y
    y3 = 0.23 * x + 0.22 * y + 1.6
    return x3, y3


def f4(x, y):
    x4 = -0.15 * x + 0.28 * y
    y4 = 0.26 * x + 0.24 * y + 0.44
    return x4, y4


def chaos_game(x, y, p):
    # randomly choosing the transformation function
    # based on the probability p
    r = np.random.choice(["f1", "f2", "f3", "f4"], p=p)
    if r == "f1":
        x, y = f1(x, y)
    elif r == "f2":
        x, y = f2(x, y)
    elif r == "f3":
        x, y = f3(x, y)
    elif r == "f4":
        x, y = f4(x, y)
    return x, y
