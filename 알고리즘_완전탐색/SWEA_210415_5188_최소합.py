def findWay(start, val):
    global result
    # start에서 한쪽에만 플러스를 하거나, 양쪽에 모두 플러스를 하는 것이 곧 이동하는 것이다.
    if start == [N-1, N-1]: # 도착했다는 것을 뜻한다.
        result.append(val)
        # print("이 길의 합계는 {}".format(val))
        return
    else:
        move_to_row = start[0] + 1
        move_to_col = start[1] + 1

        check1 = 0 <= move_to_col < N # 가로방향 이동 가능한가?
        check2 = 0 <= move_to_row < N # 세로방향 이동 가능한가?
        # 1. col 방향으로만 이동하거나
        if check1:
            start[1] = move_to_col
            sum_now = val + arr[start[0]][start[1]]
            findWay(start, sum_now)
            start[1] -= 1
        # 2. row 방향으로만 이동하거나
        if check2:
            start[0] = move_to_row
            sum_now = val + arr[start[0]][start[1]]
            findWay(start, sum_now)
            start[0] -= 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = [0, 0]
    end = [N - 1, N - 1]
    result = []

    findWay(start, arr[0][0])

    print(f'#{tc} {min(result)}')