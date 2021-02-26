import sys

n_input = int(sys.stdin.readline().rstrip())
marble_input = list(map(int,sys.stdin.readline().rstrip().split(" ")))
n_check = int(sys.stdin.readline().rstrip())
marble_check = list(map(int,sys.stdin.readline().rstrip().split(" ")))

result = []

for check in marble_check:
    checked = {check:True}
    result.append("N")
    for marble in marble_input:
        if checked.get(marble):
            result[-1] = "Y"
            break
        for key in list(checked.keys()):
            checked[key+marble] = True
            checked[key-marble] = True
            checked[marble-key] = True

for i in result:
    if i == result[-1]:
        print(i)
    else:
        print(i,end=" ")        

