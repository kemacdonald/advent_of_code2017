import pandas as pd
import numpy as np
import sys,os

#### write functions

# function that returns difference between smallest and largest values in a row
# stored as a list
def process_row_list(row_list):
    '''
    For one row, finds the smallest and largest numbers
    then computes the difference between those numbers
    '''
    row_list.sort()
    # extract last number of sorted list (i.e., the smallest)
    largest_num = row_list[len(row_list) - 1]
    # extract first number of sorted list (i.e., the smallest)
    smallest_num = row_list[0]
    # compute the difference and return
    return largest_num - smallest_num

def compute_check_sum(df):
    '''
    For each row, calls the process_row_list function
    then computes the sum of all of these numbers.
    '''
    nums_to_sum = []
    for row_idx in range(0, df.shape[0]):
        nums_to_sum.append(process_row_list(df[row_idx]))

    return sum(nums_to_sum)



##### test case
test1 = np.array([[5,1,9,5], [7, 5, 3], [2, 4, 6, 8]])

compute_check_sum(test1)

##### Deploy

# load data
os.chdir('day2')
df = np.fromfile('day2_input.txt', sep='\t', dtype=int).reshape(16,16)

# explore data structure
df.ndim
df.shape

# compute compute the checksum
compute_check_sum(df)
