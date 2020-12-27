import sys

A,B,target = map(int,sys.stdin.readline().rstrip().split(" "))

if (target - B) > 0:
    print(int(A/(target-B)) + 1)
else:
    print(-1)