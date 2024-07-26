
a, b = map(int, input().split())


def main():
    if a == b:
        return 'No'

    a_total = 0
    b_total = 0

    for i in range(1, max(a, b)):
        if i < a and a % i == 0:
            a_total += i
        if i < b and b % i == 0:
            b_total += i

    if a_total != b:
        return 'No'
    if b_total != a:
        return 'No'
    return 'Yes'


print(main())
