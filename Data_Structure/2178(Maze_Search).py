import sys
from collections import deque as dq
        
n,m = map(int,sys.stdin.readline().rstrip().split(" "))

lim = m * n
board = []
dist = []
s = dq()

for i in range(n):
    lst = list((map(int,list(sys.stdin.readline().rstrip()))))
    board.append(lst)
    dist.append([])
    
    for j in range(m):
        dist[i].append(lim+1)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
dist[0][0] = 1
s.append([0,0])

while True:
    
    y,x = s.popleft()
    
    for i in range(4):
        temp_x = x+dx[i]
        temp_y = y+dy[i]
        
        if temp_x < 0 or temp_y < 0 or temp_x > m-1 or temp_y > n-1:
            continue
            
        if board[temp_y][temp_x] == 0:
            continue
            
        if dist[temp_y][temp_x] <= lim:
            if(dist[y][x] + 1) < dist[temp_y][temp_x]:
                s.append([temp_y,temp_x])
                dist[temp_y][temp_x] = dist[y][x] + 1
            continue
            
        dist[temp_y][temp_x] = min(dist[temp_y][temp_x],dist[y][x] + 1)
        s.append([temp_y,temp_x])
        
        if len(s) == 0:
            break
    if len(s) == 0:
        break

print(dist[n-1][m-1])