from aocd import get_data
from functools import *
data = get_data(year=2022, day=18).split("\n")

filled_cubes = set()
max_coord = -1e99
min_coord = 1e99

for line in data:
    x,y,z = list(map(int,line.split(",")))
    max_coord = max([max_coord, x, y, z])
    min_coord = min([min_coord, x, y, z])
    filled_cubes.add((x,y,z))

@lru_cache(maxsize=None)
def is_exposed(cube):
    stack = [cube]
    visited = set()

    while (len(stack) > 0):
        curr_cube = stack.pop()

        if (curr_cube in filled_cubes):
            continue

        for i in range(3):

            if (not min_coord <= curr_cube[i] <= max_coord):
                return True

        if (curr_cube in visited):
            continue

        x,y,z = curr_cube
        visited.add(curr_cube)
        neighbors = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
 
        for neighbor in neighbors:
            stack.append(neighbor)

    return False

result = 0

for cube in filled_cubes:
    x,y,z = cube
    neighbors = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]
 
    for neighbor in neighbors:

        if(is_exposed(neighbor)):
            result += 1

print(result)
    