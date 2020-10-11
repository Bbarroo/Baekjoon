import sys

def getValue(a,b,i):
    return int(100*(b+i)/(a+i)) - int(100*b/a), int(100*(b+i+1)/(a+i+1)) - int(100*b/a)

numbers = sys.stdin.readline().rstrip()
numbers = numbers.split(" ")
a = int(numbers[0])
b = int(numbers[1])

if int(100*b/a) >= 99:
    print(-1)
    sys.exit()
    
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
        # print(b/a,(b+idx)/(a+idx),(b+idx+1)/(a+idx+1)) #see the result
        check = False
        break
    elif val1 > 0:
        high = idx - 1

if check: print(-1)