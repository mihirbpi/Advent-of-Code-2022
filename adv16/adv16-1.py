from aocd import get_data
from functools import *
data = get_data(year=2022, day=16).split("\n")

valves_dict = {}
flow_dict = {}

for line in data:
    line =  line.replace("valves", "valve")
    line = line.replace(",","")
    line_split = line.split(" ")
    valve = line_split[1]
    flow_rate = int(line_split[4].split("=")[1][:-1])
    other_valves = line_split[line_split.index("valve")+1:]
    valves_dict[valve] = [flow_rate, other_valves]

@lru_cache(maxsize=None)
def max_press(curr, opened, mins_left):

    if(mins_left <= 0):
        return 0

    highest_press = 0

    if (curr not in opened):

        val = (mins_left-1) * valves_dict[curr][0]
        curr_opened =  tuple(sorted(opened + (curr,)))

        for other_valve in valves_dict[curr][1]:

            if(val != 0):
                highest_press = max(highest_press, val + max_press(other_valve, curr_opened, mins_left-2))

            highest_press = max(highest_press, max_press(other_valve, opened, mins_left-1))

    return highest_press

print(max_press("AA", (), 30))