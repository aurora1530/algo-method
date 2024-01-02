N = int(input())

A = list(map(int, input().split()))

stack = [{'index': 0, 'score': 0}]  # key:val,key=day,val:score

# tail.value < val ならば、tailのkey。valをpush.
# tail.value >= valならば、tailはいらないのでpop. tail.value<valとなる値を見つけるまでpop.その後、valをpush.

for i in range(1, N):
    now_score = A[i]
    tail_score = stack[-1]
    if tail_score['score'] < now_score:
        print(i - tail_score['index'])
        stack.append({'index': i, 'score': now_score})
    else:
        stack.pop()
        while (1):
            if stack[-1]['score'] < now_score:
                print(i - stack[-1]['index'])
                stack.append({'index': i, 'score': now_score})
                break
            else:
                stack.pop()
