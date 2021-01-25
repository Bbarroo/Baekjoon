import sys

cnt = int(sys.stdin.readline().rstrip())

for _ in range(cnt):
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().rstrip().split(" "))
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        r = (x2 - x1) ** 2+ (y2-y1) ** 2
        if (r1 +r2)**2 == r or abs(r1-r2) ** 2 == r:
            print(1)
        elif (r1+r2)**2 < r or abs(r1-r2) ** 2 > r:
            print(0)
        else:
            print(2)
    