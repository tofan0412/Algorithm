# GOLD5
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# Memoization을 위한 dp 리스트를 먼저 정의하자. dp[K]는 금액 K원에 대한 가능한 경우의 수를 뜻한다.
dp = [0] * 10001

credits = 1 # k = 1인 경우부터 시작한다.


for i in range(credits, k+1):
    # 이전 과정들이 중복되지 않았다는 가정 하에..
    dp[i] =  




