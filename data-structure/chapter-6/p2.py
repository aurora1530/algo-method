B = 30
M = 1000003


def charToNumber(char: str):
    return ord(char)-ord('a') + 1


def rolling_hash(word: str):
    result = 0
    word_l = len(word)
    for i in range(word_l):
        result += charToNumber(word[word_l - 1 - i]) * (B**i)
    return result % M


N = int(input())
S = input().split()

max = 0
counter = [0] * (M)

for word in S:
    hashed_word = rolling_hash(word)
    counter[hashed_word] += 1
    if counter[hashed_word] > max:
        max = counter[hashed_word]

print(max)
