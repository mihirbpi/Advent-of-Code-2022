from aocd import get_data
from math import pow
from numpy import base_repr
data = get_data(year=2022, day=25).split("\n")

def snafu_to_decimal(s):
    result = 0

    for i in range(0, len(s)):

        if(s[i] == "-"):
            result += (-1) * int(pow(5, len(s)-1-i))

        elif(s[i] == "="):
            result += (-2) * int(pow(5, len(s)-1-i))

        else:
            result += int(s[i]) * int(pow(5, len(s)-1-i))

    return result

def decimal_to_snafu(n):
    base_5_list = [int(c) for c in base_repr(n, 5)]
    i = len(base_5_list) - 1

    while (i >= 0):
        curr_digit = base_5_list[i]

        if(not curr_digit in [5, 4, 3]):
            i -= 1
            continue

        if(curr_digit == 5):
            base_5_list[i] = 0

            if (i-1 >= 0):
                base_5_list[i-1] += 1
                i -= 1
            else:
                base_5_list = [1] + base_5_list
                i = 0

        elif(curr_digit == 4):
            base_5_list[i] = "-"
            
            if (i-1 >= 0):
                base_5_list[i-1] += 1
                i -= 1
            else:
                base_5_list = [1] + base_5_list
                i = 0

        elif(curr_digit == 3):
            base_5_list[i] = "="
            
            if (i-1 >= 0):
                base_5_list[i-1] += 1
            else:
                base_5_list = [1] + base_5_list
                i = 0

    return "".join(map(str,base_5_list))

result = 0

for line in data:
    result += snafu_to_decimal(line)

print(decimal_to_snafu(result))