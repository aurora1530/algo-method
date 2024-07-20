# 1 + 2 + … + N
import sys
sys.setrecursionlimit(10**6)

N = int(input())


def rec_sum(x: int) -> int:
    if x == 0:
        return 0
    return rec_sum(x-1) + x


print(rec_sum(N))
