N, X, Y = list(map(int, input().split()))

intersection = X & Y
union = X | Y
print(intersection, union)
