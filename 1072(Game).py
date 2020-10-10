import sys

def getValue(a,b,i):
    return int((b+i)/(a+i)*100) - int(b/a*100), int((b+i+1)/(a+i+1)*100) - int(b/a*100)

numbers = sys.stdin.readline().rstrip()
numbers = numbers.split(" ")
a = int(numbers[0])
b = int(numbers[1])
lim = int(a**2/(99*a-100*b))+1

lst = []

low = 0
high = lim
check = True
while low <= high:
    idx = int((low+high)/2)  
    val1,val2 = getValue(a,b,idx)
    if val1 == 0 and val2 == 0:
        low = idx+1
    elif val1 == 0 and val2 > 0:
        print(idx+1)
        print(b/a,(b+idx)/(a+idx),(b+idx+1)/(a+idx+1)) #see the result
        check = False
        break
    elif val1 > 0:
        high = idx - 1

if check: print(-1)