import sys

nums = int(sys.stdin.readline().rstrip())

rewards = []

for i in range(nums):
    if i == 0:
        rewards.append([int(sys.stdin.readline().rstrip())])
        continue
    numbers = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    temp_lst = []
    
    for k in range(i+1):
        if k == 0:
            temp_res = rewards[i-1][0] + numbers[k]
        elif k == i:
            temp_res = rewards[i-1][-1] + numbers[k]
        else:
            temp_res = max(rewards[i-1][k-1],rewards[i-1][k]) + numbers[k]
            
        temp_lst.append(temp_res)
    rewards.append(temp_lst)

print(max(rewards[-1]))