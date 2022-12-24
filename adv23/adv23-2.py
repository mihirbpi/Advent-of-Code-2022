from aocd import get_data
from collections import defaultdict
data = get_data(year=2022, day=23).split("\n")

elves = set()

for row in range(len(data)):

    for col in range(len(data[row])):

        if(data[row][col] == "#"):
            elves.add((row, col))

check_order = ["N", "S", "W", "E"]
round = 0

while (True):
    round += 1
    elves_can_move = set()
    proposed_locs = defaultdict(lambda: 0)

    for elf in elves:
        elf_row, elf_col = elf

        around = {(elf_row-1, elf_col-1), (elf_row-1, elf_col), (elf_row-1, elf_col+1), (elf_row, elf_col-1), (elf_row, elf_col+1), (elf_row+1,elf_col-1), (elf_row+1, elf_col), (elf_row+1, elf_col+1)}

        if (not any([(x in elves) for x in around])):
            continue

        for dir in check_order:

            if ((dir == "N") and 
                ((elf_row-1, elf_col) not in elves) and 
                ((elf_row-1, elf_col+1) not in elves) and
                ((elf_row-1, elf_col-1) not in elves)):
                elves_can_move.add((elf_row, elf_col, elf_row-1, elf_col, "N"))
                proposed_locs[(elf_row-1, elf_col)] += 1
                break

            elif ((dir == "S") and 
                  ((elf_row+1, elf_col) not in elves) and
                  ((elf_row+1, elf_col+1) not in elves) and 
                  ((elf_row+1, elf_col-1) not in elves)):
                elves_can_move.add((elf_row, elf_col, elf_row+1, elf_col, "S"))
                proposed_locs[(elf_row+1, elf_col)] += 1
                break

            elif ((dir == "W") and 
                  ((elf_row, elf_col-1) not in elves) and
                  ((elf_row-1, elf_col-1) not in elves) and
                  ((elf_row+1, elf_col-1) not in elves)):
                elves_can_move.add((elf_row, elf_col, elf_row, elf_col-1, "W"))
                proposed_locs[(elf_row, elf_col-1)] += 1
                break

            elif ((dir == "E") and 
                  ((elf_row, elf_col+1) not in elves) and
                  ((elf_row-1, elf_col+1) not in elves) and 
                  ((elf_row+1, elf_col+1) not in elves)):
                elves_can_move.add((elf_row, elf_col, elf_row, elf_col+1, "E"))
                proposed_locs[(elf_row, elf_col+1)] += 1
                break

    for elf in elves_can_move.copy():
            elf_row, elf_col, elf_new_row, elf_new_col, _ = elf

            if (proposed_locs[(elf[2], elf[3])] > 1):
                elves_can_move.remove(elf)

    if(len(list(elves_can_move)) == 0):
        print(round) 
        break

    elves_to_change = {(elf[0], elf[1]) for elf in elves_can_move}
    new_elves = {(elf[2], elf[3]) for elf in elves_can_move}
    elves = elves.difference(elves_to_change)
    elves = elves.union(new_elves)
    check_order.append(check_order[0])
    check_order.pop(0)