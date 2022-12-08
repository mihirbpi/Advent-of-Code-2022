from aocd import get_data
import math
data = get_data(year=2022, day=8).split("\n")

height, width = len(data), len(data[0])
grid = [[int(data[y][x]) for x in range(width)] for y in range(height)]
max_scenic_score  = 0

for y in range(height):

    for x in range(width): 
        col = [grid[r][x] for r in range(height)]
        viewing_scores = [0, 0, 0, 0]

        for r in range(y-1,-1,-1):
            viewing_scores[0] += 1

            if(col[r] >= grid[y][x]):
                break
        
        for c in range(x-1,-1,-1):
            viewing_scores[1] += 1 

            if(grid[y][c] >= grid[y][x]):
                break 

        for r in range(y+1, height):
            viewing_scores[2] += 1

            if(col[r] >= grid[y][x]):
                break

        for c in range(x+1,width):
            viewing_scores[3] += 1

            if(grid[y][c] >= grid[y][x]):
                break

        max_scenic_score = max(max_scenic_score, math.prod(viewing_scores)) 

print(max_scenic_score)

