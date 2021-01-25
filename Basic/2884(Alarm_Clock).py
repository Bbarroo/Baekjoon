import sys

times = sys.stdin.readline().rstrip()
times = times.split(" ")

time = int(times[0]) * 60 + int(times[1]) + 1395

hour = int(time/60) % 24
minute = time % 60

print(hour,minute)

