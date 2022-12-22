from aocd import get_data
import re
data = get_data(year=2022, day=22)

board_data = data.split("\n\n")[0]
move_data = data.split("\n\n")[1]
board = []

for line in board_data.split("\n"):
    board.append(line)

width = max(map(len, board))
board = [line + " " * (width - len(line)) for line in board]

r = 0
c = 0
dr = 0
dc = 1

while (board[r][c] != "#" and board[r][c] != "."):
    c += 1

moves = re.findall(r'(\d+)([RL]?)', move_data)

for x,y in moves:
    x = int(x)

    for _ in range(x):
        cdr = dr
        cdc = dc
        nr = r + dr
        nc = c + dc

        if nr < 0 and 50 <= nc < 100 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 100, 0

        elif nc < 0 and 150 <= nr < 200 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 0, nr - 100

        elif nr < 0 and 100 <= nc < 150 and dr == -1:
            nr, nc = 199, nc - 100

        elif nr >= 200 and 0 <= nc < 50 and dr == 1:
            nr, nc = 0, nc + 100

        elif nc >= 150 and 0 <= nr < 50 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 99

        elif nc == 100 and 100 <= nr < 150 and dc == 1:
            dc = -1
            nr, nc = 149 - nr, 149

        elif nr == 50 and 100 <= nc < 150 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc - 50, 99

        elif nc == 100 and 50 <= nr < 100 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 49, nr + 50

        elif nr == 150 and 50 <= nc < 100 and dr == 1:
            dr, dc = 0, -1
            nr, nc = nc + 100, 49

        elif nc == 50 and 150 <= nr < 200 and dc == 1:
            dr, dc = -1, 0
            nr, nc = 149, nr - 100

        elif nr == 99 and 0 <= nc < 50 and dr == -1:
            dr, dc = 0, 1
            nr, nc = nc + 50, 50

        elif nc == 49 and 50 <= nr < 100 and dc == -1:
            dr, dc = 1, 0
            nr, nc = 100, nr - 50

        elif nc == 49 and 0 <= nr < 50 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 0

        elif nc < 0 and 100 <= nr < 150 and dc == -1:
            dc = 1
            nr, nc = 149 - nr, 50

        if (board[nr][nc] == "#"):
            dr = cdr
            dc = cdc
            break
        
        r = nr
        c = nc

    if (y == "R"):
        dr, dc = dc, -dr

    elif (y == "L"):
        dr, dc = -dc, dr

row = r + 1
col = c + 1
facing = None

if((dr,dc) ==(0,1)):
    facing = 0

elif((dr,dc) == (1,0)):
    facing = 1

elif ((dr,dc) == (0,-1)):
    facing = 2

elif((dr,dc) == (-1,0)):
    facing = 3

print (1000 * row + 4 * col + facing)