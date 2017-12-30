# --- Day 4: High-Entropy Passphrases part 2 ---
import numpy as np
import pandas as pd
import os

# For added security, yet another system policy has been put in place.
# Now, a valid passphrase must contain no two words that are anagrams
# of each other - that is, a passphrase is invalid if any word's letters
# can be rearranged to form any other word in the passphrase.

# function to check if two strings are an anagrams of each other
def check_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

s1 = 'abcde'
s2 = 'fghij'
s3 = 'oiii'
s4 = 'iiio'

check_anagram(s1, s2)
check_anagram(s3, s4)

# function to check a full passphrase
def check_phrase_valid(passphrases):
    for phrase in passphrases:
        test_phrases = [s for s in passphrases if s != phrase]
        if len(phrase) == 1:
            return True
        # check the test phrase against the other phrases
        for comp_phrase in test_phrases:
            if check_anagram(phrase, comp_phrase):
                return False
    return True

test_phrase = [s1, s2, s3, s4]
check_phrase_valid(test_phrase)

test_phrase2 = ['a', 'ab', 'abc', 'abd', 'abf', 'abj']
check_phrase_valid(test_phrase2)

test_phrase3 = ['abcde', 'fghij']
check_phrase_valid(test_phrase3)


return True

# function to iterate over list of Passphrases
# stores the number of valid Passphrases
def count_valid_passphrases(list_of_passphrases):
    n_valid_phrases = 0
    for phrase in list_of_passphrases:
        if check_phrase_valid(phrase):
            n_valid_phrases += 1
    return n_valid_phrases

test_phrases_list = [test_phrase, test_phrase2, test_phrase3]
count_valid_passphrases(test_phrases_list)

#### deploy

#### read data
df = pd.read_table('day4_input.txt', sep='\n', header=None)

## clean up data
passphrases = list(df[0])
list_of_passphrases = []
for phrase in passphrases:
    list_of_passphrases.append(phrase.split())

count_valid_passphrases(list_of_passphrases)
