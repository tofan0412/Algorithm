# GOLD5
n, k = map(int, input().split())
coins = []
for _ in n:
    coins.append(int(input()))

dp = [0] * (k + 1)
# k부터 시작해서, n가지 Action을 취할 수 있다.
def solution(number, route):
    if number == 0:


    if dp[number] != 0:
        return dp[number]

    for coin in coins:
        if number - coin > 0:
            solution(number, route + str(coin))
