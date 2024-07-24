N = 30

work_times = [list(map(int,input().split())) for _ in range(N)]

total_minutes = 0

for times in work_times:
    minutes = times[3] + times[2] * 60 - times[1] - times[0] * 60
    if minutes > 480:
        minutes -= 60
    elif minutes > 360:
        minutes -= 45
    total_minutes += minutes

h = total_minutes // 60
m = total_minutes % 60

print(h,m)