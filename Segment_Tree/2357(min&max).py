import sys
import math

class maxsTree:

    def __init__(self,lst):
        
        n = int(math.log(len(lst),2))
        self.lst = lst
        self.tree = []
        for i in range(2 ** (n+2) + 1):
            self.tree.append(-1)
        self.makeTree(0,len(lst)-1,1)

    def makeTree(self,start,end,idx):
        if start == end:
            self.tree[idx] = self.lst[start]
            
            return self.tree[idx]
        
        mid = int((start+end)/2)
        self.tree[idx] = max(self.makeTree(start,mid,idx * 2),self.makeTree(mid+1,end,idx * 2 + 1))
        
        return self.tree[idx]

    def showTree(self):
        print(self.tree)
    
    def getMax(self,first,last):
        return self.getMaxrec(first,last,1,len(self.lst),1)

    def getMaxrec(self,first,last,start,end,idx):
        if first <= start and last >= end:
            return self.tree[idx]
        elif first > end or last < start:
            return 0
        mid = int((start + end)/2)
        return max(self.getMaxrec(first,last,start,mid,2*idx),self.getMaxrec(first,last,mid+1,end,idx*2+1))


class minsTree:

    def __init__(self,lst):
        
        n = int(math.log(len(lst),2))
        self.lst = lst
        self.tree = []
        for i in range(2 ** (n+2) + 1):
            self.tree.append(-1)
        self.makeTree(0,len(lst)-1,1)

    def makeTree(self,start,end,idx):
        if start == end:
            self.tree[idx] = self.lst[start]
            
            return self.tree[idx]
        
        mid = int((start+end)/2)
        self.tree[idx] = min(self.makeTree(start,mid,idx * 2),self.makeTree(mid+1,end,idx * 2 + 1))
        
        return self.tree[idx]

    def showTree(self):
        print(self.tree)
    
    def getMin(self,first,last):
        return self.getMinrec(first,last,1,len(self.lst),1)

    def getMinrec(self,first,last,start,end,idx):
        if first <= start and last >= end:
            return self.tree[idx]
        elif first > end or last < start:
            return 1000000001
        mid = int((start + end)/2)
        res = min(self.getMinrec(first,last,start,mid,2*idx),self.getMinrec(first,last,mid+1,end,idx*2+1))
        return res
n,m = map(int,sys.stdin.readline().rstrip().split(" "))

lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))

mint = minsTree(lst)
maxt = maxsTree(lst)
for _ in range(m):
    s,d = map(int,sys.stdin.readline().rstrip().split(" "))
    print(mint.getMin(s,d),end = ' ')
    print(maxt.getMax(s,d))

