import numpy as np
import matplotlib.pyplot as plt
import math

# Initial x and y coordinates of the triangle

x = 0
y = 0

# probability of choosing a particular function
# The probabilities must add up to 1
p = [0.33, 0.33, 0.34]

# Return the initial coordinates of the triangle
# as a numpy array


def initial_points():
    return x, y


# Transformation functions
#
def f1(x, y):
    x1 = x / 2
    y1 = y / 2
    return x1, y1


def f2(x, y):
    x2 = (x + 1) / 2
    y2 = y / 2
    return x2, y2


def f3(x, y):
    x3 = (x + 0.5) / 2
    y3 = (y + math.sqrt(3) / 2) / 2
    return x3, y3


def chaos_game(x, y, p):
    # randomly choosing the transformation function
    # based on the probability p
    r = np.random.choice(["f1", "f2", "f3"], p=p)
    if r == "f1":
        x, y = f1(x, y)
    elif r == "f2":
        x, y = f2(x, y)
    elif r == "f3":
        x, y = f3(x, y)
    return x, y
