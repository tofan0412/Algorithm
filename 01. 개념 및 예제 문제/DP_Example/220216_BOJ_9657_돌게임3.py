# SILVER3
# 완벽하게 게임을 한다는 건, 이길 수 있는 경우의 수가 있다면 그 경우의 수만 놓는다는 의미이다.
n = int(input())

# dp[i]의 정의 : 상근이든 창영이든, 내 차례에 남은 돌의 개수가 i개일 때 내가 이길 수 있는지의 여부를 나타낸다(한 가지 경우라도 내가 이길 수 있는 경우의 수가 있다면 1이다).
# 1은 이길 수 있는 것이고 0은 이길 수 없는 것이다.
dp = [0 for _ in range(1001)]

dp[1] = 1
dp[2] = 0 # 내 차례에 돌이 2개 있다면 절대 이길 수 없음
dp[3] = 1
dp[4] = 1

for stone in range(5, n+1):
    # 만약 상대방이 상대방 차례에 stone-1개의 돌을 가지고 있을 때 상대방이 이길 수 있는 경우의 수가 0개라면? 내가 이기는 것이다. (모든 경우가 자신이 이기는 경우이기 때문에)
    if not dp[stone-1]:
        dp[stone] = 1
    if not dp[stone-3]:
        dp[stone] = 1
    if not dp[stone-4]:
        dp[stone] = 1

if dp[n] == 1:
    print('SK') # 시작은 상근이가 하기 때문에
else:
    print('CY')




