T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    maze = [list(input()) for i in range(N)]
    dist_map = [[0]*N for i in range(N)]
    s_point, e_point = [], [] # 출발지점, 도착지점

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
    dist_map[e_point[0]][e_point[1]] = 200

    # 상,하,좌,우를 확인한다.
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = []
    queue.append(s_point)

    while queue:
        row, col = queue.pop(0) # 상하좌우를 계산할 기준 좌표를 의미한다.
        # 이미 처리했다는 의미를 위해 마킹한다.
        maze[row][col] = 200

        # 좌표검사
        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == '0':
                    queue.append((nr, nc))
                    dist_map[nr][nc] = dist_map[row][col] + 1
                if maze[nr][nc] == '3':
                    if dist_map[nr][nc] >= dist_map[row][col] + 1:
                        dist_map[nr][nc] = dist_map[row][col] + 1

    if dist_map[e_point[0]][e_point[1]] == 200:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {dist_map[e_point[0]][e_point[1]]}')