# find the sum of all digits that match the next digit in the list.
# The list is circular, so the digit after the last digit is the first digit
# in the list.

def invert_captcha(num_list):
    # nums to sum
    num_to_sum = []
    # extract the first number
    fst = num_list[0]

    # iterate over num_list to check which numbers contribute to sum
    for idx in range(len(num_list)):
        if idx < len(num_list) - 1:
            if num_list[idx] == num_list[idx+1]:
                num_to_sum.append(num_list[idx])
        else:
            if num_list[idx] == fst:
                num_to_sum.append(num_list[idx])

    return sum(num_to_sum)

# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches
test_case1 = [1, 1, 2, 2]
invert_captcha(test_case1)


# 1111 produces 4 because each digit (all 1) matches the next.
test_case2 = [1,1,1,1]
invert_captcha(test_case2)

# 1234 produces 0 because no digit matches the next.
test_case3 = [1,2,3,4]
invert_captcha(test_case3)

# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
test_case4 = [9,1,2,1,2,1,2,9]
invert_captcha(test_case4)

# read captcha input
text_file = open("input_day1.txt", "r")
captcha = text_file.read()


# convert from string to list
captcha_list = []

for digit in captcha:
    if digit.isdigit():
        captcha_list.append(int(digit))

invert_captcha(captcha_list)
