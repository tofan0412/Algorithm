# SILVER5
# 탁자 위에 돌 N개가 있다.
# 상근이와 창영이는 턴을 번갈아 가면서 돌을 가져가며, 돌은 1개 or 3개 가져갈 수 있다.
# 마지막 돌을 가져가는 사람이 이기게 된다.
memo = [''] * 1001 # 돌이 N개 있을 때, 이기는 사람을 기록해 둔다.
N = int(input())
memo[1] = 'SK' # 1개 있으므로, 무조건 상근이가 이긴다.
memo[2] = 'CY'
memo[3] = 'SK'
memo[4] = 'CY'

stones = 5

# 상근이와 창영이는 본인의 차례에 돌을 1개 빼거나, 3개 빼는 행동만을 할 수 있다.
while True:
    if stones > N:
        break

    if memo[stones-1] == memo[stones-3] == 'SK':
        memo[stones] = 'CY'
    elif memo[stones-1] == memo[stones-3] == 'CY':
        memo[stones] = 'SK'

    stones += 1
print(memo[N])

