# SILVER2
# BFS와 DP로 풀 수 있다. DP의 경우 <2579 계단오르기>를 참고하자.
N = int(input())
arr = list(map(int, input().split()))

# dp[k]의 정의 : k번째 발판까지 점프점프하면서 올때, 가능한 최소한의 점프 수.
dp = [-1] * N
dp[0] = 0

# 생각하지 못한 점 : 반례 -> 0 / 0 0 0 1 0. 처음 발판부터 시작해서 올 수 있어야지, 중간부터 올 수는 없다.
for i in range(1, N):
    candidates = [] # i번째 발판에 점프해서 넘어올 수 있는 후보군
    for j in range(0, i):
        if arr[j] >= i - j and dp[j] != -1:
            candidates.append(dp[j])

    # 만약 후보가 없을 경우..?
    if len(candidates) == 0:
        dp[i] = -1
    else:
        dp[i] = min(candidates) + 1

print(dp[N-1])
