N = int(input())
A = list(map(int, input().split()))

max_a = max(A)

counter = 0
for a in A:
    if a == max_a:
        counter += 1

print(counter)
