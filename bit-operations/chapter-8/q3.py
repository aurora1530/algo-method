X = list(map(int, input().split()))

ans = [[] for _ in range(8)]
for i in range(8):
    x = X[i]
    for j in range(7, -1, -1):
        # j番目が立っているかどうかを調べる
        flag1 = x & (1 << (2*j))
        flag2 = x & (1 << (2*j+1))
        ans[i].append('.' if (flag1 == 0 and flag2 == 0)
                      else 'x' if (flag1 == 0 and flag2 != 0) else 'o')
    print(''.join(ans[i]))
