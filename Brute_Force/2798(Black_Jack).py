import sys

a = sys.stdin.readline().rstrip()
nums = sys.stdin.readline().rstrip()
nums = nums.split(" ")
n,m = a.split(" ")

nums = sorted(list(map(int, nums)))


n = int(n)
m = int(m)

fir = 0
sec = 1
thi = 2
sum_calc = 0
while fir < n - 2:
    sec = fir + 1
    while sec < n - 1:
        thi = sec + 1
        while thi < n:
            sum_temp =sum([nums[fir],nums[sec],nums[thi]])
            if sum_temp > m:
                break          
            if (m - sum_temp) < (m - sum_calc):
                sum_calc = sum_temp          
            thi += 1
        sec += 1
    fir += 1
print(sum_calc)
   