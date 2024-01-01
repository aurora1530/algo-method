N = int(input())
A = list(map(int, input().split()))

counter = [0]*(5 * (10**5)+1)
max_num = 5 * (10**5)
max_count = 0
for a in A:
    counter[a] += 1
    if counter[a] == max_count and max_num > a:
        max_num = a
    if counter[a] > max_count:
        max_count = counter[a]
        max_num = a
print(max_num)
