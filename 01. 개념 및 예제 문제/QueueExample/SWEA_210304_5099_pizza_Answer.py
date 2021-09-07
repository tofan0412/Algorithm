T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N은 화덕이 한번에 구울 수 있는 피자의 최대 개수, M은 피자의 개수
    pizza = list(map(int, input().split()))

    firepot = []

    for i in range(N):
        firepot.append((i+1, pizza[i]))

    # 피자를 N번부터 넣어야 한다.
    next_pizza = N
    last_pizza = -1

    while firepot:
        num, cheese = firepot.pop(0)

        cheese //= 2
        last_pizza = num
        # 치즈의 양이 남아있다면
        if cheese:
            firepot.append((num, cheese))
        else: # 치즈가 다 녹은 것을 의미한다.
            if next_pizza < M: # 우리가 아직 넣어야 할 피자가 남아있다는 것을 뜻한다.
                firepot.append((next_pizza + 1, pizza[next_pizza]))
                next_pizza += 1

    print("#{} {}".format(tc, last_pizza))
