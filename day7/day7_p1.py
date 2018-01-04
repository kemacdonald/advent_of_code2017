# --- Day 7: Recursive Circus ---

import numpy as np
import pandas as pd
import re

def process_program(program_info_string):
    program_info_list = program_info_string.split()
    weight = program_info_list[1].strip('()')
    if '->' in program_info_string:
        programs_above = program_info_string[program_info_string.find('>')+1:].strip().split()
    else:
        programs_above = 'None'
    return weight, programs_above

# read in data
f = open('day7_input.txt', 'r')
data_raw = f.read()
f.close()

# clean it up
data = data_raw.split(sep='\n')

# subset data for testing
test_data = data[0:4]
d = {}

# process each program to extract the data we want
for program in test_data:
    program_name = program.split()[0]
    d[program_name] = process_program(program)

# find the bottom program in the tree
# to do this, we just need to find the program that is
# not in any of the "above programs"

# build list of 
list(d.values())[0][1]
