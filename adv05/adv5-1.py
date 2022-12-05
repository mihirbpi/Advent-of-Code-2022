from aocd import get_data
stacks, moves = get_data(year=2022, day=5).split("\n\n")
stacks_array = [x.replace("["," ").replace("]", " ") for x in stacks.split("\n")]
num_stacks = int(stacks_array[-1][-2])
current_stacks = []

for i in range(num_stacks):
    current_stacks.append([])

index = 0

for i in range(1, len(stacks_array[:-1][0])):
    to_add = [x[i] for x in stacks_array[:-1] if x[i] != " "][::-1]

    if(len(to_add) > 0):
        current_stacks[index].extend(to_add)
        index += 1

for move in moves.split("\n"):
    times, orig, dest = int(move.split(" ")[1]), int(move.split(" ")[3]), int(move.split(" ")[5])

    for i in range(times):
        current_stacks[dest-1].append(current_stacks[orig-1].pop(-1))

print("".join([x[-1] for x in current_stacks]))