from aocd import get_data
data = get_data(year=2022, day=10).split("\n")

X = 1
X_vals = []

for instr in range(len(data)):

    if(data[instr].split(" ")[0] == "noop"):
        X_vals.append(X)

    elif(data[instr].split(" ")[0] == "addx"):
        X_vals.extend([X, X])
        X += int(data[instr].split(" ")[1])

screen = [40 * ["."] for i in range(6)]

for cycle in range(0,240):
    row = cycle // 40
    col = cycle % 40

    if (col in [X_vals[cycle]-1,X_vals[cycle], X_vals[cycle]+1] ):
        screen[row][col] = "#"

for row in range(6):
    print("".join(screen[row]))
    



