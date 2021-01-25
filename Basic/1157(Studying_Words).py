import sys
text = sys.stdin.readline().rstrip()
text = list(text.upper())
check = {}

for t in text:
    if t in check:
        check[t] += 1
    else:
        check[t] = 1
        
check = sorted(check.items(),key=lambda x: x[1], reverse = True)
if len(check) > 1:
    if check[0][1] == check[1][1]:
        print("?")
    else:
        print(check[0][0])
else:
    print(check[0][0])