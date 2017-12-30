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

# param values; todo: name the values in the returned data structure for clarity
def get_square_mat_params(start_value):
    nearest_square = math.ceil(math.sqrt(start_value))
    corner_val = nearest_square**2
    return nearest_square, corner_val

# build array and reshape into square matrix
def build_spiral_mat(start_value):
    params = get_square_mat_params(start_value)
    start_array = np.array(build_square_mat_array(start_value, params[1]))
    A = start_array.reshape(params[0], params[0])
    return to_spiral(A)




# get the indices of any number in the spiral matrix
def idx_to_coords(test_value, test_array):
    idx = np.where(test_array == test_value)
    return idx[0][0], idx[1][0]


##### testing
test_value = 277678
center_value = 1

# build spiral array
spiral_array = build_spiral_mat(test_value)

# extract coordinate values for origin and for test value
coord_values_test = idx_to_coords(test_value, spiral_array)
coord_values_origin = idx_to_coords(center_value, spiral_array)

# compute manhattan distance
# the sum of the absolute differences of their Cartesian coordinates.
# the Manhattan distance between x (a,b) and y (c,d) is |a−c|+|b−d|

def compute_manhat_dist(coords1, coords2):
    return abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1])

# testing function
compute_manhat_dist(coord_values_test, coord_values_origin)
