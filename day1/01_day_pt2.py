# Now, instead of considering the next digit, it wants you to consider
# the digit halfway around the circular list. That is, if your list contains
# 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward
# matches it. Fortunately, your list has an even number of elements.

def invert_captcha_p2(num_list):
    # nums to sum
    num_to_sum = []
    # extract the first number
    fst = num_list[0]
    # extract the halfway point of num_list
    midpoint = len(num_list) // 2

    # iterate over num_list to check which numbers contribute to sum
    for idx in range(midpoint):
        if num_list[idx] == num_list[idx + midpoint]:
            num_to_sum.append(num_list[idx])
            num_to_sum.append(num_list[idx + midpoint])

    return sum(num_to_sum)

### Test cases

# 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
test1 = [1,2,1,2]
invert_captcha_p2(test1)
# 1221 produces 0, because every comparison is between a 1 and a 2.
test2 = [1,2,2,1]
invert_captcha_p2(test2)

# 123425 produces 4, because both 2s match each other, but no other digit has a match.
test3 = [1,2,3,4,2,5]
invert_captcha_p2(test3)
# 123123 produces 12.
test4 = [1,2,3,1,2,3]
invert_captcha_p2(test4)
# 12131415 produces 4.
test5 = [1,2,1,3,1,4,1,5]
invert_captcha_p2(test5)

### Deploy

# read captcha input
text_file = open("input_day1.txt", "r")
captcha = text_file.read()

# convert from string to list
captcha_list = []

for digit in captcha:
    if digit.isdigit():
        captcha_list.append(int(digit))

invert_captcha_p2(captcha_list)
