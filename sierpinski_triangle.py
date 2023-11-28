import math
import numpy as np
import matplotlib.pyplot as plt

# Initial triangle coordinates A of equilateral Triangle
A = np.array([[0, 0], [0.5, math.sqrt(3) / 2], [1, 0]])

# initial array of all points that can be dynamically changed
# of the triangle

# Plotting the initial triangle
plt.scatter(A[:, 0], A[:, 1], s=0.3, c="red")

# Initial triangle coordinates A of equilateral Triangle
def initial_triangle():
    return A

# Affine transformation functions
def f1(A):
    # make a copy of A
    A1 = A.copy()
    for i in range(len(A1)):
        A1[i] = A1[i] / 2
    return A1


def f2(A):
    # make a copy of A
    A2 = A.copy()
    for i in range(len(A2)):
        A2[i] = (A2[i] + [1, 0]) / 2
    return A2


def f3(A):
    # make a copy of A
    A3 = A.copy()
    for i in range(len(A3)):
        A3[i] = (A3[i] + [0.5, math.sqrt(3) / 2]) / 2
    return A3



# Array of functions
f = [f1, f2, f3]

def contraction_mapping(A):
    # Applying affine transformation f1 to all points of A
    A1 = f1(A)
    print(A1)
    # Applying affine transformation f2 to all points of A
    A2 = f2(A)
    # Applying affine transformation f3 to all points of A
    A3 = f3(A)

    # Combining all points of A1, A2, A3
    A = np.concatenate((A1, A2, A3), axis=0)

    # plotting the points
    plt.scatter(A[:, 0], A[:, 1], s=0.3, c="red")
    return A
