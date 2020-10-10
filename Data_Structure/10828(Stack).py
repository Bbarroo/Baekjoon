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
        
s = Stack()
cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    order = sys.stdin.readline().rstrip()
    
    if " " in order:
        target = int(order.split(" ")[1])
        s.push(target)
    else:
        if order == "pop":
            print(s.pop())
        elif order == "size":
            print(s.size())
        elif order == "empty":
            print(s.isEmpty())
        elif order == "top":
            print(s.top())
        