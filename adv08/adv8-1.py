from aocd import get_data
data = get_data(year=2022, day=8).split("\n")

height, width = len(data), len(data[0])
grid = [[int(data[y][x]) for x in range(width)] for y in range(height)]
num_visible = 0

for y in range(height):

    for x in range(width):
        col = [data[r][x] for r in range(height)]

        if(not any([h >= data[y][x] for h in col[y+1:]])):
            num_visible += 1

        elif(not any([h >= data[y][x] for h in col[:y]])):
            num_visible += 1

        elif(not any([h >= data[y][x] for h in data[y][x+1:]])):
            num_visible += 1

        elif(not any([h >= data[y][x] for h in data[y][:x]])):
            num_visible += 1

print(num_visible)     



