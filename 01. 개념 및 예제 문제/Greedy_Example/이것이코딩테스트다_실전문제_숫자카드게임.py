'''
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
단 게임의 룰을 지키며 카드를 뽑아야 하며, 룰은 다음과 같다.
1. N x M 형태로 카드가 놓여져 있다
2. 먼저 row를 선택한다.
3. 그 다음 선택된 행에서 가장 숫자가 낮은 카드를 뽑아야 한다.
4. 따라서 처음에 row를 선택할 때, 이후에 해당 row에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.
'''

N, M = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(N)]

# 각 row 별로 최소값을 찾아본다.
result = list()
for i in range(N):
    row_min_value = 10001
    for j in range(M):
        if cards[i][j] <= row_min_value:
            row_min_value = cards[i][j]
    # 한 row에 대한 최솟값을 찾았다.
    result.append(row_min_value)

# 이제 result에서 가장 작은 값을 출력하면 된다.
print(max(result))

