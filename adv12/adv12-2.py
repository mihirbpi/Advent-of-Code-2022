from aocd import get_data
from collections import defaultdict, deque
from string import ascii_lowercase

data = get_data(year=2022, day=12).split("\n")

def height(s):
    return ascii_lowercase.index(s)

start, end = None, None
grid = defaultdict(lambda: None)

for row in range(len(data)):

    for col in range(len(data[0])):
        grid[(row,col)] = [data[row][col], []]

        if(data[row][col] == "S"):
            start = (row,col)
            grid[start] = ["a", []]

        elif(data[row][col] == "E"):
            end = (row,col)
            grid[end] = ["z", []]

for row in range(len(data)):

    for col in range(len(data[0])):

        for surround in [(row+1, col), (row-1,col), (row, col+1), (row, col-1)]:

            if(grid[surround] and (height(grid[surround][0]) <= height(grid[(row,col)][0]) + 1)):
                grid[(row,col)][1].append(surround)

def get_steps(s):           
    bfs_queue = deque()
    visited = set()
    visited.add(s)
    bfs_queue.append(s)
    curr = s
    lengths_dict = defaultdict(lambda:0)
    lengths_dict[curr] = 0

    while (bfs_queue):
        curr = bfs_queue.popleft()

        if(curr == end):
            break

        neighbors = grid[curr][1]

        for neighbor in neighbors:

            if not neighbor in visited:
                visited.add(neighbor)
                lengths_dict[neighbor] = lengths_dict[curr] + 1
                if(neighbor == end):
                    print("neighbor", s)
                bfs_queue.append(neighbor)

    if(end in lengths_dict):
        return lengths_dict[end]
    return 1e99

min_dist = 1e99

for row in range(len(data)):

    for col in range(len(data[0])):
        if(grid[(row,col)] and grid[(row,col)][0] == "a"):
            min_dist = min(min_dist, get_steps((row,col)))

print(min_dist)