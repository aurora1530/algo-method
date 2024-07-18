X = int(input())
A = list(map(int, input().split()))
values = [50, 10, 5, 1]

count = 0

for i, v in enumerate(values):
    need_amount = X // v
    if need_amount <= A[i]:
        X -= v * need_amount
        count += need_amount
    else:
        X -= v * A[i]
        count += A[i]

print(count)
