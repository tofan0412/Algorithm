'''
6개의 동전이 있다. 각각의 동전을 생산하는데는 일정한 비용이 발생한다.
최소 비용으로 그 금액만큼 동전을 생산하고자 한다.
목표 금액 money와 1원, 5원, 10원, 50원, 100원, 500원에 대한 생산 비용 정보가 담긴 costs 리스트가 제공된다.
각 동전의 개수는 충분하다고 가정한다. 목표금액을 만들기 위해 필요한 최소 생산 비용을 계산하시오.
'''

# 1원당 생산비용으로 변환해서 생각하면 된다.
def solution(money, costs):
    INF = int(1e9)
    # 1. money가 0이 아닐때까지 반복한다.
    value = []
    # result는 현재까지 발생된 생산비용의 합을 뜻한다.
    result = 0
    for i in range(len(costs)):
        value.append(costs[i] / coins[i])
    while money != 0:
        # idx는 최저 생산 비용에 해당하는 동전의 인덱스이다.
        idx = value.index(min(value))
        # cnt는 해당 동전으로 money를 거슬러 줄 때 발생하는 동전의 개수이다.
        cnt = money // coins[idx]

        # 만약 해당 동전으로 거슬러 줄 수 없는 경우..
        if cnt == 0:
            value[idx] = INF
            continue
        else:
            money -= cnt * coins[idx]
            result += cnt * costs[idx]

    return result


coins = [1, 5, 10, 50, 100, 500]
print(solution(1999, [2, 11, 20, 100, 200, 600]))
print(solution(4578, [1, 4, 99, 35, 50, 1000]))
