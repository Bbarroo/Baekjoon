import sys

cnt = int(sys.stdin.readline().rstrip())

for i in range(cnt):
    text = sys.stdin.readline().rstrip()
    engs,num = text.split("-")
    
    result = 0
    
    for cnt, eng in enumerate(engs):
        result += (ord(eng)-65) * (26 ** (2 - cnt))
    result -= int(num)
    
    if abs(result) > 100:
        print("not nice")
    else:
        print("nice")
    