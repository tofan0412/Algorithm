# SILVER2
# 최장 감소 수열을 구하면 된다.
# dp[i] : arr[i]를 포함하는 최장 감소 수열의 길이를 뜻한다.

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
dp[0] = 1 # 자기 자신을 포함하므로..

for i in range(1, n):
    for j in range(0, i):
        if arr[i] < arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))
