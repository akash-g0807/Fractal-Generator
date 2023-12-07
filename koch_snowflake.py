import math
import numpy as np
import matplotlib.pyplot as plt

# Initial coordinates of the Koch snowflake
A = np.array([[0.5, math.sqrt(3) / 2]])

# initial array of all points that can be dynamically changed
# of the Koch snowflake
# Plotting the initial snowflake
plt.scatter(A[:, 0], A[:, 1], s=0.5, c="red")

def initial_points():
    return A


# Affine transformation functions

def f1(A):
    # make a copy of A
    A1 = A.copy()
    for i in range(len(A1)):
        A1[i] = np.matmul(np.matrix([[-1/6, math.sqrt(3)/6], [-math.sqrt(3)/6, -1/6]]), A1[i]) + np.array([1/6, math.sqrt(3)/6])
    return A1

def f2(A):
    # make a copy of A
    A2 = A.copy()
    for i in range(len(A2)):
        A2[i] = np.matmul(np.matrix([[1/6, -math.sqrt(3)/6], [math.sqrt(3)/6, 1/6]]), A2[i]) + np.array([1/6, math.sqrt(3)/6])
    return A2

def f3(A):
    # make a copy of A
    A3 = A.copy()
    for i in range(len(A3)):
        A3[i] = np.matmul(np.matrix([[1/3, 0], [0, 1/3]]), A3[i]) + np.array([1/3, math.sqrt(3)/3])
    return A3

def f4(A):
    # make a copy of A
    A4 = A.copy()
    for i in range(len(A4)):
        A4[i] = np.matmul(np.matrix([[1/6, math.sqrt(3)/6], [-math.sqrt(3)/6, 1/6]]), A4[i]) + np.array([2/3, math.sqrt(3)/3])
    return A4

def f5(A):
    # make a copy of A
    A5 = A.copy()
    for i in range(len(A5)):
        A5[i] = np.matmul(np.matrix([[1/2, -math.sqrt(3)/6], [math.sqrt(3)/6, 1/2]]), A5[i]) + np.array([1/3, 0])
    return A5

def f6(A):
    # make a copy of A
    A6 = A.copy()
    for i in range(len(A6)):
        A6[i] = np.matmul(np.matrix([[-1/3, 0], [0, -1/3]]), A6[i]) + np.array([2/3, 0])
    return A6

def f7(A):
    # make a copy of A
    A7 = A.copy()
    for i in range(len(A7)):
        A7[i] = np.matmul(np.matrix([[1/3, 0], [0, 1/3]]), A7[i]) + np.array([2/3, 0])
    return A7

# Array of functions
f = [f1, f2, f3, f4, f5, f6, f7]

def contraction_mapping(A):

    # Applying affine transformation f1 to all points of A
    A1 = f1(A)
    # Applying affine transformation f2 to all points of A
    A2 = f2(A)
    # Applying affine transformation f3 to all points of A
    A3 = f3(A)
    # Applying affine transformation f4 to all points of A
    A4 = f4(A)
    # Applying affine transformation f5 to all points of A
    A5 = f5(A)
    # Applying affine transformation f6 to all points of A
    A6 = f6(A)
    # Applying affine transformation f7 to all points of A
    A7 = f7(A)

    # Combining all points of A1, A2, A3, A4, A5, A6, A7
    A = np.concatenate((A1, A2, A3, A4, A5, A6, A7), axis=0)
    return A
