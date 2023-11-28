import math
import numpy as np
import matplotlib.pyplot as plt

# This is the barnsley fern leaf fractal

# Initial coordinates of the barnsley fern leaf: 4 points
A = np.array([[0, 0], [0, 0.16], [0.85, 0.04], [0.2, -0.26]])

# Plotting the initial barnsley fern leaf
plt.scatter(A[:, 0], A[:, 1], s=0.5, c="green")

# Return the initial coordinates of the barnsley fern leaf


def initial_points():
    return A


# Affine transformation functions
#
def f1(A):
    # make a copy of A
    A1 = A.copy()
    for i in range(len(A1)):
        A1[i] = np.matmul(np.matrix([[0, 0], [0, 0.16]]), A1[i])
    return A1


def f2(A):
    # make a copy of A
    A2 = A.copy()
    for i in range(len(A2)):
        A2[i] = np.matmul(np.matrix([[0.85, 0.04], [-0.04, 0.85]]), A2[i]) + [0, 1.6]
    return A2


def f3(A):
    # make a copy of A
    A3 = A.copy()
    for i in range(len(A3)):
        A3[i] = np.matmul(np.matrix([[0.2, -0.26], [0.23, 0.22]]), A3[i]) + [0, 1.6]
    return A3


def f4(A):
    # make a copy of A
    A4 = A.copy()
    for i in range(len(A4)):
        A4[i] = np.matmul(np.matrix([[-0.15, 0.28], [0.26, 0.24]]), A4[i]) + [0, 0.44]
    return A4


# Array of functions
f = [f1, f2, f3, f4]


def contraction_mapping(A):
    # Applying affine transformation f1 to all points of A
    A1 = f1(A)
    # Applying affine transformation f2 to all points of A
    A2 = f2(A)
    # Applying affine transformation f3 to all points of A
    A3 = f3(A)
    # Applying affine transformation f4 to all points of A
    A4 = f4(A)

    # Combining all points of A1, A2, A3, A4
    A = np.concatenate((A1, A2, A3, A4), axis=0)

    return A
