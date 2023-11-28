
import matplotlib.pyplot as plt
import numpy as np

import math
import importlib
# Sierpinski Triangle using deterministic method usinf affine transformations
# input the file name

print("------------------------------------")
print("Welcome to the fractal generator")
print("The following are the diagrams available:")
print("Enter the number for the diagram of:")
print("1. Sierpinski Triangle")

print("------------------------------------")

input_file = int(input("Enter the number: "))

if input_file == 1:
    file_name = "sierpinski_triangle"


fractal = importlib.import_module(file_name)


# input the number of iterations
n = int(input("Enter the number of iterations: "))

# Iterating the contraction mapping function n times

A = fractal.initial_triangle()

for i in range(n):
    A = fractal.contraction_mapping(A)

print(A)

# Getting the x and y coordinates of all points
x = A[:, 0]
y = A[:, 1]
print(x)
print(y)


plt.show()
