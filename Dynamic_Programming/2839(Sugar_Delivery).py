import sys

size = int(sys.stdin.readline().rstrip())

n_five = int(size/5)
left_sugar = int(size%5)
result = n_five

if left_sugar == 0:
    print(result)
elif left_sugar == 1:
    result -= 1
    if result < 0:
        print(-1)
    else:
        print(result + 2)
    
elif left_sugar == 2:
    result -= 2
    if result < 0:
        print(-1)
    else:
        print(result + 4)
    
elif left_sugar == 3:
    print(result + 1)
    
elif left_sugar == 4:
    result -= 1
    if result < 0:
        print(-1)
    else:
        print(result + 3)