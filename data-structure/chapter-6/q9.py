N = int(input())
S = input().split()


# used_char_count = [0]*26 # [0]:aが使われた個数、[1]:bが使われた個数...

counter = {}  # key:val key=''.join(list(map(str,used_char_count))),val 個数


def charToNum(char: str) -> int:
    return ord(char)-ord('a')


for word in S:
    used_char_count = [0]*26
    for char in word:
        char_num = charToNum(char)
        used_char_count[char_num] += 1
    key = ''.join([str(i) for i in used_char_count])
    counter[key] = counter.get(key, 0) + 1

bottom = N*(N-1)
top = sum([n*(n-1) for n in counter.values()])
print(top/bottom)
