from aocd import get_data
list = [[int(y) for y in x.split("\n")] for x in get_data(year=2022,day=1).split("\n\n")]
sorted_list = sorted(list, key=lambda x: sum(x))
print(sum(sorted_list[-1] + sorted_list[-2] + sorted_list[-3]))