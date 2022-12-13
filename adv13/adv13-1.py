from aocd import get_data
import ast
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

indices_sum = 0

for i in range(len(data)):
    line = data[i]
    list_left, list_right = list(map(ast.literal_eval, line.split("\n")))

    if(compare(list_left, list_right) > 0):
        indices_sum += i + 1

print(indices_sum) 

    
                
            
