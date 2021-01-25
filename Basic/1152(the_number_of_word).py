import sys

text = list(sys.stdin.readline().rstrip())

cnt = 0

for i,t in enumerate(text):
    if i == 0:
        if t != " ":
            cnt += 1
    else:
        if t != " " and text[i-1] == " ":
            cnt += 1
print(cnt)