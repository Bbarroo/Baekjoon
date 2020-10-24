import sys

nums = int(sys.stdin.readline().rstrip())

cost = []

for i in range(nums):
    r,g,b = map(int,sys.stdin.readline().rstrip().split(" "))
    
    if i != 0:
        r += min(cost[1],cost[2])
        g += min(cost[0],cost[2])
        b += min(cost[1],cost[0])
    cost = [r,g,b]
    
print(min(cost))
        