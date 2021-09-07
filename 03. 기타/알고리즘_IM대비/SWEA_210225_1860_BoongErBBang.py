T = int(input())
for tc in range(1, T+1):
    # N : 붕어빵 사는 사람수, M : 진기가 붕어빵 만드는데 걸리는 시간, K : M초동안 만든 붕어빵의 수
    N,M,K = list(map(int,input().split()))
    customer = list(map(int,input().split()))

    # 먼저, 손님이 오는 시간대를 오름차순으로 정렬하자.
    # Bubble sort
    for i in range(len(customer)):
        for j in range(len(customer)-1):
            if customer[j] > customer[j+1]:
                customer[j], customer[j+1] = customer[j+1], customer[j]
    # N초에 복수의 사람이 올 수 있다.

    time = 0 # 시간초를 카운트할 변수
    bbang_cnt = 0 # 만든 빵의 개수를 카운트할 변수
    customer_cnt = 0 # N초에 오는 사람의 수를 카운트할 변수
    result = "Possible"
    while N > 0:
        # 경과한 시간초가 M의 배수이면 : K만큼의 붕어빵을 만든 것이다.
        if time % M == 0 and time != 0:
            bbang_cnt += K

        # 해당 시간에 몇명이 방문했는지를 카운트한다.
        customer_cnt = 0 # 매초마다 방문하는 손님의 개수가 다르므로 초기화
        for i in customer:
            if time == i:
                customer_cnt += 1

        # 현재 빵의 개수에서 방문한 손님수만큼의 빵의 개수를 제외한다.
        bbang_cnt -= customer_cnt
        N -= customer_cnt
        if bbang_cnt < 0: # 음수이면 Impossible
            result = "Impossible"
            break
        time += 1
    print(f'#{tc} {result}')







