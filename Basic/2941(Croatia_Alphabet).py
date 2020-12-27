import sys

text = list(sys.stdin.readline().rstrip())

cnt = 0
for t in range(len(text)):
    if text[t] == 'z':
        if text[t-1] == 'd':
            cnt += 1
            
print(int((len(text) - 3 * cnt) /2) + cnt)
        