from aocd import get_data
import math
data = get_data(year=2022, day=11).split("\n\n")

monkey_list = []

for monkey_info in data:
    entries = monkey_info.split("\n")
    item_list = list(map(int,entries[1].split(": ")[1].split(",")))
    op = entries[2].split(": ")[1].split(" ")[-2:]
    test_div = int(entries[3].split(" ")[-1])
    true_monkey = int(entries[4].split(" ")[-1])
    false_monkey = int(entries[5].split(" ")[-1])
    monkey_list.append([item_list, op, test_div, true_monkey, false_monkey, 0])

for round in range(20):

    for monkey in monkey_list:

        while(len(monkey[0]) > 0):

            curr_item = monkey[0].pop(0)
            monkey[-1] += 1

            if(monkey[1][0] == "*"):

                if(monkey[1][1] == "old"):
                    curr_item = curr_item * curr_item

                else:
                    curr_item = curr_item * int(monkey[1][1])

            elif(monkey[1][0] == "+"):
                curr_item = curr_item + int(monkey[1][1])
            
            curr_item = curr_item // 3

            if(curr_item % monkey[2] == 0):
                monkey_list[monkey[3]][0].append(curr_item)

            else:
                monkey_list[monkey[4]][0].append(curr_item)

monkey_list.sort(key=lambda x: x[-1])
print(math.prod([entry[-1] for entry in monkey_list[-2:]]))