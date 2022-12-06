from aocd import get_data
data = get_data(year=2022, day=6).split("\n")[0]

for i in range(0, len(data)-3):
    string = data[i:i+4]

    if(not any([string.count(e) > 1 for e in string])):
        print(i+4)
        break
