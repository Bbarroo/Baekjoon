import sys

length = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().strip()

mod = 999983
base = 31
n_table = []
n_table.append(1)
for i in range(1, length):
    n_table.append(n_table[-1] * base % mod)

lo = 0
hi = length
max_len = 0
while lo <= hi:
    mid = (lo + hi) // 2
    found = False
    h = 0
    power = 1
    hash_table = {}

    for i in range(length - mid + 1):
        if i == 0:
            for j in range(mid):
                h = ((h * base) + (ord(string[i + j]) - ord('a'))) % mod
        else:
            h = (h - (ord(string[i-1]) - ord('a')) * n_table[mid - 1] % mod) % mod
            h *= base
            h += (ord(string[i + mid - 1]) - ord('a'))
            h %= mod
        if h in hash_table:
            for start in hash_table[h]:
                found = True
                for t in range(mid):
                    if string[i + t] != string[start + t]: found = False
                if found: 
                    max_len = max_len if max_len > mid else mid
                    break
            hash_table[h].append(i)
        else:
            hash_table[h] = [i]

    if found: lo = mid + 1
    else: hi = mid - 1

print(max_len)