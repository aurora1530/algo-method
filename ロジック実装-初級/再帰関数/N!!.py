# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10**6)

N = int(input())


def prod(num: int) -> int:
    if num <= 0:
        return 1
    return num * prod(num - 2)


print(prod(N))
