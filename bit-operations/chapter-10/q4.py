N = int(input())
W = input().split()


def is_pangram(text: str) -> bool:
    for char_num in range(ord('a'), ord('z')+1):
        char = chr(char_num)
        if char not in text:
            return False
    return True


min_word = -1
for S in range(2**N):
    word_list = [w for idx, w in enumerate(W) if S & 1 << idx != 0]
    if is_pangram(''.join(word_list)):
        length = len(word_list)
        if length < min_word or min_word == -1:
            min_word = length
print(min_word)
