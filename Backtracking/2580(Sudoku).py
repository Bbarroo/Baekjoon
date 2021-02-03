import sys
def get_possible_numbers(target):
    global board
    check = set()
    y,x = target
    for i in range(9):
        check.add(board[y][i])
        check.add(board[i][x])
    sector_y = int(y/3) * 3
    sector_x = int(x/3) * 3
    for i in range(3):
        for j in range(3):
            new_y = sector_y + i
            new_x = sector_x + j
            if new_y == y and new_x == x:
                continue
            else:
                check.add(board[new_y][new_x])
    nums = set([1,2,3,4,5,6,7,8,9])
    return list(nums-check)

global board   
board = []
for i in range(9):
    line = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    board.append(line)

check = []
possible = []
for y in range(9):
    temp = []
    for x in range(9):
        if board[y][x] == 0:
            check.append([y,x])
        temp.append(-1)
    possible.append(temp)

i = 0
while i < len(check):
    y,x = check[i]
    if possible[y][x] == -1:
        possible_lst = get_possible_numbers(check[i])
        if possible_lst == []:
            possible[y][x] = -1
            board[y][x] = 0
            i -= 1
        else:
            board[y][x] = possible_lst[0]
            del possible_lst[0]
            possible[y][x] = possible_lst
            i += 1
    elif possible[y][x] == []:
        possible[y][x] = -1
        board[y][x] = 0
        i -= 1
    else:
        board[y][x] = possible[y][x][0]
        del possible[y][x][0]
        i += 1

for y in range(9):
    for x in range(9):
        if x != 8:
            print(board[y][x], end = ' ')
        else:
            print(board[y][x])