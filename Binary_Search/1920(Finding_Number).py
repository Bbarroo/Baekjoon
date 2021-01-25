import sys

num_lst = int(sys.stdin.readline().rstrip())
lst = list(map(int,sys.stdin.readline().rstrip().split(" ")))
num_target = int(sys.stdin.readline().rstrip())
targets = list(map(int,sys.stdin.readline().rstrip().split(" ")))

lst.sort()

for target in targets:
    start = 0
    end = num_lst - 1
    while True:
        mid = int((start + end)/2)
        if lst[mid] == target:
            print(1)
            break
        if start == end:
            print(0)
            break
        if lst[mid] > target:
            end = mid
        elif lst[mid] < target:
            start = mid + 1