from aocd import get_data
from collections import defaultdict
data = get_data(year=2022, day=17).split("\n")

class Rock:

    def __init__(self, x_start, y_start, grid, type):
        self.positions = []

        if(type == 0):
            for x in range(x_start, x_start+4):
                self.positions.append((x, y_start))

        elif(type == 1):
            self.positions.append((x_start, y_start+1))
            self.positions.append((x_start+1, y_start+1))
            self.positions.append((x_start+2, y_start+1))
            self.positions.append((x_start+1, y_start+2))
            self.positions.append((x_start+1, y_start))

        elif(type == 2):
            for x in range(x_start, x_start+3):
                self.positions.append((x, y_start))
            self.positions.append((x_start+2, y_start+1))
            self.positions.append((x_start+2, y_start+2))
        
        elif(type == 3):
            for y in range(y_start, y_start+4):
                self.positions.append((x_start, y))

        elif(type == 4):
            self.positions.append((x_start, y_start))
            self.positions.append((x_start, y_start+1))
            self.positions.append((x_start+1, y_start))
            self.positions.append((x_start+1, y_start+1))


        for pos in self.positions:
            grid[pos] = "#"

    def move_right(self, grid):

        if any([grid[(pos[0]+1, pos[1])] == "#" and not (pos[0]+1, pos[1]) in self.positions for pos in self.positions]):
            return

        if any([pos[1] < 0 for pos in self.positions]):
            return

        if any([pos[0]+1 > 6 for pos in self.positions]):
            return

        if any([pos[0]+1 < 0 for pos in self.positions]):
            return

        new_positions = [(pos[0]+1,pos[1]) for pos in self.positions]

        for pos in self.positions:
            grid[pos] = "."

        for new_pos in new_positions:
            grid[new_pos] = "#"
        self.positions = new_positions

    def move_left(self, grid):

        if any([grid[(pos[0]-1, pos[1])] == "#" and not (pos[0]-1, pos[1]) in self.positions for pos in self.positions]):
            return

        if any([pos[1] < 0 for pos in self.positions]):
            return 

        if any([pos[0]-1 > 6 for pos in self.positions]):
            return 

        if any([pos[0]-1 < 0 for pos in self.positions]):
            return

        new_positions = [(pos[0]-1,pos[1]) for pos in self.positions]

        for pos in self.positions:
            grid[pos] = "."

        for new_pos in new_positions:
            grid[new_pos] = "#"
        self.positions = new_positions
    
    def fall_down(self, grid):

        if any([grid[(pos[0], pos[1]-1)] == "#" and not (pos[0], pos[1]-1) in self.positions for pos in self.positions]):
            return False

        if any([pos[1]-1 < 0 for pos in self.positions]):
            return False

        if any([pos[0] > 6 for pos in self.positions]):
            return False

        if any([pos[0] < 0 for pos in self.positions]):
            return False

        new_positions = [(pos[0],pos[1]-1) for pos in self.positions]

        for pos in self.positions:
            grid[pos] = "."

        for new_pos in new_positions:
            grid[new_pos] = "#"

        self.positions = new_positions
        return True

class Simulation:

    def __init__(self):
        self.grid = defaultdict(lambda: ".")
        self.curr_rock = 0
        self.num_stopped = 0
        self.jet_index = 0

    def process_curr_rock(self):
        y_start = None

        if(self.num_stopped == 0):
            y_start  = 3

        else:
            y_start = max([x[1] for x in self.grid if self.grid[x] == "#"]) + 4

        rock = Rock(2, y_start, self.grid, self.curr_rock)

        while (True):
            dir = data[0][self.jet_index]

            if (dir == ">"):
                self.jet_index += 1
                self.jet_index = self.jet_index % len(data[0])
                rock.move_right(self.grid)
                res = rock.fall_down(self.grid)
                
                if (not res):
                    self.num_stopped += 1
                    break


            elif(dir == "<"):
                self.jet_index += 1
                self.jet_index = self.jet_index % len(data[0])
                rock.move_left(self.grid)
                res = rock.fall_down(self.grid)

                if (not res):
                    self.num_stopped += 1
                    break
        self.curr_rock += 1
        self.curr_rock = self.curr_rock % 5

    def run_simulation(self):

        while(self.num_stopped < 2022):
            self.process_curr_rock()
                    
sim = Simulation()
sim.run_simulation()
print(max([1 + x[1] for x in sim.grid if sim.grid[x] == "#"]))