import sys
import math

class Segment_Tree:
    
    def __init__(self,lst):
        
        n = int(math.log(len(lst),2))
        self.lst = lst
        self.tree = []
        for i in range(2 ** (n+2) + 1):
            self.tree.append(-1)
        self.makeTree(0,len(lst)-1,1)
        
    def makeTree(self,first,end,idx):
        if first == end:
            self.tree[idx] = self.lst[first]
            
            return self.tree[idx]
        
        mid = int((first+end)/2)
        self.tree[idx] = self.makeTree(first,mid,idx * 2) + self.makeTree(mid+1,end,idx * 2 + 1)
        
        return self.tree[idx]
    
    def sum_recur(self,start,end,idx,left,right):
        if left > end or right < start:
            return 0
        elif left <= start and right >= end:
            return self.tree[idx]
        mid = int((start + end)/2)
        sum_def = self.sum_recur(start,mid,idx*2,left,right) + self.sum_recur(mid+1,end,idx*2+1,left,right)
        return sum_def
    
    def sum(self,left,right):
        return self.sum_recur(0,len(self.lst)-1,1,left-1,right-1)
    
    def changeValue_recur(self,start,end,idx,target_idx,target):
        valued = lst[target_idx]
        lst[target_idx] = target
        delta = target - valued
        
        if target_idx > end or target_idx < start:
            return 0
        
        self.tree[idx] += delta
        if start == end: 
            return 0 
        mid = int((start + end)/2)
        self.changeValue_recur(start,mid,idx*2,target_idx,target)
        self.changeValue_recur(mid+1,end,idx*2+1,target_idx,target)
        return self.tree[idx]
    
    def changeValue(self,target,change_num):
        return self.changeValue_recur(0,len(self.lst)-1,1,target-1,change_num)
    
    def showTree(self):
        print(self.tree)

            
a = sys.stdin.readline().rstrip()
fir, sec, thi = a.split(" ")
lst = []
fir = int(fir)
sec = int(sec) + int(thi)
for i in range(fir):
    num = int(sys.stdin.readline().rstrip())
    lst.append(num)

t = Segment_Tree(lst)
for i in range(sec):
    nums = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    if nums[0] == 1:
        t.changeValue(nums[1],nums[2])
    elif nums[0] == 2:
        print(t.sum(nums[1],nums[2]))