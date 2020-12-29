import sys
x,y = map(int,sys.stdin.readline().rstrip().split(" "))

tomatoes = []

for i in range(y):
    tomatoes.append(list(map(int,sys.stdin.readline().rstrip().split(" "))))

dy = [1,-1,0,0]
dx = [0,0,-1,1]

adultomato = []

for coor_y in range(y):
    for coor_x in range(x):
        if tomatoes[coor_y][coor_x] == 1:
            adultomato.append([coor_y,coor_x])  # get a information of initial ripe tomato

cache = []

check = False
cnt = 0

while True:
    for tomato in adultomato:
        for i in range(4):

            new_y = tomato[0] + dy[i]
            new_x = tomato[1] + dx[i]

            if new_y < 0 or new_x < 0 or new_y >= y or new_x >= x: # check list index
                continue

            new_tomato = tomatoes[new_y][new_x]

            if new_tomato == -1 or new_tomato == 1:  # if already riped or none, coninue
                continue
            else:
                cache.append([new_y,new_x])
                tomatoes[new_y][new_x] = 1
                check = True
    if len(cache) == 0:  # if there is a no changed tomato, finish the loop
        break
    else: # if there are some tomato changed, it is next riped tomato. and increase count
        adultomato = cache.copy()
        cache = []
        cnt += 1

alladult = True

for coor_y in range(y): # check there is any none-ripe tomato
    for coor_x in range(x):
        if tomatoes[coor_y][coor_x] == 0:
            alladult = False

if alladult:
    print(cnt)
else:
    print(-1)