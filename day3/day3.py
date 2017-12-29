# --- Day 3: Spiral Memory --- #

# Each square on the grid is allocated in a spiral pattern starting
# at a location marked 1 and then counting up while spiraling outward.

# How many steps are required to carry the data from the square
# identified in your puzzle input all the way to the access port?

# Set up
import pandas as pd
import numpy as np
import math


def to_spiral(A):
    A = np.array(A)
    B = np.empty_like(A)
    B.flat[base_spiral(*A.shape)] = A.flat
    return B

def spiral_ccw(A):
    A = np.array(A)
    out = []
    while(A.size):
        out.append(A[0][::-1])    # first row reversed
        A = A[1:][::-1].T         # cut off first row and rotate clockwise
    return np.concatenate(out)

def base_spiral(nrow, ncol):
    return spiral_ccw(np.arange(nrow*ncol).reshape(nrow,ncol))[::-1]

# find carteisan coordinate of a given number (e.g., 277678)

# figure out the dimensions of the matrix based on the nearest dimensions
# that would make a pretty square matrix

# function to build array with empty values to complete the square matrix
def build_square_mat_array(start_value, corner_value):
    square_mat_array = list(range(1, 1 + start_value))
    zeros_to_add = [0] * (corner_value - start_value)

    for zero in zeros_to_add:
        square_mat_array.append(zero)

    return square_mat_array

# param values
def get_square_mat_params(start_value):
    nearest_square = math.ceil(math.sqrt(start_value))
    corner_val = nearest_square**2
    shape_param = int(math.sqrt(corner_val))

    return nearest_square, corner_val, shape_param

get_square_mat_params(11)

# build array
tmp = np.array(build_square_mat_array(11, 16))

# reshape into square matrix
A = tmp.reshape(shape_param,shape_param)

# spiralize it
to_spiral(A)

# compute manhattan distance
# the sum of the absolute differences of their Cartesian coordinates.
# the Manhattan distance between x (a,b) and y (c,d) is |a−c|+|b−d|

def compute_manhat_dist(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])


# testing function
origin = [0,0]
test_point = [0,-2]

compute_manhat_dist(origin, test_point)
