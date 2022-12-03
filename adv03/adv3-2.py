from aocd import get_data
data = get_data(year=2022, day=3).split("\n")
priorities = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
total_priorities = 0

for i in range(0, len(data)-2, 3):
    first_rucksack, second_rucksack, third_rucksack = set(list(data[i])), set(list(data[i+1])), set(list(data[i+2]))
    common_item = list(first_rucksack.intersection(second_rucksack, third_rucksack))[0]
    total_priorities += 1 + priorities.index(common_item)
    
print(total_priorities)