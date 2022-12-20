from aocd import get_data
data = list(map(int,get_data(year=2022, day=20).split("\n")))

KEY = 811589153
data = [(i,data[i]*KEY) for i in range(len(data))]
original_data = data.copy()
m = len(original_data)

def swap(l, i, j):
    l[j], l[i] = l[i], l[j]
    return l

for round in range(10):

    for entry in original_data:
        index_num_to_move = data.index(entry)
        num_to_move = entry[1] % (m-1)
        idx = index_num_to_move

        for x in range(num_to_move):
            data = swap(data, idx, (idx+1) % m)
            idx = (idx+1) % m

final_list = [x[1] for x in data]
zero_index = final_list.index(0)
ans = 0

for i in range(1,4):
    ans += final_list[(zero_index + i*1000) % m]
print(ans)