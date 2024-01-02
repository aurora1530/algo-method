X = input()
N = int(input())
S = input().split()


stack = []

operator = ['+', '-', '*']

for char in S:
    if char in operator:
        right_num: int = stack.pop(-1)
        left_num: int = stack.pop(-1)
        if char == '+':
            push_num = left_num + right_num
        elif char == '-':
            push_num = left_num - right_num
        else:
            push_num = left_num * right_num
        stack.append(push_num)
    else:
        stack.append(int(char))

print(f"{X}={stack[0]}")
