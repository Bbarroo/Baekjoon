import sys
import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i  == 0 :
            return False
    return True
n = int(sys.stdin.readline().rstrip())

sqrt_n = int(math.sqrt(n)) + 1
lst = {}
for i in range(1,sqrt_n):
    if n % i == 0:
        if isPrime(i):
            lst[i] = True
        ied = n // i
        if isPrime(ied):
            lst[ied] = True

res = n
for i in lst.keys():
    res *= 1-1/i

print(int(res))
    