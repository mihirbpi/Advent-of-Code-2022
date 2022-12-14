from aocd import get_data
from collections import defaultdict
data = get_data(year=2022, day=14).split("\n")

def sign(x):

    if (x > 0):
        return 1

    elif (x < 0):
        return -1
    
    return 0

max_y = 0
grid = defaultdict(lambda: ".")
grid[(500,0)] = "+"

for line in data:
    coords_list = line.split(" -> ")

    for i in range(0, len(coords_list)-1):
        start, end = coords_list[i:i+2]
        x_start, y_start = list(map(int, start.split(",")))
        x_end, y_end = list(map(int, end.split(",")))
        max_y = max(max_y, max(y_start, y_end))

        grid[(x_start, y_start)] = "#"

        if(x_start == x_end):
            for y in range(y_start, y_end + sign(y_end-y_start), sign(y_end-y_start)):
                grid[(x_start, y)] = "#"

        elif(y_start == y_end):

            for x in range(x_start, x_end + sign(x_end-x_start), sign(x_end-x_start)):
                grid[(x, y_start)] = "#"

num_sand = 0

while(not grid[(500,0)] == "o"):
    curr_pt = (500,0)
    num_sand += 1

    while (True):
        curr_x, curr_y = curr_pt

        if(grid[(curr_x, curr_y+1)] == "."):

            if(curr_y+1 >= max_y + 2):
                break

            grid[(curr_x, curr_y)] = "."
            grid[(curr_x, curr_y+1)] = "o"
            curr_pt = (curr_x, curr_y+1)

        elif(grid[(curr_x-1, curr_y+1)] == "."):

            if(curr_y+1 >= max_y + 2):
                break

            grid[(curr_x, curr_y)] = "."
            grid[(curr_x-1, curr_y+1)] = "o"
            curr_pt = (curr_x-1, curr_y+1)

        elif(grid[(curr_x+1, curr_y+1)] == "."):

            if(curr_y+1 >= max_y + 2):
                break

            grid[(curr_x, curr_y)] = "."
            grid[(curr_x+1, curr_y+1)] = "o"
            curr_pt = (curr_x+1, curr_y+1)

        else:
            grid[(curr_x, curr_y)] = "o"
            break

print(num_sand)
