# 노선수가 주어진다.
tc_num = int(input())
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇번의 충전을 해야 종점에 도착할 수 있을까 ?
for tc in range(1, tc_num + 1):
    info = list(map(int, input().split()))
    # 첫번째는 최대 이동할 수 있는 정류장 수,
    move_cnt = info[0]
    # 두번째는 전체 정류장의 수
    station_num = info[1]
    # 세번째는 충전기가 설치된 정류장의 개수이다.
    charger_num = info[2]

    charger_info = list(map(int, input().split()))
    charge_cnt = 0
    for station in range(0, station_num + 1): # 0,1,2,3,4,5,6,...9,10

        # 충전기가 있는 정류장에 도착한 경우 : 충전할 지 , 말지를 판단해야 한다.
        # 남은 move_cnt 와 충전기가 있는 정류장 간의 간격을 비교해야 한다.
        if station in (charger_info):
            # 현재 충전횟수로 마지막 정류장까지 갈 수 있다면
            if move_cnt >= station_num - station:
                pass
            # 마지막으로 충전기가 있는 정류장에 도착했을 때 : 다음으로 충전기가 있는 곳은 없다.
            if station == charger_info[-1]:
                if move_cnt < station_num - station:
                    charge_cnt += 1
                    move_cnt = info[0]
                    continue

            # 마지막 정류장까지 갈 수는 없지만, 다음 충전기가 있는 정류장까진 갈 수 있다면
            elif move_cnt >= charger_info[charger_info.index(station)+1] - station:
                pass
            # 다음 충전기가 있는 정류장까지 남은 이동횟수로 갈 수 없다면? 충전해야 한다.
            else:
                charge_cnt += 1 # 충전횟수 + 1
                move_cnt = info[0]
                # 충전을 했는데, 다음 충전기가 있는 정류장까지 3회의 이동횟수로 도달할 수 없다면..?
                if move_cnt < charger_info[charger_info.index(station)+1] - station:
                    charge_cnt = 0
                    break
        move_cnt -= 1

    print(f'#{tc} {charge_cnt}')