from aocd import get_data
from functools import *
from collections import deque
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
    valves_dict[valve] = other_valves
    flow_dict[valve] = flow_rate

nonzero_valve_dists = {}

for valve in valves_dict:

    if(valve != "AA" and not flow_dict[valve]):
        continue

    nonzero_valve_dists[valve] = {valve:0, "AA":0}
    queue = deque([(0,valve)])
    visited = {valve}

    while (queue):
        dist, curr_valve = queue.popleft()

        for next_valve in valves_dict[curr_valve]:

            if(next_valve in visited):
                continue

            visited.add(next_valve)

            if(flow_dict[next_valve]):
                nonzero_valve_dists[valve][next_valve] = dist + 1

            queue.append((dist+1, next_valve))

    del nonzero_valve_dists[valve][valve]

    if(valve != "AA"):
        del nonzero_valve_dists[valve]["AA"]

@lru_cache(maxsize=None)
def max_press(valve, time, opened):

    highest_press = 0

    for next_valve in nonzero_valve_dists[valve]:

        if(next_valve in opened):
            continue

        time_left = time - nonzero_valve_dists[valve][next_valve] - 1

        if(time_left <= 0):
            continue
        
        highest_press = max(highest_press,  
        flow_dict[next_valve] * time_left + max_press(next_valve, time_left,  tuple(sorted([*opened, next_valve])))
        )
    return highest_press

print(max_press("AA", 30, ()))