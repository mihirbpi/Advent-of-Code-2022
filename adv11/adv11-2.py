from aocd import get_data
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

for monkey in monkey_list:
    monkey[0] = [list(map(lambda x: x % other_monkey[2], monkey[0])) for other_monkey in monkey_list]

for round in range(10000):

    for monkey_index in range(len(monkey_list)):
        monkey = monkey_list[monkey_index]

        while(len(monkey[0][0]) > 0):

            monkey[-1] += 1
            other_monkey_vals = []

            for other_monkey_index in range(len(monkey_list)):
                val = monkey[0][other_monkey_index].pop(0)
                new_val = 0

                if(monkey[1][0] == "*"):

                    if(monkey[1][1] == "old"):
                            new_val = (val * val) % monkey_list[other_monkey_index][2]
                    else:
                        new_val = (val * int(monkey[1][1])) % monkey_list[other_monkey_index][2]
                    
                elif(monkey[1][0] == "+"):
                    new_val = (val + int(monkey[1][1])) % monkey_list[other_monkey_index][2]
                other_monkey_vals.append(new_val)
            
            if(other_monkey_vals[monkey_index] == 0):

                for other_monkey_index in range(len(monkey_list)):
                    monkey_list[monkey[3]][0][other_monkey_index].append(other_monkey_vals[other_monkey_index])

            else:

               for other_monkey_index in range(len(monkey_list)):
                    monkey_list[monkey[4]][0][other_monkey_index].append(other_monkey_vals[other_monkey_index])

monkey_list.sort(key=lambda x: x[-1])
print(math.prod([entry[-1] for entry in monkey_list[-2:]]))