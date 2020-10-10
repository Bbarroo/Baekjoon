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
pipes = sys.stdin.readline().rstrip()
cnt = 0
piped = "("
for pipe in pipes:
    if pipe == "(":
        s.push("(")
    elif pipe == ")":
        s.pop()
        if piped == ")":
            cnt += 1
        else:
            cnt += s.size()
    piped = pipe
print(cnt)