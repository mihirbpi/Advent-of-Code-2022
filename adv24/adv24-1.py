from aocd import get_data
from math import lcm
from heapq import heapify, heappop, heappush

data = get_data(year=2022, day=24).split("\n")

height, width = len(data), len(data[0])
start = (0,1)
orig_state = (0, start)
end = (height-1, width-2)
period = lcm(height-2, width-2)
blizzards = set()
walls = set()

for col in range(width):

    if(col != 1):
        walls.add((0, col))

    if (col != width-2):
        walls.add((height-1, col))

for row in range(height):
    walls.add((row, 0))
    walls.add((row, width-1))

for row in range(height):

       for col in range(width):

            if(data[row][col] in ["^", ">", "<", "v"]):
                blizzards.add((data[row][col], row, col))

blizzard_states = [None] * period
blizzard_states[0] = blizzards

for t in range(1, period):
    new_blizzards = set()

    for blizzard in blizzards:
        dir, row, col = blizzard

        if (dir == "^"):
            curr_row, curr_col = (row - 1) % height, col

            while ((curr_row, curr_col) in walls):
                curr_row = (curr_row - 1) % height

        elif (dir == "v"):
            curr_row, curr_col = (row + 1) % height, col

            while ((curr_row, curr_col) in walls):
                curr_row = (curr_row + 1) % height

        elif (dir == ">"):
            curr_row, curr_col = row, (col + 1) % width

            while ((curr_row, curr_col) in walls):
                curr_col = (curr_col + 1) % width

        elif (dir == "<"):
            curr_row, curr_col = row, (col - 1) % width

            while ((curr_row, curr_col) in walls):
                curr_col = (curr_col - 1) % width   

        new_blizzards.add((dir, curr_row, curr_col)) 

    blizzard_states[t] = new_blizzards
    blizzards = new_blizzards

for i in range(0, len(blizzard_states)):
    blizzard_states[i] = {(x[1], x[2]) for x in blizzard_states[i]}

pq = [orig_state]
heapify(pq)
visited = set()

while (len(pq) > 0):
    popped = heappop(pq)

    if (popped in visited):
        continue

    visited.add(popped)
    mins, s = popped
    e_row, e_col = s

    if((e_row, e_col) == end):
        print(mins)
        break

    neighbors = [(e_row-1, e_col), (e_row+1, e_col), (e_row, e_col-1), (e_row, e_col+1), (e_row, e_col)]

    for neighbor in neighbors:

            if (neighbor in blizzard_states[(mins+1) % period]):
                continue
            
            if ((not neighbor in [start, end]) and 
            ((not 1 <= neighbor[0] <= height-2) or (not 1 <= neighbor[1] <= width-2))):
                continue

            heappush(pq, (mins+1, neighbor))