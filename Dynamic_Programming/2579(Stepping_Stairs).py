import sys

cnt = int(sys.stdin.readline().rstrip())

rewards = []

for i in range(cnt):
    num = int(sys.stdin.readline().rstrip())
    
    if i == 0:
        rewards.append([num])
    elif i == 1:
        rewards.append([num,num+rewards[0][0]])
    elif i == 2:
        rewards.append([num+rewards[0][0],num+rewards[1][0]])
    else:
        rewards.append([max(rewards[i-2])+num,rewards[i-1][0]+num])

print(max(rewards[cnt-1]))