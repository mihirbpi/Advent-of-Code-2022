from aocd import get_data
from collections import deque
data = get_data(year=2022, day=19).split("\n")

def bfs(ore_rbt_cost_ore, clay_rbt_cost_ore, obs_rbt_cost_ore, obs_rbt_cost_clay, geod_rbt_cost_ore, geod_rbt_cost_obs):

    start_state = (1,0,0,0,0,0,0,0,24)
    queue = deque([start_state])
    visited = set()
    best = -1e99

    while (queue):
        state = queue.popleft() 
        ore_rbts, clay_rbts, obs_rbts, geod_rbts, ore, clay, obs, geod, mins = state
        best = max(best, geod)

        if (mins < 1):
            continue

        max_cost_ore = max([ore_rbt_cost_ore, clay_rbt_cost_ore, obs_rbt_cost_ore, geod_rbt_cost_ore])

        if (ore_rbts >= max_cost_ore):
            ore_rbts = max_cost_ore

        if (clay_rbts >= obs_rbt_cost_clay):
            clay_rbts = obs_rbt_cost_clay

        if (obs_rbts >= geod_rbt_cost_obs):
            obs_rbts = geod_rbt_cost_obs

        if ore >= mins*max_cost_ore - ore_rbts*(mins-1):
            ore = mins*max_cost_ore - ore_rbts*(mins-1)

        if clay >= mins*obs_rbt_cost_clay -clay_rbts*(mins-1):
            clay = mins*obs_rbt_cost_clay -clay_rbts*(mins-1)

        if obs >= mins*geod_rbt_cost_obs - obs_rbts*(mins-1):
            obs = mins*geod_rbt_cost_obs - obs_rbts*(mins-1)

        state = (ore_rbts, clay_rbts, obs_rbts, geod_rbts, ore, clay, obs, geod, mins)

        if state in visited:
            continue

        visited.add(state)
        queue.append((ore_rbts, clay_rbts, obs_rbts, geod_rbts, ore + ore_rbts, clay + clay_rbts, obs + obs_rbts, geod + geod_rbts, mins-1))

        if (ore >= ore_rbt_cost_ore):
            queue.append((ore_rbts+1, clay_rbts, obs_rbts, geod_rbts, ore + ore_rbts - ore_rbt_cost_ore, clay + clay_rbts, obs + obs_rbts, geod + geod_rbts, mins-1))

        if (ore >= clay_rbt_cost_ore):
            queue.append((ore_rbts, clay_rbts+1, obs_rbts, geod_rbts, ore + ore_rbts - clay_rbt_cost_ore, clay + clay_rbts, obs + obs_rbts, geod + geod_rbts, mins-1))

        if (ore >= obs_rbt_cost_ore and clay >= obs_rbt_cost_clay):
            queue.append((ore_rbts, clay_rbts, obs_rbts+1, geod_rbts, ore + ore_rbts - obs_rbt_cost_ore, clay + clay_rbts - obs_rbt_cost_clay, obs + obs_rbts, geod + geod_rbts, mins-1))

        if (ore >= geod_rbt_cost_ore and obs >= geod_rbt_cost_obs):
            queue.append((ore_rbts, clay_rbts, obs_rbts, geod_rbts+1, ore + ore_rbts - geod_rbt_cost_ore, clay + clay_rbts, obs + obs_rbts - geod_rbt_cost_obs, geod + geod_rbts, mins-1))

    return best

result = 0

for line in data:
    ID = int(line.split(" ")[1][:-1])
    ore_rbt_cost_ore = int(line.split(" ")[6])
    clay_rbt_cost_ore = int(line.split(" ")[12])
    obs_rbt_cost_ore = int(line.split(" ")[18])
    obs_rbt_cost_clay = int(line.split(" ")[21])
    geod_rbt_cost_ore = int(line.split(" ")[27])
    geod_rbt_cost_obs = int(line.split(" ")[30])
    max_geods = bfs(ore_rbt_cost_ore, clay_rbt_cost_ore, obs_rbt_cost_ore, obs_rbt_cost_clay, geod_rbt_cost_ore, geod_rbt_cost_obs)
    result += ID * max_geods

print(result)