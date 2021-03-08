import sys
from collections import deque

n_input = int(sys.stdin.readline().rstrip())

ant_hall = {}
for _ in range(n_input):
    halls = list(map(str,sys.stdin.readline().rstrip().split(" ")))
    n_hall = halls[0]
    temp_hall = ant_hall
    for hall in halls[1:]:
        if temp_hall.get(hall) is None:
            temp_hall[hall] = {}
        temp_hall = temp_hall[hall]
  
q = deque()

for key in list(sorted(ant_hall.keys())):
    q.appendleft([key,ant_hall[key],0])
while q:
    target, target_dict, layer = q.pop()
    print('-' * layer + target)
    for key in list(sorted(target_dict.keys(),reverse=True)):
        q.append([key,target_dict[key],layer+2])
