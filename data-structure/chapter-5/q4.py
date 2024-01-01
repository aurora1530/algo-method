N = int(input())

start_num = ord('a')
char_exists = [0] * 26

words = input().split()

for word in words:
    chars = list(word)
    for char in chars:
        char_exists[ord(char)-start_num] = 1

print('Yes' if sum(char_exists) == 26 else 'No')
