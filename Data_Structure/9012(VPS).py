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
        

cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    checkVPS = sys.stdin.readline().rstrip()
    
    s = Stack()
    isRight = True
    for vps in checkVPS:
        if vps == "(":
            s.push(1)
        elif vps == ")":
            if s.pop() == -1:
                isRight = False
    if s.isEmpty() == 0:
        isRight = False
    if isRight:
        print("YES")
    else:
        print("NO")