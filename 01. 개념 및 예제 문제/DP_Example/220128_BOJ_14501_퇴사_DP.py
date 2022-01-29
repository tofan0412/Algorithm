# SILVER3
# DP를 활용하여 풀어보자.

# 1. N일에 상담을 진행한 경우 Pay는 N+1일에 받는다.
N = int(input())
t, p = [], []
for _ in range(N):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

t = [0] + t + [0]
p = [0] + p + [0]
memo = [0] * (N + 2)
# 따라서 첫날은 무조건 0이다. (전날 일을 한 내역이 없으므로)

# N+1일까지 해줘야 한다.
for today in range(1, N+2):
    # 돈을 정산받는 N+1일인 경우 2가지로 나뉜다.
    # 1. N일까지 상담을 진행해서 N+1일에 정산을 받는 경우
    # 2. N일 이전에 상담이 끝나 이미 정산이 끝난 경우
    tmp = [0]
    factor = False
    for before_day in range(1, today):
        if before_day + t[before_day] == today:
            factor = True
            result = max(memo[today-1], memo[before_day] + p[before_day])
            tmp.append(result)

    # 만약 해당되는 before_day가 없다면? 전날 정산받은 금액 고대로 가져온다. (매우 중요...!!)
    if len(tmp) == 1:
        memo[today] = memo[today-1]
    else:
        memo[today] = max(tmp)
print(memo[N+1])
