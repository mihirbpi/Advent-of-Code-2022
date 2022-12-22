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
        nr = r
        nc = c

        while True:
            nr = (nr + dr) % len(board)
            nc = (nc + dc) % len(board[0])

            if (board[nr][nc] != " "):
                break

        if (board[nr][nc] == "#"):
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

print(1000*row + 4*col + facing)