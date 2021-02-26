import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):

    n_student = int(sys.stdin.readline().rstrip())
    students = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    visited_student = {}
    matched = 0

    for i in range(1,n_student+1):
        temp_choosed_lst = []
    
        if visited_student.get(i):
            continue
        temp_choosed = {}
        pick = i

        while True:
            visited_student[pick] = True
            temp_choosed_lst.append(pick)
            temp_choosed[pick] = len(temp_choosed)
            picked = students[pick-1]

            if temp_choosed.get(picked) != None:
                idx = temp_choosed[picked]
                matched += len(temp_choosed_lst) - idx
                break

            if visited_student.get(picked) != None:
                break

            pick = picked

    print(n_student - matched)