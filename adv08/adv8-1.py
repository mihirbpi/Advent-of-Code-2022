from aocd import get_data
data = get_data(year=2022, day=8).split("\n")

height, width = len(data), len(data[0])
grid = [[int(data[y][x]) for x in range(width)] for y in range(height)]
num_visible = 0

for y in range(height):

    for x in range(width):
        col = [grid[r][x] for r in range(height)]

        if(not any([h >= grid[y][x] for h in col[y+1:]]) or
           not any([h >= grid[y][x] for h in col[:y]]) or  
           not any([h >= grid[y][x] for h in grid[y][x+1:]]) or 
           not any([h >= grid[y][x] for h in grid[y][:x]])):
            num_visible += 1

print(num_visible)     



