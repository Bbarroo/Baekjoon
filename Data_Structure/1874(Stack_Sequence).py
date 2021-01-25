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
calc_lst = []
top = 0
for i in range(cnt):
    num = int(sys.stdin.readline().rstrip()) 
    if num > s.top():
        for k in range(top+1,num+1):
            s.push(k)
            calc_lst.append("+")
        s.pop()
        calc_lst.append("-")
        top = num
    elif num == s.top():
        s.pop()
        calc_lst.append("-")
    else:
        print("NO")
        sys.exit()
for i in calc_lst:
    print(i)
