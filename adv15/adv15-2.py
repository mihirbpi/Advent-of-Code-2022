from aocd import get_data
from z3 import *
data = get_data(year=2022, day=15).split("\n")

def manhattan(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    return abs(x1-x2) + abs(y1-y2)

sensors_dict = {}
max_x_y = 4000000

for line in data:
    line_split = line.split(" ")
    sensor_x = int(line_split[2].split("=")[1][:-1])
    sensor_y = int(line_split[3].split("=")[1][:-1])
    close_beacon_x = int(line_split[8].split("=")[1][:-1])
    close_beacon_y = int(line_split[9].split("=")[1])
    sensor = (sensor_x, sensor_y)
    beacon = (close_beacon_x, close_beacon_y)
    close_dist = manhattan(sensor, beacon)
    sensors_dict[sensor] = close_dist

x = Int('x')
y = Int('y')
solution = Int('solution')
s = Solver()
s.add(x > 0, x < max_x_y, y > 0, y < max_x_y)

for sensor in sensors_dict:
    sensor_x, sensor_y = sensor
    dist = sensors_dict[sensor]
    s.add(Abs(x-sensor_x) + Abs(y-sensor_y) > dist)

s.add(solution == 4000000*x+y)
s.check()
answer = s.model()[solution].as_long()
print(answer)