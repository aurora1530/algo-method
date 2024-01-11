led_statuses = [
    "1110111", "0100100", "1011101", "1101101", "0101110",
    "1101011", "1111011", "0100111", "1111111", "1101111"
]

N, M = map(int, input().split())


before = int(led_statuses[N], base=2)
after = int(led_statuses[M], base=2)

print(before ^ after)
