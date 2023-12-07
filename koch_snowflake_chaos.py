import numpy as np
import matplotlib.pyplot as plt
import math

# Initial x and y coordinates of the koch snowflake

x = 0
y = 0

# probability of choosing a particular function based on the probability, p
# total of 7 functions
# The probabilities must add up to 1
p = [1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7, 1 / 7]

# Return the initial coordinates of the koch snowflake


def initial_points():
    return x, y


# Transformation functions
#
def f1(x, y):
    x1 = -1 / 6 * x + math.sqrt(3) / 6 * y + 1 / 6
    y1 = -math.sqrt(3) / 6 * x - 1 / 6 * y + math.sqrt(3) / 6
    return x1, y1


def f2(x, y):
    x2 = 1 / 6 * x - math.sqrt(3) / 6 * y + 1 / 6
    y2 = math.sqrt(3) / 6 * x + 1 / 6 * y + math.sqrt(3) / 6
    return x2, y2


def f3(x, y):
    x3 = 1 / 3 * x + 1 / 3
    y3 = 1 / 3 * y + math.sqrt(3) / 3
    return x3, y3


def f4(x, y):
    x4 = 1 / 6 * x + math.sqrt(3) / 6 * y + 2 / 3
    y4 = -math.sqrt(3) / 6 * x + 1 / 6 * y + math.sqrt(3) / 3
    return x4, y4


def f5(x, y):
    x5 = 1 / 2 * x - math.sqrt(3) / 6 * y + 1 / 3
    y5 = math.sqrt(3) / 6 * x + 1 / 2 * y
    return x5, y5


def f6(x, y):
    x6 = -1 / 3 * x + 2 / 3
    y6 = -1 / 3 * y
    return x6, y6


def f7(x, y):
    x7 = 1 / 3 * x + 2 / 3
    y7 = 1 / 3 * y
    return x7, y7


def chaos_game(x, y, p):
    # randomly choosing the transformation function
    # based on the probability p
    r = np.random.choice(["f1", "f2", "f3", "f4", "f5", "f6", "f7"], p=p)
    if r == "f1":
        x, y = f1(x, y)
    elif r == "f2":
        x, y = f2(x, y)
    elif r == "f3":
        x, y = f3(x, y)
    elif r == "f4":
        x, y = f4(x, y)
    elif r == "f5":
        x, y = f5(x, y)
    elif r == "f6":
        x, y = f6(x, y)
    elif r == "f7":
        x, y = f7(x, y)
    return x, y
