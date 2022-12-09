from aocd import get_data
from collections import defaultdict
import math

data = get_data(year=2022, day=9).split("\n")
grid_dict = defaultdict(lambda: False)
grid_dict[(0,0)] = True
poses = []

for i in range(10):
    poses.append([0,0])

def are_touching(head_pos, tail_pos):

    for horiz_dir in [-1,0,1]:

        for vert_dir in [-1,0,1]:

            if((head_pos[0]+horiz_dir == tail_pos[0]) and (head_pos[1]+vert_dir == tail_pos[1])):
                return True

def update_tail_pos(head_pos, tail_pos):

    if(head_pos[0] >= tail_pos[0]+2 and tail_pos[1] == head_pos[1]):
            tail_pos[0] += 1

    elif(head_pos[0] <= tail_pos[0]-2 and tail_pos[1] == head_pos[1]):
        tail_pos[0] -= 1

    elif(head_pos[1] >= tail_pos[1]+2 and tail_pos[0] == head_pos[0]):
        tail_pos[1] += 1

    elif(head_pos[1] <= tail_pos[1]-2 and tail_pos[0] == head_pos[0]):
        tail_pos[1] -= 1

    elif(tail_pos[0] != head_pos[0] and tail_pos[1] != head_pos[1] and not are_touching(head_pos, tail_pos)):

        if(head_pos[0] > tail_pos[0] and head_pos[1] > tail_pos[1]):
            tail_pos[0] += 1
            tail_pos[1] += 1

        elif(head_pos[0] > tail_pos[0] and head_pos[1] < tail_pos[1]):
            tail_pos[0] += 1
            tail_pos[1] -= 1

        elif(head_pos[0] < tail_pos[0] and head_pos[1] > tail_pos[1]):
            tail_pos[0] -= 1
            tail_pos[1] += 1

        elif(head_pos[0] < tail_pos[0] and head_pos[1] < tail_pos[1]):
            tail_pos[0] -= 1
            tail_pos[1] -= 1


def update_rope():
    for i in range(9):
        update_tail_pos(poses[i], poses[i+1])

for up_move in data:
    dir, steps = up_move.split(" ")[0], int(up_move.split(" ")[1])

    for step in range(steps):

        if(dir == "R"):
            poses[0][0] += 1
            update_rope()
            grid_dict[tuple(poses[9])] = True

        elif(dir == "L"):
            poses[0][0] -= 1
            update_rope()
            grid_dict[tuple(poses[9])] = True

        elif(dir == "U"):
            poses[0][1] += 1
            update_rope()
            grid_dict[tuple(poses[9])] = True

        elif(dir == "D"):
            poses[0][1] -= 1
            update_rope()
            grid_dict[tuple(poses[9])] = True

print(len(grid_dict))