T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    maze = [list(input()) for i in range(N)]
    dist_map = [[0]*N for i in range(N)]
    s_point = 0 # 출발지점
    e_point = 0 # 도착지점

    # 출발지와 도착지를 찾는다.
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                s_point = (row, col)
            if maze[row][col] == '3':
                e_point = (row, col)
    # dist_map의 시작부분은 -1로 하고
    # dist_map의 도착부분은 99로 한다.
    dist_map[s_point[0]][s_point[1]] = -1
    dist_map[e_point[0]][e_point[1]] = 99

    # 상,하,좌,우를 확인한다.
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = []
    queue.append(s_point)
    while queue:
        tmp = queue.pop(0) # 상하좌우를 계산할 기준 좌표를 의미한다.
        row = tmp[0]
        col = tmp[1]
        # 이미 처리했다는 의미를 위해 마킹한다.
        maze[row][col] = 99

        up = row + dr[0]
        down = row + dr[1]
        left = col + dc[2]
        right = col + dc[3]

        # 좌표검사
        if 0 <= up and up < N:
            # 통로인 경우에는 거리를 dist_map에 표시한다.
            if maze[up][col] == '0':
                queue.append((up, col))
                dist_map[up][col] = dist_map[row][col] + 1
            # 도착점인 경우, 이미 거리가 마킹되어있을 o수 있다.
            # 따라서 마킹된 거리값보다 작은 경우에만 새롭게 마킹한다.
            if maze[up][col] == '3':
                if dist_map[up][col] >= dist_map[row][col] + 1:
                    dist_map[up][col] = dist_map[row][col] + 1

        if 0 <= down and down < N:
            if maze[down][col] == '0':
                queue.append((down, col))
                dist_map[up][col] = dist_map[row][col] + 1
            if maze[up][col] == '3':
                if dist_map[down][col] >= dist_map[row][col] + 1:
                    dist_map[down][col] = dist_map[row][col] + 1

        if 0 <= left and left < N:
            if maze[row][left] == '0':
                queue.append((row, left))
                dist_map[row][left] = dist_map[row][col] + 1
            if maze[row][left] == '3':
                if dist_map[row][left] >= dist_map[row][col] + 1:
                    dist_map[row][left] = dist_map[row][col] + 1

        if 0 <= right and right < N:
            if maze[row][right] == '0':
                queue.append((row, right))
                dist_map[row][right] = dist_map[row][col] + 1
            if maze[row][right] == '3':
                if dist_map[row][right] >= dist_map[row][col] + 1:
                    dist_map[row][right] = dist_map[row][col] + 1
    if dist_map[e_point[0]][e_point[1]] == 99:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {dist_map[e_point[0]][e_point[1]]}')