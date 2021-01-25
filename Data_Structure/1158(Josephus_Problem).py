import sys

texts = sys.stdin.readline().rstrip()

howm,term = texts.split(" ")
howm = int(howm)
term = int(term)

people = list(range(1,howm+1))

cnt = -1
removed_people =[]

while people:
    cnt += term
    cnt = cnt % len(people)
    
    removed_people.append(people.pop(cnt))
    cnt -= 1

print("<",end="")
for i in enumerate(removed_people):
    if i[0] != len(removed_people)-1:
        print(str(i[1]),end=", ")
    else:
        print(str(i[1]),end=">")