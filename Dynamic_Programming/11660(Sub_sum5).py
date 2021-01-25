import sys

n,m = map(int,sys.stdin.readline().rstrip().split(" "))

square = []

for i in range(n):
    square.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))

for i in range(n):
    for k in range(n):
        if k != 0:
            square[i][k] += square[i][k-1]
        if i != 0:
            square[i][k] += square[i-1][k]
        if i != 0 and k != 0:
            square[i][k] -= square[i-1][k-1]

for i in range(m):
    x1, y1, x2 ,y2 = map(int,sys.stdin.readline().rstrip().split(" "))
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    if x1 == 0 and y1 == 0:
        print(square[x2][y2])
    elif x1 == 0:
        print(square[x2][y2] - square[x2][y1 - 1])
    elif y1 == 0:
        print(square[x2][y2] - square[x1 - 1][y2])
    else:
        print(square[x2][y2] + square[x1-1][y1-1] - square[x2][y1-1] - square[x1-1][y2])
