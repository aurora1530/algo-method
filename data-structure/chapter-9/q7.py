H = int(input())

max_bottom_v = 2 ** H  # 最下層の頂点の最大値
min_bottom_v = 1
# H-1までの数
num_above_H = sum([2 ** n for n in range(H)])

print(*[num_above_H + min_bottom_v, num_above_H+max_bottom_v])
