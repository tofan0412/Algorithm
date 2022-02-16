# SILVER3
# 완벽하게 게임을 한다는 건, 이길 수 있는 경우의 수가 있다면 그 경우의 수만 놓는다는 의미이다.

n = int(input())
dp = ['' for _ in range(1001)]
dp[1] = 'SK'
dp[2] = 'CY'
dp[3] = 'SK'
dp[4] = 'SK'
dp[5] = 'SK'
dp[6] = 'SK'
dp[7] = 'CY'
dp[8] = 'SK'

for i in range(9, n+1):
    # SK이가 승리할 수 있는 경우의 수가 하나라도 있다면

    # 상근이가 먼저 시작하므로, dp[i-1], dp[i-3], dp[i-4]에서 차례는 창영이다.
    # 1. 상근이가 i개의 돌에서 1개를 뺸 경우 -> 창영이는 i-1개의 돌에서 1,3,4개를 뺄 수 있다.
    case1 = i - 1
    case2 = i - 3
    case3 = i - 4
    # 1,3,4개를 뺀 이후 남은 돌의 dp[]를 판단해야 한다.
    if dp[case1-1] == 'SK' or dp[case1-3] == 'SK' or dp[case1-4] == 'SK':
        dp[i] = 'SK'
    # 2. 상근이가 i개의 돌에서 3개를 뺸 경우
    elif dp[case2-1] == 'SK' or dp[case2-3] == 'SK' or dp[case2-4] == 'SK':
        dp[i] = 'SK'
    # 3. 상근이가 i개의 돌에서 4개를 뺸 경우
    elif dp[case3-1] == 'SK' or dp[case3-3] == 'SK' or dp[case3-4] == 'SK':
        dp[i] = 'SK'
    else:
        dp[i] = 'CY'

print(dp[n])
