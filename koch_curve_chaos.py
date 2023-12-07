import numpy as np
import matplotlib.pyplot as plt
import math

# Initial x and y coordinates of the koch curve

x = 0
y = 0

# probability of choosing a particular function based on the probability, p
# total of 4 functions
# The probabilities must add up to 1
p = [1/4, 1/4, 1/4, 1/4]

# Return the initial coordinates of the koch curve

def initial_points():
    return x, y

# Transformation functions

def f1(x, y):
    x1 = 1/3 * x
    y1 = 1/3 * y
    return x1, y1

def f2(x, y):
    x2 = 1/6 * x - math.sqrt(3)/6 * y + 1/3
    y2 = math.sqrt(3)/6 * x + 1/6 * y
    return x2, y2

def f3(x, y):
    x3 = 1/6 * x + math.sqrt(3)/6 * y + 1/2
    y3 = -math.sqrt(3)/6 * x + 1/6 * y + math.sqrt(3)/6
    return x3, y3

def f4(x, y):
    x4 = 1/3 * x + 2/3
    y4 = 1/3 * y
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
