N = int(input())
L = list(map(int, input().split()))

L.sort()


counter = 0

for i in range(0, N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if L[i] + L[j] > L[k]:
                counter += 1

print(counter)
