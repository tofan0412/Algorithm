# SILVER2
# 최장 증가 부분 수열 구하라는 거잖아...
n = int(input())
arr = list(map(int, input().split()))

# 1. dp[k] 정의 : arr[k]를 포함하는 LIS의 길이
dp = [1] * n #1로 하는 이유: 자기 자신부터 시작할 경우도 있기 때문에...

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

