# SILVER2
t = int(input())
dp = [0] * 1000001
dp[1] = 1 % 1000000009
dp[2] = 2 % 1000000009
dp[3] = 4 % 1000000009
dp[4] = 7 % 1000000009

history = 4
for tc in range(t):
    n = int(input())

    if n <= history:
        print(dp[n])
        continue
    else:
        for num in range(history+1, n+1):
            dp[num] = (dp[num-1] + dp[num-2] + dp[num-3]) % 1000000009
        history = n
        print(dp[n])
