# 동전의 종류는 6가지. 동전을 생산하는 공장
# 최소 비용으로 그 금액만큼 동전을 생산하고자 한다. 
# 각 단위로 생산할 수 있는 금액까지 최대로 생산을 했을 때, 필요한 비용을 계산
def solution(money, costs):  # money는 생산해야 하는 금액, costs는 생산 단가 리스트
    coins = [1, 5, 10, 50, 100, 500]
    answer = 0  # 최종 정답

    while True:
        # 종료 조건 : 남은 money가 없다면..
        if money == 0:
            break

        min_cost = int(1e9)
        rest_money = int(1e9)

        for i in range(6):  # costs는 1원, 5원, 10원, 100원, 500원
            # 1. 각 단위 동전당 필요한 개수 계산
            cnt = money // coins[i]
            rest = money % coins[i]
            # 2. 각 단위 동전당 필요한 금액 계산
            total_cost = cnt * costs[i]
            # 3. 최소 생산 금액 구하기
            if min_cost > total_cost and cnt > 0:
                min_cost = total_cost
                rest_money = rest

        # 여기로 오면 각 동전당 필요한 생산 비용 중, 그 비용이 최소인 동전이 결정된다.
        answer += min_cost
        money = rest_money
    return answer


# print(solution(1999, [2,11, 20, 100, 200, 600]))
print(solution(4578, [1, 4, 99, 35, 50, 1000]))
