T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split())) # 1일, 한달, 3달, 1년 이용권 요금
    plan = list(map(int, input().split())) # 1월 ~ 12월까지의 수영장 이용 계획

    kind = [0] * 12 # 0은 1일권, 1은 1달권, 2는 3달권, 3은 1년권, -1은 안함
    numbers = [0] * 12
    personal_costs = [0] * 12 # 달달이 비용을 적어둔다.
    # 각 인덱스 별로 리스트를 넣는다. [이용권 종류, 끊은 갯수] 순으로 한다.

    # 일단, 1일 이용권을 이용할 것인지, 1달 이용권을 이용할 것인지를 판별하자.
    for i, frequency in enumerate(plan): # 수영장 가는 빈도..!
        cost_day = frequency * costs[0] # 1일 이용권으로 끊었을 때의 비용
        if cost_day > costs[1]: # 한달 이용권을 끊는다.
            kind[i] = 1
            numbers[i] += 1
        elif frequency == 0:
            kind[i] = -1
        else:
            kind[i] = 0
            numbers[i] += frequency
        personal_costs[i] = numbers[i] * costs[kind[i]]

    # print(personal_costs)
    # 이제, 3달 이용권으로 바꿀 구간이 있는지를 판별한다.
    for i in range(len(kind)-2):
        cost_total = 0
        if kind[i] != 0 and kind[i+1] != 0 and kind[i+2] != 0:
            cost_total += personal_costs[i]
            cost_total += personal_costs[i+1]
            cost_total += personal_costs[i+2]

            if cost_total > costs[2]:
                # 해당 3달은 3달 이용권으로 변경한다.
                # 3달의 kind는 모두 2로 수정하고, 티켓의 개수는 가운데에만 표기한다.
                kind[i], kind[i+1], kind[i+2] = 2, 2, 2
                numbers[i] = 0
                numbers[i+1] = 1
                numbers[i+2] = 0
                personal_costs[i+1] = numbers[i+1] * costs[kind[i+1]]

    # 마지막으로 지금까지 사용한 1일 이용권, 한달 이용권, 3달 이용권과 비용을 합해서
    # 1년 이용권과 비교한다.
    if sum(personal_costs) > costs[3]:
        print(f'#{tc} {costs[3]}')
    else:
        print(f'#{tc} {sum(personal_costs)}')








