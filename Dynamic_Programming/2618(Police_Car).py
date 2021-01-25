import sys



def calcDist(lst1,lst2):
   return abs(lst1[0]-lst2[0]) + abs(lst1[1] - lst2[1])

max_co = int(sys.stdin.readline().rstrip())
nums = int(sys.stdin.readline().rstrip())

car_1 = [1,1]
car_2 = [max_co,max_co]
how = []
first = [car_1,car_2,0,0]
dist_coor = []
now =[first]
root = []
for i in range(nums):
    new_coor = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    dist_coor.append([new_coor[0],new_coor[1]])

    check = {}

    for tn in now:
        go_one = [new_coor, tn[1], tn[2] + calcDist(new_coor,tn[0]),1]
        go_two = [tn[0], new_coor, tn[2] + calcDist(new_coor,tn[1]),2]
        check_key_one = go_one[1][0] * 10000 + go_one[1][1]
        check_key_two = go_two[0][0] * 10000 + go_two[0][1]
        if check.get(check_key_two) is None:
            check[check_key_two] = go_two
        elif check[check_key_two][2] > go_two[2]:
            check[check_key_two] = go_two
        if check.get(check_key_one) is None:
            check[check_key_one] = go_one
        elif check[check_key_one][2] > go_one[2]:
            check[check_key_one] = go_one
    now = list(check.values())
    root.append(now)

smallest = 0

ii = 0
jj = 0
real_root = []
dist = -1
changed =0
index_changed = 0
nonmodified = 0
for i,ro in enumerate(reversed(root)):
    if i == 0:
        for k in ro:
            if dist == -1 or dist> k[2]:
                dist = k[2]
                index_changed = k[3]
                changed = k[k[3]-1]
                if k[3] == 1:
                    index_nonmodified = 1
                    nonmodified = k[1]
                else:
                    index_nonmodified = 0
                    nonmodified = k[0]
                smallest = k[2]
                real_root = []
                real_root.append(k[3])
    else:
        for k in ro:
            if k[2] == 0:
                break
            if calcDist(changed,k[index_changed-1]) == dist - k[2] and nonmodified ==k[index_nonmodified]:
                dist = k[2]
                index_changed = k[3]
                changed = k[k[3] - 1]
                if k[3] == 1:
                    index_nonmodified = 1
                    nonmodified = k[1]
                else:
                    index_nonmodified = 0
                    nonmodified = k[0]
                real_root.append(k[3])
                break
print(smallest)
for k,i in enumerate(reversed(real_root)):
    print(i)

