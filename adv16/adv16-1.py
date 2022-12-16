from aocd import get_data
from functools import *
data = get_data(year=2022, day=16).split("\n")
valves_dict = {}

for line in data:
    line =  line.replace("valves", "valve")
    line = line.replace(",","")
    line_split = line.split(" ")
    valve = line_split[1]
    flow_rate = int(line_split[4].split("=")[1][:-1])
    other_valves = line_split[line_split.index("valve")+1:]
    valves_dict[valve] = [flow_rate, other_valves]

@lru_cache(maxsize=None)
def max_press(curr_valve, opened, mins_left):

    if(mins_left <= 0):
        return 0

    curr_flow, connected_valves = valves_dict[curr_valve]
    highest_press = 0

    for next_valve in connected_valves:
        highest_press = max(highest_press, max_press(next_valve, opened, mins_left-1))

    if curr_valve not in opened and curr_flow > 0:
        new_opened =  tuple(sorted([*opened, curr_valve]))
        highest_press = max(highest_press, max_press(curr_valve, new_opened, mins_left-1) + (mins_left-1) * curr_flow)

    return highest_press

print(max_press("AA", (), 30))