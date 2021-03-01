import sys


def check():
    phones= {}
    seperated_phone = {}
    n_phone = int(sys.stdin.readline().rstrip())
    check = True
    for _ in range(n_phone):
        phone = str(sys.stdin.readline().rstrip())
        for idx in range(len(phone)):
            if not check:
                break
            if idx != len(phone)-1:
                seperated_phone[phone[:idx+1]] = True
                if phones.get(phone[:idx+1]) is not None:
                    check = False
            else:
                if seperated_phone.get(phone[:idx+1]) is not None:
                    check = False
                else:
                    seperated_phone[phone[:idx+1]] = True
                    phones[phone[:idx+1]] = True
    if not check:
        return "NO"
    return "YES"
        
n_input = int(sys.stdin.readline().rstrip())

for _ in range(n_input):
    print(check())