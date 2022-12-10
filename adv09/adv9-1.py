from aocd import get_data
from collections import defaultdict

data = get_data(year=2022, day=9).split("\n")
grid_dict = defaultdict(lambda: False)
grid_dict[(0,0)] = True
head_pos, tail_pos = [0,0], [0,0]

def are_touching():

    for horiz_dir in [-1,0,1]:

        for vert_dir in [-1,0,1]:

            if((head_pos[0] + horiz_dir == tail_pos[0]) and (head_pos[1] + vert_dir == tail_pos[1])):
                return True

def update_tail_pos():

    if(head_pos[0] >= tail_pos[0]+2 and tail_pos[1] == head_pos[1]):
            tail_pos[0] += 1

    elif(head_pos[0] <= tail_pos[0]-2 and tail_pos[1] == head_pos[1]):
        tail_pos[0] -= 1

    elif(head_pos[1] >= tail_pos[1]+2 and tail_pos[0] == head_pos[0]):
        tail_pos[1] += 1

    elif(head_pos[1] <= tail_pos[1]-2 and tail_pos[0] == head_pos[0]):
        tail_pos[1] -= 1

    elif(tail_pos[0] != head_pos[0] and tail_pos[1] != head_pos[1] and not are_touching()):

        if(head_pos[0] > tail_pos[0]):
            tail_pos[0] += 1

            if(head_pos[1] > tail_pos[1]):
                tail_pos[1] += 1

            else:
                tail_pos[1] -= 1

        elif(head_pos[0] < tail_pos[0]):
            tail_pos[0] -= 1

            if(head_pos[1] > tail_pos[1]):
                tail_pos[1] += 1
                
            else:
                tail_pos[1] -= 1

for up_move in data:
    dir, steps = up_move.split(" ")[0], int(up_move.split(" ")[1])

    for step in range(steps):

        if(dir == "R"):
            head_pos[0] += 1

        elif(dir == "L"):
            head_pos[0] -= 1

        elif(dir == "U"):
            head_pos[1] += 1

        elif(dir == "D"):
            head_pos[1] -= 1
    
        update_tail_pos()
        grid_dict[tuple(tail_pos)] = True
        
print(len(grid_dict))