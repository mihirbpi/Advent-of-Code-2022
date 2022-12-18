from aocd import get_data
data = get_data(year=2022, day=18).split("\n")

filled_cubes = []

for line in data:
    x,y,z = list(map(int,line.split(",")))
    filled_cubes.append((x,y,z))

surface_faces = 0

for cube in filled_cubes:
    x,y,z = cube
    neighbors = [(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)]

    covered_faces = 0

    for neighbor in neighbors:

        if neighbor in filled_cubes:
            covered_faces += 1

    surface_faces += 6 - covered_faces

print(surface_faces)