# --- Day 6: Memory Reallocation ---

# A debugger program here is having an issue: it is trying to
# repair a memory reallocation routine, but it keeps getting
# stuck in an infinite loop.
#
# In this area, there are sixteen memory banks; each memory bank
# can hold any number of blocks. The goal of the reallocation
# routine is to balance the blocks between the memory banks.

# The reallocation routine operates in cycles. In each cycle,
# it finds the memory bank with the most blocks (ties won by the
# lowest-numbered memory bank) and redistributes those blocks among
# the banks. To do this, it removes all of the blocks from the selected
# bank, then moves to the next (by index) memory bank and inserts one
# of the blocks. It continues doing this until it runs out of blocks;
# if it reaches the last memory bank, it wraps around to the first one.

# The debugger would like to know how many redistributions can
# be done before a blocks-in-banks configuration is produced that
# has been seen before.

import numpy as np

def check_memory(test_array, memory):
    # reverse memory so we check most recent values first
    memory_size = len(memory) - 1
    in_memory = False
    count = 0
    while count < memory_size and in_memory == False:
        if np.array_equal(test_array, ltm[count]):
            in_memory = True
        count +=1
    return in_memory

def redist_blocks(current_array):
    current_bank_idx = current_array.argmax()
    blocks_to_dist = current_array[current_bank_idx]
    last_bank_idx = len(current_array) - 1
    current_array[current_bank_idx] = 0
    count = 0
    while blocks_to_dist > 0:
        # handle the case of arriving at the end of the memory banks
        if current_bank_idx + 1 > last_bank_idx:
            current_bank_idx = 0
            current_array[current_bank_idx] += 1
            blocks_to_dist -= 1
            count += 1
        else:
            current_bank_idx += 1
            current_array[current_bank_idx] += 1
            blocks_to_dist -= 1
            count += 1

    return(current_array)

def update_memory(test_bank, long_term_memory, next_open_slot_idx):
    long_term_memory[next_open_slot_idx] = test_bank
    return long_term_memory

def check_bank(test_bank, long_term_memory):
    # store initial config in long_term_memory
    seen_before_global = False
    current_config = test_bank
    memory_idx = 0 # hacky way to deal with initial state of memory check
    size_of_memory = len(long_term_memory)

    # start while loop after running the initialization steps
    while seen_before_global == False and memory_idx < size_of_memory:
        seen_before_global = check_memory(current_config, long_term_memory)
        long_term_memory = update_memory(current_config, long_term_memory, memory_idx)
        current_config = redist_blocks(current_config)
        memory_idx +=1

    return memory_idx - 1


#### Testing
test_bank = np.array([0,2,7,0])
ltm = np.zeros([10,4])
check_bank(test_bank, ltm)

#### Deploy
memory_bank = np.array([0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11])
ltm = np.zeros([10000,len(memory_bank)])

# to do need to make this code more efficient
# i think the best place to start is the search algorithm
# right now it just naively searches from the first to the last item stored in memory

#check_bank(memory_bank, ltm)
