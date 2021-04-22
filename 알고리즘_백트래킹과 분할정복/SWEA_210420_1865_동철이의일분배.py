import sys
sys.stdin = open("input.txt", "r")


# 이 때 idx는 row를 의미한다.
def checkProb(person, percents):
    global max_percents
    if percents <= max_percents:
        return

    if person == N:
        # 기존의 확률합보다 크다면
        if percents > max_percents:
            max_percents = percents
            return

    for job in range(N):
        # 아직 일 하지 않았다면
        if worked[job] == 0:
            worked[job] = 1
            tmp = percents
            percents *= prob[person][job] / 100
            checkProb(person+1, percents)
            worked[job] = 0
            percents = tmp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prob = [list(map(int, input().split())) for _ in range(N)]
    # 일을 누군가 수행했는지를 나타내는 컬럼이다.
    worked = [0] * N
    max_percents = 0

    checkProb(0, 1)
    print('#{} {:0.6f}'.format(tc, max_percents * 100))
