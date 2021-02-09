case = int(input())
for tc in range(1, case+1):
    #버스 노선 수
    N = int(input())
    # 그 다음은 해당 노선이 다니는 정류장 번호의 범위가 나온다. 이 때 노선 수 N에 따라 반복되어야 한다.
    bus_lines = []
    for i in range(0, N):
        bus_line = list(map(int, input().split())) # 만약 [200, 4500] 이면 200번 ~ 4500번 정류장을 모두 지난다는 뜻이다.
        bus_lines.append(range(bus_line[0], bus_line[1]+1))

    bus_stops = int(input()) # P개의 버스 정류장
    bstop_cnt = [0] * bus_stops
    # 이제부터 각 정류장의 정류장 번호가 나온다. ( P개의 버스 정류장 )
    # P개만큼 입력을 받아야 한다. (각 버스 정류장의 고유 번호 )

    bstop_name = [0] * bus_stops
    for stop in range(0, bus_stops):
        bstop_name[stop] = int(input())

    # 입력을 다하면 bstop_name은 다음과 같이 작성된다.
    # [1,2,3,4,5]

    for i, stop in enumerate(bstop_name):
        # 각 버스 번호가 노선에 있는지 없는지를 계산해야 한다.
        for line in bus_lines: # line은 [1,2,3] , [2,3,4,5] 와 같이 된다.
            if stop in line:
                bstop_cnt[i] += 1

    result = ''
    for cnt in bstop_cnt:
        result += str(cnt) + ' '
    print(f'#{tc} {result}')