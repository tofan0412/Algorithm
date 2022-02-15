# SILVER2
# BFS와 DP로 풀 수 있다. DP의 경우 <2579 계단오르기>를 참고하자.
N = int(input())
arr = list(map(int, input().split()))

# dp[k]의 정의 : k번째 발판까지 점프점프하면서 올때, 가능한 최소한의 점프 수.
dp = [100001] * N
dp[0] = 0

# 내가 기존에 생각했던 점: top - down 형식으로 생각했다면..
# dp 풀이는 bottom - up 방식으로 생각했다는 점이다.
for now in range(0, N): # now는 현재 위치
    # 현재 위치 기준으로 점프해서 이동할 수 있는 모든 범위에 대해 생각한다.
    for jump in range(arr[now]+1):
        # 점프해서 간 곳의 최소 회수는 해당 칸의 기존 점프 회수와 현재 칸에서 +1한 점프회수를 비교한다.

        # 점프해서 갈 수 있는 칸이 존재해야 한다.
        if now + jump < N:
            dp[now+jump] = min(dp[now + jump], dp[now] + 1)

if dp[N-1] == 100001:
    print(-1)
else:
    print(dp[N-1])

