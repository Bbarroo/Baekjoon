import sys

def find(lst,target):
    start = 0
    end = len(lst)
    while start < end:
        mid = int((start + end)/2)
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid
        elif lst[mid] < target:
            start = mid + 1
    return mid

cnt,target = map(int,sys.stdin.readline().rstrip().split(" "))

trees = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    
trees.sort()

gathered = 0
gathered_bef = 0
idx = 0
start = 0
end = trees[-1]
while True:
    mid = int((start + end) / 2)
    idx = find(trees,mid+1)
    idx_bef = find(trees,mid+2)
    
    if idx < len(trees):
        if trees[idx] > mid:
            gathered = sum(trees[idx:]) - mid * (len(trees) - idx)
        elif trees[idx] <= mid:
            gathered = sum(trees[idx+1:]) - mid * (len(trees) - idx-1)
    if idx_bef < len(trees):      
        if trees[idx_bef] > (mid+1):
            gathered_bef = sum(trees[idx_bef:]) - (mid+1) * (len(trees) - idx_bef)
        elif trees[idx_bef] <= (mid+1):
            gathered_bef = sum(trees[idx_bef+1:]) - (mid+1) * (len(trees) - idx_bef-1)
    print(gathered,gathered_bef,start,end)
    if gathered >= target:
        if gathered_bef >= target:
            start = mid + 1
        elif gathered_bef < target:
            print(mid)
            break
    if gathered < target:
        end = mid



