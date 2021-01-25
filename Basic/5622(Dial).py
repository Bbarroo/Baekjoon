import sys
texts = sys.stdin.readline().rstrip()

result = 0
for text in texts:
    result += 3
    ascii_text = ord(text) - 65
    if ascii_text < 15:
        result += int(ascii_text/3)
    elif ascii_text < 19:
        result += 5
    elif ascii_text < 22:
        result += 6
    else:
        result += 7

print(result)