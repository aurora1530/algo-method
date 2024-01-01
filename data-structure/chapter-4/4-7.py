class Runner:
    def __init__(self, num):
        self.fore = None
        self.back = None
        self.num = num
        self.is_drop = False

    def drop(self):
        self.is_drop = True


def overtake(runner: Runner):
    fore_runner = runner.fore
    if fore_runner is None or runner.is_drop:
        return 'Error'
    fore_runner_num = fore_runner.num

    back_runner = runner.back
    if back_runner is not None:
        back_runner.fore = fore_runner
    if fore_runner.fore is not None:
        fore_runner.fore.back = runner

    # 入れ替え
    runner.fore = fore_runner.fore  # fore_runner.foreがNoneのときも含む
    runner.back = fore_runner
    fore_runner.fore = runner
    fore_runner.back = back_runner  # back_runnerがNoneのときも含む

    return fore_runner_num


def dropout(runner: Runner):
    runner.drop()
    fore_runner = runner.fore
    back_runner = runner.back
    if fore_runner is None and back_runner is None:
        return
    if back_runner is not None:
        back_runner.fore = fore_runner
    if fore_runner is not None:
        fore_runner.back = back_runner
    return


N = int(input())
A = list(map(int, input().split()))
Q = int(input())

runners = [Runner(i) for i in range(N)]
for i in range(N):
    runner_num = A[i]
    runners[runner_num].fore = None if i == 0 else runners[A[i-1]]
    runners[runner_num].back = None if i == N-1 else runners[A[i+1]]

for i in range(Q):
    query, v = map(int, input().split())
    if query == 0:
        print(overtake(runners[v]))
    else:
        dropout(runners[v])
