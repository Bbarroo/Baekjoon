import sys

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
        
    def get_max(self):
        return max(i[0] for i in self.queue)
        
cnt = int(sys.stdin.readline().rstrip())

for _ in range(cnt):
    q = Queue()
    
    n_order,check = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    orders = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    
    for i in range(n_order):
        
        if i == check:
            q.enqueue([orders[i],1])
        else: 
            q.enqueue([orders[i],0])
        cnt = 1

    while q.isEmpty() != True:
        temp = q.dequeue()

        if q.isEmpty():
            if temp[1] == 1:
                print(cnt)
            break
        if temp[0] < q.get_max():
            q.enqueue(temp)
        else:

            if temp[1] == 0: 
                cnt += 1
            else:
                print(cnt)
                break
        
    
    
    
    