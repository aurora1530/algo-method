from typing import Set
N = int(input())
A = list(map(int, input().split()))
A.append(0)

set_score: Set[int] = set()

for a0 in A:
    for a1 in A:
        for a2 in A:
            score = a0 + a1 + a2
            set_score.add(score)

print(len(set_score))
