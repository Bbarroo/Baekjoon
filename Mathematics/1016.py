import sys

min_n, max_n = list(map(int, sys.stdin.readline().rstrip().split(' ')))

max_root = int(pow(max_n,0.5))

num_lst = []
check_lst = []

for i in range(min_n,max_n+1):
    num_lst.append(i)
    check_lst.append(1)

for i in range(2,max_root+1):
    prime = i**2
    if min_n % prime == 0:
        min_num = 0
    else:
        min_num = (int(min_n/prime) + 1) * prime - min_n

    while min_num < len(num_lst):
        check_lst[min_num] = 0
        min_num += prime

print(sum(check_lst))
