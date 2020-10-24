import math
import sys
class Fib:
    def __init__(self):
        self.lst = []
        for i in range(41):
            self.lst.append([-1,-1,-1])
        self.lst[0] = [0,1,0]
        self.lst[1] = [1,0,1]
        
    def fib(self,n):
        
        a = [0,0,0]
        b = [0,0,0]
        
        if n <= 1:
            return self.lst[n]
        
        else:
            if self.lst[n-1][0] == -1:
                a = self.fib(n-1)
                self.lst[n-1] = a
            else:
                a = self.lst[n-1]
            
            if self.lst[n-2][0] == -1:
                b = self.fib(n-2)
                self.lst[n-2] = b
            else:
                b = self.lst[n-2]
            
            res = []
            for i in range(3):
                res.append(a[i] + b[i])

            return res
        
nums = int(sys.stdin.readline().rstrip())
fib = Fib()

for i in range(nums):
    num = int(sys.stdin.readline().rstrip())
    res = fib.fib(num)
    print(res[1],res[2])


