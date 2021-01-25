import math
import sys

class Sum_ott:
    def __init__(self):
        self.lst = []
        for i in range(11):
            self.lst.append(-1)
        self.lst[0] = 1
        self.lst[1] = 1
        self.lst[2] = 2

    def get_howm_sums(self,num):
        if self.lst[num] == -1:
            self.lst[num] = self.get_howm_sums(num-1) + self.get_howm_sums(num-2) + self.get_howm_sums(num-3)
        return self.lst[num]
    
cnt = int(sys.stdin.readline().rstrip())
so = Sum_ott()
for _ in range(cnt):
    num = int(sys.stdin.readline().rstrip())
    print(so.get_howm_sums(num))
    