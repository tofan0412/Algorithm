T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N은 화덕이 한번에 구울 수 있는 피자의 최대 개수, M은 피자의 개수
    ci = list(map(int, input().split()))
    # ci는 피자 치즈의 양을 정보로 갖고 있는 리스트이다.
    pizzas = []
    for i in range(len(ci)):
        pizza = [i+1, ci[i]] # pizza는 피자번호와 치즈의 양을 갖는다.
        pizzas.append(pizza)

    queue = [] # 화덕
    order = [] # 피자를 구운 순서
    # 가장 먼저 화덕에 N개만큼의 피자를 queue에 담는다.
    for i in range(N):
        t = pizzas.pop(0)
        queue.append(t)

    cycle = 0 # 회전수를 나타내는 변수
    while len(order) != M: # 화덕에 피자가 남아있는 동안 계속 반복한다.
        # 먼저 피자 위 치즈가 모두 녹았는지를 확인하고, 녹았으면 뺀다.
        # 이 때 queue의 가장 첫번째만 확인할 수 있다.
        if queue[0][1] == 0:
            # 남은 피자가 있으면 넣는다.
            if len(pizzas) > 0:
                t = queue[0]
                order.append(t[0])  # 빼낸 피자 순서를 기록한다.
                queue[0] = pizzas.pop(0) # 새로운 피자를 넣는다.
            else: # 남은 피자가 없으면 그냥 빼낸다.
                # 이 때, 중요한 점 : 해당 자리를 그냥 공백으로 채워야 한다.
                t = queue[0]
                queue[0] = ['F', 'F'] # 자리는 채워둬야 한다.
                order.append(t[0])

        # 피자를 회전 시키자.
        t = queue.pop(0)
        queue.append(t)
        cycle += 1
        if cycle == N:
            # 1바퀴를 돌았으므로 모든 피자의 치즈의 양을 절반으로 줄인다.
            for j in range(len(queue)):
                if type(queue[j][1]) == int:
                    queue[j][1] = queue[j][1] // 2
                else: # 다 구운 피자의 경우에는 하지 않는다.
                    pass
            # 사이클 초기화
            cycle = 0

    print(f'#{tc} {order[-1]}')






