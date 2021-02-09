# 노선수가 주어진다.
tc_num = int(input())
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇번의 충전을 해야 종점에 도착할 수 있을까 ?
for tc in range(1, tc_num + 1):
    # 노선 정보를 받는다.
    line_info = list(map(int, input().split()))
    # line_info[0] : 충전 후 최대 이동가능 거리,
    # line_info[1] : 정류장 수,
    # line_info[2] : 충전소가 설치된 정류장의 수
    charge_stop = list(map(int, input().split())) # 충전소가 있는 정류장의 index 정보이다.

    # 버스 출발
    charger_visit_cnt = 0 # 버스가 지나간 충전소가 있는 정류장을 카운트.
    charge_cnt = 0 # 버스가 충전한 회수를 카운트
    movable_distance = line_info[0]

    for bus_stop in range(0, line_info[1] + 1): # 정류장의 수는 0까지 있으므로 +1해야 한다.
        # bus_stop은 현재 버스가 들른 정류장을 의미한다.

        # 만약 movable_distance가 음수이면 도착할 수 없다는 것을 의미한다.
        if movable_distance < 0:
            charge_cnt = 0
            break

        #출발하기 전에, 만약 버스가 충전소가 있는 정류장에 있다면
        if bus_stop in charge_stop:
            # 2가지를 판단해야 한다.
            # 1. 다음 충전소가 있는 경우 - 충전소가 있는 정류장의 개수를 알고 있다.
            charger_visit_cnt += 1 # 방문하였으므로 +1해준다.
            if charger_visit_cnt < line_info[2]:
                # 이동 가능 거리가 다음 충전소를 가는데 필요한 거리보다 크거나 같다면 : 충전할 필요가 없다.
                if movable_distance >= charge_stop[charge_stop.index(bus_stop) + 1] - charge_stop[charge_stop.index(bus_stop)]:
                    pass
                # 이동 가능 거리가 다음 충전소를 가는데 필요한 거리보다 작다면 : 충전해야 한다.
                else:
                    movable_distance = line_info[0] # 충전!
                    charge_cnt += 1

            # 2. 다음 충전소가 없는 경우
            if charger_visit_cnt == line_info[2]:
                # 현재 이동 가능 거리와, 남은 거리를 비교한다.
                # 남은거리까지 현재 이동 가능 거리로 도달할 수 없는 경우
                if movable_distance < line_info[1] - bus_stop:
                    charge_cnt = 0 # 충전 횟수에 0을 주고 for문을 끝낸다.
                    break
                # 충전소는 없지만, 현재 이동 가능 거리로 마지막까지 도착할 수 있는 경우
                else:
                    pass

        # 마지막으로, 다음 정류장까지 이동해야 하므로, 이동 가능 거리에서 -1

        movable_distance -= 1

    # 마지막으로 출력한다 .
    print(f'#{tc} {charge_cnt}')