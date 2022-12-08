from aocd import get_data
data = get_data(year=2022, day=8).split("\n")

height, width = len(data), len(data[0])
grid = [[int(data[y][x]) for x in range(width)] for y in range(height)]
max_scenic_score  = 0

for y in range(height):

    for x in range(width): 
        col = [data[r][x] for r in range(height)]

        viewing_score_d = 0

        for r in range(y+1, height):
            viewing_score_d += 1

            if(col[r] >= data[y][x]):
                break

        viewing_score_u = 0

        for r in range(y-1,-1,-1):
            viewing_score_u += 1

            if(col[r] >= data[y][x]):
                break

        viewing_score_r = 0

        for c in range(x+1,width):
            viewing_score_r += 1

            if(data[y][c] >= data[y][x]):
                break

        viewing_score_l = 0
        
        for c in range(x-1,-1,-1):
            viewing_score_l += 1 

            if(data[y][c] >= data[y][x]):
                break 

        max_scenic_score = max(max_scenic_score, viewing_score_u * viewing_score_l * viewing_score_d * viewing_score_r)  

print(max_scenic_score)

