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

# Answer
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)
    for i in charge:
        bus_stop[i] = 1
    bus = 0 # 버스의 위치
    ans = 0 # 충전 회수

    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자.
        bus += K
        if bus >= N : break # 종점에 도착하거나 종점지보다 더 나아간 경우

        for i in range(bus, bus-K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus = i
                break
            # 충전기를 못 찾았을 때
        else: # for에 대한 else문이다. for문을 수행하고 수행한다.
            ans = 0
            break

    print(f'#{tc} {ans}')

# Answer2
# 들어온 정류장만을 가지고 판단할 수는 없을까..?
# 예를 들어 다음과 같이 만들자.
# [0,1,3,5,7,9,10]
# 이동 가능 거리를 3이라고 했을 때
# 0(시작점) + 3 > 1 : 이 충전소는 넘어간다.
# 0 + 3 = 3 : 이 충전소는 넘어간다.
# 0 + 3 < 5 : 이 충전소까진 갈 수 없다. 따라서 last라는 변수에 이전 정류장 위치 3을 저장한다.

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    ans = 0

    charge = [0] + charge + [N]
    # 아래와 같은 코드
    # charge.insert(0,0)
    # charge.append(N)

    last = 0
    # 충전소에 출발점과 도착지를 넣어놓았으므로
    for i in range(1, M+2): # M+2는 charge의 길이와 같다. (0과 N을 추가했으므로..)
        if charge[i] - charge[i-1] > K: # 다음 충전소까지 갈 수 없다..
            ans = 0
            break
        # 다음 충전소까지 갈 수 있으면 아무 작업도 하지 않는다.
        # 갈 수 없다면 내 바로 직전 충전소로 위치를 옮기고 충전 회수 +1
        if charge[i] > last + K:
            last = charge[i-1]
            ans += 1

    print(f'#{tc} {ans}')