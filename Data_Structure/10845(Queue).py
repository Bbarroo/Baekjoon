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
        
    def push(self,num):
        self.queue.append(num)
        self.long += 1
    
    def pop(self):
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
        
q = Queue()
cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    order = sys.stdin.readline().rstrip()
    
    if " " in order:
        target = int(order.split(" ")[1])
        q.push(target)
    else:
        if order == "pop":
            print(q.pop())
        elif order == "size":
            print(q.size())
        elif order == "empty":
            print(q.isEmpty())
        elif order == "front":
            print(q.front())
        elif order == "back":
            print(q.back())
        
        