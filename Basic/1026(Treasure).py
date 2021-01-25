import sys

cnt = int(sys.stdin.readline().rstrip())

A = list(map(int,sys.stdin.readline().rstrip().split(" ")))
B = list(map(int,sys.stdin.readline().rstrip().split(" ")))

A.sort()
B.sort()
B.reverse()

res = 0

for i in range(len(A)):
    res += A[i] * B[i]
    
print(res)