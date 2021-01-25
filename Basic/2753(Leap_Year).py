import sys

year = int(sys.stdin.readline().rstrip())

if year % 400 == 0:
    print(1)
    sys.exit()
if year % 4 == 0 and year % 100 != 0:
    print(1)
    sys.exit()

print(0)
    
