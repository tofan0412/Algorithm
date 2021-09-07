for tc in range(1, 11):
    tc_num = int(input())
    # list를 이용한 큐
    queue = list(map(int, input().split()))
    cycle = 5
    factor = False
    while not factor:
        # 1번의 사이클동안 진행한다.
        for i in range(1, cycle+1):
            t = queue.pop(0)
            t -= i
            queue.append(t)
            # 만약 맨 뒤에 붙인 수가 0과 같거나 0보다 작다면, 사이클을 종료한다.
            if t <= 0:
                # 가장 마지막 값을 0으로 변경해야 한다.
                queue[-1] = 0
                factor = True
                break

    # 여기에 왔다는 건, while을 탈출했다는 의미이다.
    result = ""
    for number in queue:
        result += str(number) + ' '
    print(f'#{tc_num} {result}')

