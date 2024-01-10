N = int(input())
num_flag = 30

result = []
for i in range(num_flag):
    ans = N & 1 << i
    if ans == 0:
        continue
    result.append(i)
print(len(result))
print(*result)
