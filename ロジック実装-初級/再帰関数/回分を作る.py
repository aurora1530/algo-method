N = int(input())
X = input()


def rec(i: int) -> str:
    if i == 0:
        return X[i]
    return rec(i-1) + X[i] + rec(i-1)


print(rec(N - 1))
