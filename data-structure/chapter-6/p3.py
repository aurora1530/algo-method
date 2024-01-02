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


table = [0] * M


class Node:
    def __init__(self, x=''):
        self.nex = None
        self.val = x


for i in range(M):
    nil = Node()
    nil.nex = nil
    table[i] = nil

Q = int(input())

for _ in range(Q):
    query, T = input().split()
    if query == '0':
        hx = rolling_hash(T)
        insert_node = Node(T)
        current_table_node = table[hx]
        insert_node.nex = current_table_node.nex
        current_table_node.nex = insert_node
    elif query == '1':
        hx = rolling_hash(T)
        now_node = table[hx]
        while (1):
            if now_node.nex.val == T:
                target_node = now_node.nex
                break
            else:
                now_node = now_node.nex
            if now_node.nex == now_node:
                break
        now_node.nex = target_node.nex
    else:
        hx = rolling_hash(T)
        now_node = table[hx]
        while (1):
            if now_node.nex.val == T:
                print('Yes')
                break
            else:
                now_node = now_node.nex
            if now_node.nex.val == '':
                print('No')
                break
