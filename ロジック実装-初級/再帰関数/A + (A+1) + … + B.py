# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

A, B = map(int, input().split())


def sum_rec(start: int, end: int) -> int:
    if end - start == 0:
        return end
    return sum_rec(start, end - 1) + end


print(sum_rec(A, B))
