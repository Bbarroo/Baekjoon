import sys

X = int(sys.stdin.readline().rstrip())

num = 4
memo = {}
memo[1] = 0
memo[2] = 1
memo[3] = 1
while num <= X:
    val = memo[num-1]
    
    if num % 2 == 0:
        val = min(val,memo[int(num/2)])
    
    if num % 3 == 0:
        val = min(val,memo[int(num/3)])
        
    memo[num] = val+1
    
    num += 1
    
print(memo[X])