import sys

value = int(sys.stdin.readline().rstrip())

a = 1
b = 2

result = []
while a<=50000:
    if b ** 2 - a ** 2 == value:
        result.append(b)
        b += 1
    elif b ** 2 - a**2 > value:
        a += 1
    else:
        b += 1
if not result:
    print (-1)
for i in result:
    print(i)