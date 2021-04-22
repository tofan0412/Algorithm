def charge(idx, capacity):
    global cnt
    if idx == N: # 도착했으므로 종료한다.
        return
    # 남은 거리 안에 도착 지점이 없는 경우에는 충전해야 한다.
    # 남은 이동 거리와 충전량을 비교해봐야 한다.
    elif idx+capacity < N-1:
        # capacity 거리 이내에서 가장 큰 곳에서 충전해야 한다.
        max_gap = 0
        max_idx = 0
        left_distance = capacity
        for i in range(idx+1, idx+capacity+1):
            left_distance -= 1
            if charge_info[i] - left_distance >= max_gap:
                max_gap = charge_info[i] - left_distance
                max_idx = i
        cnt += 1
        charge(max_idx, charge_info[max_idx])
    # 남은 거리 안에 도착 지점이 있는 경우에는 충전안해도 된다.
    else:
        return cnt


T = int(input())
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    charge_info = info[1:]
    charge_info.append(0)
    cnt = 0

    charge(0, charge_info[0])
    print(f'#{tc} {cnt}')