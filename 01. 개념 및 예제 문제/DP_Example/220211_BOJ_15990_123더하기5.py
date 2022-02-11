# SILVER2
# 이전 문제와 동일하지만, 같은 수를 두번 연속해서 사용해선 안된다.
# 시간 초과 발생 -> 2차원 배열로 생각해야 한다.
t = int(input())
# col=0은 앞에서 뺀 수가 1일 때, col=1d은 앞에서 뺀 수가 2일 때, col=2는 앞에서 뺀 수가 3일 때, col=4는 최종적으로 나오는 경우의 수
dp = [[0, 0, 0, 0] for _ in range(100001)]
dp[1][0] = 0
dp[1][1] = 1
dp[1][2] = 1
dp[1][3] = sum(dp[1][0:3]) // 2

dp[2][0] = 1
dp[2][1] = 0
dp[2][2] = 1
dp[2][3] = sum(dp[2][0:3]) // 2

dp[3][0] = 2
dp[3][1] = 2
dp[3][2] = 2
dp[3][3] = sum(dp[3][0:3]) // 2

for num in range(4, 100001):
    # 앞에서 뺀 수가 1이고, 남은 수가 num일 때
    dp[num][0] = dp[num - 2][1] + dp[num - 3][2]
    dp[num][3] += dp[num][0]
    # 앞에서 뺀 수가 2이고, 남은 수가 num일 때
    dp[num][1] = dp[num - 1][0] + dp[num - 3][2]
    dp[num][3] += dp[num][1]
    # 앞에서 뺀 수가 3이고, 남은 수가 num일 때
    dp[num][2] = dp[num - 1][0] + dp[num - 2][1]
    dp[num][3] += dp[num][2]

    dp[num][3] = dp[num][3] // 2 % 1000000009

for tc in range(t):
    n = int(input())

    print(dp[n][3])
