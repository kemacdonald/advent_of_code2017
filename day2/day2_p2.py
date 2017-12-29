import pandas as pd
import numpy as np
import sys,os

def process_row_list_p2(row_list):
    '''
    finds the only two numbers in each row where one evenly divides the other
    that is, where the result of the division operation is a whole number
    '''
    for test_num in row_list:
        # remove test_num from test set
        test_set = row_list[row_list != test_num]

        # test if set contains number that is evenly divisible
        test_result = test_set[test_num % test_set == 0]

        if len(test_result > 0):
            return test_num // test_result[0]

def even_div(np_array):
    '''
    For each row, calls the process_row_list function,
    then computes the sum of all of these numbers.
    '''
    nums_to_sum = []
    for row_idx in range(0, np_array.shape[0]):
        nums_to_sum.append(process_row_list_p2(np_array[row_idx]))

    return sum(nums_to_sum)

##### test case
test1 = np.array([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
process_row_list_p2(test1[2])

even_div(test1)

#### deploy

# load data
df = np.fromfile('day2_input.txt', sep='\t', dtype=int).reshape(16,16)

# explore data structure
df.ndim
df.shape

# compute compute the checksum
even_div(df)
