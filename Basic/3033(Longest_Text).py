import sys
global n, texts, mod
n = int(sys.stdin.readline().rstrip())
texts = sys.stdin.readline().rstrip()
mod = 999983
base = 31
n_table = []
n_table.append(1)
for i in range(1,n):
    n_table.append(n_table[i-1] * base % mod)

def pattern_match(idx1, idx2, M):
    global texts
    for i in range(M):
        if texts[idx1+i] != texts[idx2+i]: return False
    return True


result = 0
def check(length):
    global n, texts, mod
    hash_table = {}
    num = n - length + 1
    h = 0
    for i in range(length):
        h *= base
        h += ord(texts[i])
        h %= mod
    hash_table[h] = [0]
    for i in range(1,num):
        h -= ord(texts[i-1])*n_table[length-1] % mod
        h = h % mod
        h *= base
        h += ord(texts[i+length-1])
        h %= mod
        if hash_table.get(h):
            for h_t in hash_table[h]:
                if pattern_match(i,h_t,length):
                    return True
            hash_table[h].append(i)
        else:
            temp_lst = [i]
            hash_table[h] = temp_lst
    return False

low = 0
high = n-1
result = 0
while low <= high: 
    mid = int((low+high)/2)
    if check(mid):
        result = mid
        low = mid + 1
    else:
        high = mid -1

print(result)