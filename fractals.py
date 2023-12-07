import matplotlib.pyplot as plt
import numpy as np

import math
import importlib

# input the file name
print("------------------------------------")
print("Welcome to the fractal generator")
print("The following are the diagrams available:")
print("Enter the number for the diagram of:")
print("1. Sierpinski Triangle")
print("2. Barnsley Fern")
print("3. Siepinski Triangle using chaos game")
print("4. Barnsley Fern using chaos game")
print("5. Koch Snowflake")
print("------------------------------------")

input_file = int(input("Enter the number: "))

if input_file == 1:
    file_name = "sierpinski_triangle"
if input_file == 2:
    file_name = "barnsley_fern"
if input_file == 3:
    file_name = "sierpinski_triangle_chaos"
if input_file == 4:
    file_name = "barnsley_fern_chaos"
if input_file == 5:
    file_name = "koch_snowflake"


fractal = importlib.import_module(file_name)


# input the number of iterations
n = int(input("Enter the number of iterations: "))

# Iterating the contraction mapping function n times

##### Derministic method #####
# input file does not have the string chaos in it
if "chaos" not in file_name:
    A = fractal.initial_points()
    total_points = np.array(A)

    # append initial points to the total set

    for i in range(n):
        A = fractal.contraction_mapping(A)
        total_points = np.concatenate((total_points, A), axis=0)

    plt.scatter(total_points[:, 0], total_points[:, 1], s=0.5, c="blue")
##### Derministic method #####


##### Chaos game method #####
# input file has the string chaos in it
if "chaos" in file_name:
    x, y = fractal.initial_points()

    total_set_x = []
    total_set_y = []

    for i in range(n):
        x, y = fractal.chaos_game(x, y, fractal.p)
        total_set_x.append(x)
        total_set_y.append(y)

    plt.scatter(total_set_x, total_set_y, s=0.5, c="blue")
##### Chaos game method #####


plt.show()
