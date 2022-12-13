from aocd import get_data
import ast
import functools
data = get_data(year=2022, day=13).split("\n\n")

def compare(left, right):

    if(type(left) == int and type(right) == int):

        if(left < right):
            return 1

        elif(left > right):
            return -1
            
        return 0

    if(type(left) == list and type(right) == list):
        i = -1

        while (True):
            i += 1

            if(i >= len(left) and i >= len(right)):
                return 0

            if(i >= len(left)):
                return 1
                
            if(i >= len(right)):
                return -1
            result = compare(left[i], right[i])

            if(result == 1 or result == -1):
                return result

    if(type(left) == int):
        return compare([left], right)

    if(type(right) == int):
        return compare(left, [right])

packets_list = [[[2]], [[6]]]

for i in range(len(data)):
    line = data[i]
    list_left, list_right = list(map(ast.literal_eval, line.split("\n")))
    packets_list.append(list_left) 
    packets_list.append(list_right)

packets_list.sort(key=functools.cmp_to_key(compare), reverse=True)
print((packets_list.index([[2]]) + 1) * (packets_list.index([[6]]) + 1))