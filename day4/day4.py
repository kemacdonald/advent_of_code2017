# --- Day 4: High-Entropy Passphrases part 1 ---
import numpy as np
import pandas as pd
import os

# A new system policy has been put in place that
# requires all accounts to use a passphrase instead of
# simply a password. A passphrase consists of a series of words
# (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.

# check if the length of the list of strings is equal to the "set"
# set returns the list without duplicates
def check_passphrase(passphrase):
    return len(passphrase) == len(set(passphrase))

# function to iterate over list of Passphrases
# stores the number of valid Passphrases
def count_valid_passphrases(list_of_passphrases):
    n_valid_phrases = 0
    for phrase in list_of_passphrases:
        if check_passphrase(phrase):
            n_valid_phrases += 1
    return n_valid_phrases


#### testing
test = ['aa', 'bb', 'cc', 'dd', 'ee']
test2 = ['aa', 'bb', 'cc', 'dd', 'aa']
test3 = ['aa', 'bb', 'cc', 'dd', 'aaa']
test_list = [test, test2, test3]

count_valid_passphrases(test_list)

#### read data
df = pd.read_table('day4_input.txt', sep='\n', header=None)

## clean up data
passphrases = list(df[0])
list_of_passphrases = []
for phrase in passphrases:
    list_of_passphrases.append(phrase.split())

# get the number of valid Passphrases
count_valid_passphrases(list_of_passphrases)
