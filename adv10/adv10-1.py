from aocd import get_data
data = get_data(year=2022, day=10).split("\n")

X = 1
signal_strength_total = 0
X_vals = []

for instr in range(len(data)):

    if(data[instr].split(" ")[0] == "noop"):
        X_vals.append(X)

    elif(data[instr].split(" ")[0] == "addx"):
        X_vals.extend([X, X])
        X += int(data[instr].split(" ")[1])

print(sum([X_vals[cycle-1]*cycle for cycle in [20,60,100,140,180,220]]))