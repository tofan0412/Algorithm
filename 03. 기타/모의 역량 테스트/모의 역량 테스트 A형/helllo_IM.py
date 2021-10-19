# 2021.03.17 삼성 모의 역량 테스트 A형

# 1번.
# 삼성에서 개발한 최신 모바일 프로세서 렉시노스는 가로 N개, 세로 N개의 cell로 구성되어 있다.
# 1개의 cell에는 1개의 Core 혹은 1개의 전선이 올 수 있다.
# 렉시노스의 가장 자리에는 전원이 흐르고 있다.
# core와 전원을 연결하는 전선은 직선으로만 설치가 가능하며,
# 전선은 절대로 교차해서는 안된다.
# 렉시노스의 가장자리에 위치한 core는 이미 전원이 연결된 것으로 간주한다.

# 최대한 많은 Core에 전원을 연결하였을 경우, 전선 길이 합을 구하고자 한다.
# 단, 여러 방법이 있을 경우 전선 길이의 합이 최소가 되는 값을 구하라.

def check(arr, row, col):
    global lines
    way = ['up', 'down', 'left', 'right']
    up_range = range(0, row)
    down_range = range(row+1, len(arr))
    left_range = range(0, col)
    right_range = range(col+1, len(arr))

    for up in up_range:
        if arr[up][col] == '1':
            way.remove('up')
            break
    for down in down_range:
        if arr[down][col] == '1':
            way.remove('down')
            break
    for left in left_range:
        if arr[row][left] == '1':
            way.remove('left')
            break
    for right in right_range:
        if arr[row][right] == '1':
            way.remove('right')
            break

    if len(way) == 1:
        # 연결해야 한다.
        arr[row][col] = 'C'
        if way[0] == 'up':
            for i in up_range:
                arr[i][col] = 'T'
                lines += 1
        if way[0] == 'down':
            for i in down_range:
                arr[i][col] = 'T'
                lines += 1
        if way[0] == 'left':
            for i in left_range:
                arr[row][i] = 'T'
                lines += 1
        if way[0] == 'right':
            for i in right_range:
                arr[row][i] = 'T'
                lines += 1

def calc(arr, row, col):
    global lines
    global cores
    if cores == 0: # 연결 가능한 코어가 없으면
        return
    # 4방향을 비교하고, 그 중에서 가장 짧은 곳에 연결한다.
    up_range = range(0, row)
    down_range = range(row + 1, len(arr))
    left_range = range(0, col)
    right_range = range(col + 1, len(arr))
    line_cnt = [0, 0, 0, 0]

    for up in up_range:
        if arr[up][col] == '0':
            line_cnt[0] += 1
        else: # 이미 연결된 전선이거나, 다른 코어가 가로막고 있는 경우..
            line_cnt[0] = 9999
            break
    for down in down_range:
        if arr[down][col] == '0':
            line_cnt[1] += 1
        else:
            line_cnt[1] = 9999
            break
    for left in left_range:
        if arr[row][left] == '0':
            line_cnt[2] += 1
        else:
            line_cnt[2] = 9999
            break
    for right in right_range:
        if arr[row][right] == '0':
            line_cnt[3] += 1
        else:
            line_cnt[3] = 9999
            break

    # 이제, 연결할 수 있는 방향 중 가장 짧은 방향을 선택하여 그 방향을 전선으로 연결한다.
    lines += min(line_cnt)
    if line_cnt.index(min(line_cnt)) == 0:
        for up in up_range:
            arr[up][col] = 'T'

    if line_cnt.index(min(line_cnt)) == 1:
        for down in down_range:
            arr[down][col] = 'T'

    if line_cnt.index(min(line_cnt)) == 2:
        for left in left_range:
            arr[row][left] = 'T'

    if line_cnt.index(min(line_cnt)) == 3:
        for right in right_range:
            arr[row][right] = 'T'

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rexinos = [input().split() for _ in range(N)]
    # 전선은 가로 방향 또는 세로 방향으로만 가능하다.
    cores = 0 # 전선을 연결해야 할 코어의 개수
    lines = 0 # 연결한 전선의 개수

    # 존재하는 코어의 개수 counting
    for row in range(N):
        for col in range(N):
            if rexinos[row][col] == '1':
                cores += 1

    # 가장 먼저 사이드에 존재하는 코어를 연결했다는 표시로 전환한다.
    for row in range(N):
        for col in range(N):
            factor = (row == 0) or (row == N - 1) or (col == 0) or (col == N - 1)
            if rexinos[row][col] == 1 and factor:
                rexinos[row][col] = 'C'
                cores -= 1

    # 먼저, 연결할 수 있는 방향이 한곳만 존재하는 대상을 우선적으로 연결한다.
    for row in range(N):
        for col in range(N):
            if rexinos[row][col] == '1':
                check(rexinos, row, col)

    # 이제 최초에, 연결 가능한 방향이 한곳이 아닌 대상에 대해 연결해보자.
    for row in range(N):
        for col in range(N):
            if rexinos[row][col] == '1':
                calc(rexinos, row, col)

    print('#{} {}'.format(tc, lines))



