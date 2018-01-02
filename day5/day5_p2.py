# --- Day 5: A Maze of Twisty Trampolines, All Alike Part 2 ---

# The message includes a list of the offsets for each jump.
# Jumps are relative: -1 moves to the previous instruction,
# and 2 skips the next one. Start at the first instruction in the list.
# The goal is to follow the jumps until one leads outside the list.

# Now, the jumps are even stranger: after each jump,
# if the offset was three or more, instead decrease it by 1.
# Otherwise, increase it by 1 as before.

import os
import numpy as np
import time
start_time = time.time()

# need to keep track of both value and idx
# let's just try it with a for loop
# these are basically init values for the algorithm
def get_next_vals(current_array, current_step_size, current_idx):
    '''
    Given the current value and location in list
    Returns the next location and value
    '''
    d = {'next_idx': current_step_size + current_idx, 'next_value': current_array[current_step_size + current_idx]}
    return d

# here we modify the update array function to handle the new jump effect
def update_array(current_array, current_idx):
    '''
    Updates the instructions array by adding 1 to the current location
    after visiting it
    '''
    if current_array[current_idx] >= 3:
        current_array[current_idx] = current_array[current_idx] -1
    else:
        current_array[current_idx] = current_array[current_idx] + 1
    return current_array

# ending condition is when the next location is > len(test_list)
def init_jump(test_array, start_idx):
    count = 1
    projected_location = 0
    current_idx = start_idx
    init_step_size = test_array[start_idx]
    exit_length = len(test_array)
    while (projected_location < exit_length):
        # get current values if on the first loop use initial values
        # otherwise we use the values returned from the get_next_vals function
        if count == 1:
            current_step_size = init_step_size
            test_array = update_array(test_array, current_idx)
        else:
            current_step_size = next_vals['next_value']
            current_idx = next_vals['next_idx']
            test_array = update_array(test_array, current_idx)
        # get next values
        next_vals = get_next_vals(test_array, current_step_size, current_idx)
        # update the array
        count = count + 1
        projected_location = next_vals['next_value'] + next_vals['next_idx']

        #print(next_vals, test_array, projected_location, count)
    return count

## testing
blah = [0, 3, 0, 1, -3]
start_idx = 0
# print(init_jump(blah, start_idx))

### Deploy

# read input
text_file = open("day5_input.txt", "r")
jumps = text_file.readlines()
jumps = [x.strip() for x in jumps]
jumps = [int(x) for x in jumps]
start_idx = 0

print("Number of jumps is: " + str(init_jump(jumps, start_idx)))

#### pring timing of program executiong
print("--- %s seconds ---" % (time.time() - start_time))
