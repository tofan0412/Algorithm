# SILVER5
# 탁자 위에 돌 N개가 있다.
# 상근이와 창영이는 턴을 번갈아 가면서 돌을 가져가며, 돌은 1개 or 3개 가져갈 수 있다.
# 마지막 돌을 가져가는 사람이 이기게 된다.

n = int(input())
dp = [['', ''] for _ in range(n+1)]

# 상근이 차례에, 남은 돌의 개수가 0개 일때
dp[0][0] = 'SK' # 상근이 차례에 남은 돌의 개수가 0개
dp[0][1] = 'CY' # 창영이 차례에 남은 돌의 개수가 0개
dp[1][0] = 'CY'
dp[1][1] = 'SK'

for i in range(2, n+1):
    # 남은 돌의 개수가 i개이고, 차례가 상근이일 때
    dp[i][0] = dp[i-1][1]
    # 남은 돌의 개수가 i개이고, 차례가 창영일 때
    dp[i][1] = dp[i-1][0]

print(dp[n][0])
