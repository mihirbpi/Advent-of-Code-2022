from aocd import get_data
data = get_data(year=2022, day=4).split("\n")
num_pairs = 0

for pair in data:
    pair_1, pair_2 = pair.split(",")
    pair_1_lower, pair_1_upper = [int(x) for x in pair_1.split("-")]
    pair_2_lower, pair_2_upper = [int(x) for x in pair_2.split("-")]

    if(pair_1_lower >= pair_2_lower and pair_1_upper <= pair_2_upper):
        num_pairs += 1

    elif(pair_2_lower >= pair_1_lower and pair_2_upper <= pair_1_upper):
        num_pairs += 1

print(num_pairs)
