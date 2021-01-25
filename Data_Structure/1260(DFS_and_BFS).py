import sys

class Stack:
    
    def __init__(self):
        self.stack = []
        self.long = 0
    def isEmpty(self):
        if not self.stack:
            return 1
        else:
            return 0
        
    def size(self):
        return self.long
        
    def push(self,num):
        self.stack.append(num)
        self.long += 1
    
    def pop(self):
        if self.isEmpty() == 1:
            return -1
        else:
            self.long -= 1
            return self.stack.pop(-1)
    
    def top(self):
        if self.isEmpty() == 1:
            return -1
        else:
            return self.stack[-1]
        
class Queue:
    
    def __init__(self):
        self.queue = []
        self.long = 0
    def isEmpty(self):
        if not self.queue:
            return 1
        else:
            return 0
        
    def size(self):
        return self.long
        
    def enqueue(self,num):
        self.queue.append(num)
        self.long += 1
    
    def dequeue(self):
        if self.isEmpty() == 1:
            return -1
        else:
            self.long -= 1
            return self.queue.pop(0)
    
    def front(self):
        if self.isEmpty() == 1:
            return -1
        else:
            return self.queue[0]
        
    def back(self):
        if self.isEmpty() == 1:
            return -1
        else:
            return self.queue[-1]
        
n,v,start = map(int,sys.stdin.readline().rstrip().split(" "))

s = Stack()
q = Queue()
adj = []
dfs_order = []
bfs_order = []
visited = []

for i in range(n+1):
    visited.append(False)
    adj.append([])
    
for i in range(v):
    a,b = map(int,sys.stdin.readline().rstrip().split(" "))
    adj[a].append(b)
    adj[b].append(a)
    
for ad in adj:
    ad.sort()
    ad.reverse()
    
num = start
s.push(num)

while True:
    num = s.pop()
    
    if visited[num] == False:
        dfs_order.append(num)
        visited[num] = True
        for i in adj[num]:
            s.push(i)
            
    if s.isEmpty():
        break

for i in range(n+1):
    visited[i] = (False)

for ad in adj:
    ad.reverse()
    
num = start
q.enqueue(num)

while True:
    
    num = q.dequeue()
    
    if visited[num] == False:
        bfs_order.append(num)
        visited[num] = True
        for i in adj[num]:
            q.enqueue(i)
    
    if q.isEmpty():
        break
        
for order in dfs_order:
    if order != dfs_order[-1]:
        print(order,end=' ')
    else:
        print(order)

for order in bfs_order:
    if order != bfs_order[-1]:
        print(order,end=' ')
    else:
        print(order)

