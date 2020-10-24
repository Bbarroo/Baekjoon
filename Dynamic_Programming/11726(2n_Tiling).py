import math
import sys
class Fib:
    def __init__(self):
        self.memo = []
        for i in range(1001):
            self.memo.append(-1)
        self.memo[0] = 1
        self.memo[1] = 1
        
    def fib(self,n):
        
        a = 0
        b = 0
        
        if n <= 1:
            return self.memo[n]
        
        else:
            if self.memo[n-2] == -1:
                b = self.fib(n-2)
                self.memo[n-2] = b
            else:
                b = self.memo[n-2]
                
            if self.memo[n-1] == -1:
                a = self.fib(n-1)
                self.memo[n-1] = a
            else:
                a = self.memo[n-1]         

            return a+b
        
num = int(sys.stdin.readline().rstrip())
fib = Fib()

print(int(fib.fib(num)%10007))


