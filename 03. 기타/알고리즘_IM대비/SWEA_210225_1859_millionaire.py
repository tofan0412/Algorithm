T = int(input())

for tc in range(1,T+1):
    N = int(input()) # 연속된 N일 동안

    price = list(map(int,input().split()))

    day = 0 # 기준 인덱스
    max_idx = 9999 # 최대값의 인덱스
    max_value = 0 # 최대값

    buy_num = 0 # 산 물건의 개수
    buy_price = 0 # 산 물건의 가격의 총합
    benefit = 0

    while day < len(price):
        if day == max_idx:  # 가장 비싼 날에는 모든 구매한 물건을 판매한다.
            benefit += (price[day] * buy_num) - buy_price
            day += 1 # 구매한 날은 넘어간다.
            # 구매 내역을 다시 초기화한다.
            buy_num = 0
            buy_price = 0

        max_value = 0  # 최대값을 여러번 찾을 수 있으므로, 반드시 초기화를 해줘야 한다.
        max_idx = 0

        if day == len(price) - 1:
            break

        # 가장 비싼 날이 언제인지 파악하기.
        for i in range(day, len(price)):
            if price[i] > max_value:
                max_value = price[i]
                max_idx = i
        # 최대값이 있는 인덱스까지는 계속 구매한다.
        for j in range(day, max_idx):
            buy_num += 1
            buy_price += price[j]
            day += 1  # 기준 인덱스를 증가시킨다.
    print(f'#{tc} {benefit}')




