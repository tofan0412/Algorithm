# SILVER3
N = int(input())
memo = [0] * (N + 1)
t, p = [], []
for _ in range(N):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

print(memo[N])
