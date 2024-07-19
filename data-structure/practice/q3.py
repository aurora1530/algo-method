N = int(input())

A = list(map(int, input().split()))

a_counter = {}

for a in A:
    a_counter[a] = a_counter[a] + 1 if a in a_counter else 1


counter = 0
for key, value in a_counter.items():
    diff = value - key
    counter += diff if diff >= 0 else value

print(counter)
