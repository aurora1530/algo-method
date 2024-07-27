N = int(input())

str_to_count = {}

S = input().split()


max_key = ''
max_count = 0

for s in S:
    str_to_count.setdefault(s, 0)
    str_to_count[s] += 1

    if str_to_count[s] == max_count and s < max_key:
        max_key = s
    if str_to_count[s] > max_count:
        max_count = str_to_count[s]
        max_key = s

print(max_key)
