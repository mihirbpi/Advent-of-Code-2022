from aocd import get_data
data = get_data(year=2022, day=15).split("\n")

def manhattan(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1-x2) + abs(y1-y2)

sensors_dict = {}
cannot_be_in_row = set()
beacons = set()
row = 2000000
min_x = 1e99
max_x = -1e99

for line in data:
    line_split = line.split(" ")
    sensor_x = int(line_split[2].split("=")[1][:-1])
    sensor_y = int(line_split[3].split("=")[1][:-1])
    close_beacon_x = int(line_split[8].split("=")[1][:-1])
    close_beacon_y = int(line_split[9].split("=")[1])
    sensor = (sensor_x, sensor_y)
    beacon = (close_beacon_x, close_beacon_y)
    beacons.add(beacon)
    close_dist = manhattan(sensor, beacon)

    if(abs(sensor[1]-row) > close_dist):
        continue

    else:
        min_x = min(min_x, sensor_x - close_dist)
        max_x = max(max_x, sensor_x + close_dist)
        sensors_dict[sensor] = close_dist

for x in range(min_x,max_x+1):
    completed = x - min_x

    for sensor in sensors_dict:
        closest_dist = sensors_dict[sensor]
        test_pt = (x, row)

        if (manhattan(test_pt, sensor) <= closest_dist):
            
            if (not test_pt in beacons):
                cannot_be_in_row.add(test_pt)

print(len(cannot_be_in_row))