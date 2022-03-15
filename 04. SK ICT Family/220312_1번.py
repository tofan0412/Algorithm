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
