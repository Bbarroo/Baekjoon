import sys
from collections import deque  as dq
import copy

cnt = int(sys.stdin.readline().rstrip())
field = []

for i in range(cnt):
    column =list(map(int,sys.stdin.readline().rstrip().split(" ")))
    if 9 in column:
        coor = [1,i,column.index(9),0]
        column[column.index(9)] = 0
    field.append(column)
    
q = dq()

time = 0
size = 2
eated = 0
check_m = 1

dy = [-1,0,0,1]
dx = [0,-1,1,0]
q.append(coor)

temp_field = copy.deepcopy(field)
while len(q) != 0:
    
    v,y,x,m = q[0]

    if m == check_m:
        lst = sorted(list(q))
        check_m += 1
        
        if lst[0][0] == 0:
            eated += 1
            if eated == size:
                size += 1
                eated = 0
                
            q.clear()
            field[lst[0][1]][lst[0][2]] = 0
            temp_field = copy.deepcopy(field)
            q.append([1,lst[0][1],lst[0][2],0])
            time += m
            
            check_m = 1
            continue
        
    q.popleft()

    m += 1
    
    for i in range(4):
        temp_y = y + dy[i]
        temp_x = x + dx[i]
        
        if temp_x < 0 or temp_y < 0 or temp_x > cnt-1 or temp_y > cnt-1:
            continue
        
        if temp_field[temp_y][temp_x] < 0 or temp_field[temp_y][temp_x] > size:
            temp_field[temp_y][temp_x] = -1
            continue
            
        if temp_field[temp_y][temp_x] == 0 or temp_field[temp_y][temp_x] == size:
            q.append([1,temp_y,temp_x,m])
        elif temp_field[temp_y][temp_x] < size:
            q.append([0,temp_y,temp_x,m])
        temp_field[temp_y][temp_x] = -1

print(time)
    
        
        
        
