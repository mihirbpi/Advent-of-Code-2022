from aocd import get_data
data = get_data(year=2022, day=3).split("\n")
priorities = [chr(i) for i in range(97,123)] + [chr(i) for i in range(65,91)]
total_priorities = 0

for entry in data:
    first_rucksack, second_rucksack = set(entry[:len(entry)// 2]), set(entry[len(entry)//2:])
    common_item = list(first_rucksack.intersection(second_rucksack))[0]
    total_priorities += 1 + priorities.index(common_item)
    
print(total_priorities)

