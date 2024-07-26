S = input()


def main():
    for i in range(1, len(S)):
        if S[i-1] == S[i]:
            return True

    return False


print('Yes' if main() else 'No')
