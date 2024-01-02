N = int(input())
S = input().split()


base_char_num = ord('a')


def charToNumber(char: str):
    num = ord(char)
    return num - base_char_num+1


base = 30
max_char_num = charToNumber('z')


def wordToNumber(word: str):
    sum = 0
    for i in range(1, len(word)+1):
        sum += charToNumber(word[-i]) * (base ** (i-1))
    return sum


counter = [0] * (max_char_num*(base ** 3 + base **
                 2 + base ** 1 + base ** 0 + 1))

for word in S:
    counter[wordToNumber(word)] += 1

Q = int(input())

for _ in range(Q):
    word = input()
    print(counter[wordToNumber(word)])
