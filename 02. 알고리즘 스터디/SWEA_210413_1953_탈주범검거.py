def bfs(q):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while q:
        point = q.pop(0)  # (r, c)로 구성된다.
        vMap[point[0]][point[1]] = 1
        for way in range(4):
            move_to_row = point[0] + dr[way]
            move_to_col = point[1] + dc[way]
            # IndexError 여부
            check1 = 0 <= move_to_row & move_to_row < N
            check2 = 0 <= move_to_col & move_to_col < M

            # 만약 좌표내 존재하는 부분이고
            if check1 and check2:
                check4 = not vMap[move_to_row][move_to_col] # 방문 여부
                # 위 좌표 탐사
                if way == 0:
                    if arr[point[0]][point[1]] in [1, 2, 4, 7] \
                            and arr[move_to_row][move_to_col] in [1, 2, 5, 6] and check4:
                        dMap[move_to_row][move_to_col] = dMap[point[0]][point[1]] + 1
                        q.append((move_to_row, move_to_col))
                # 아래 방향 탐사
                elif way == 1:
                    if arr[point[0]][point[1]] in [1, 2, 5, 6] \
                            and arr[move_to_row][move_to_col] in [1, 2, 4, 7] and check4:
                        dMap[move_to_row][move_to_col] = dMap[point[0]][point[1]] + 1
                        q.append((move_to_row, move_to_col))
                # 왼쪽 방향 탐사
                elif way == 2:
                    if arr[point[0]][point[1]] in [1, 3, 6, 7] \
                            and arr[move_to_row][move_to_col] in [1, 3, 4, 5] and check4:
                        dMap[move_to_row][move_to_col] = dMap[point[0]][point[1]] + 1
                        q.append((move_to_row, move_to_col))
                # 오른쪽 방향 탐사
                elif way == 3:
                    if arr[point[0]][point[1]] in [1, 3, 4, 5]  \
                            and arr[move_to_row][move_to_col] in [1, 3, 6, 7] and check4:
                        dMap[move_to_row][move_to_col] = dMap[point[0]][point[1]] + 1
                        q.append((move_to_row, move_to_col))


def count_p(L): # 주어진 시간에 대해, 해당 시간 이내에 이동할 수 있는 모든 좌표를 구한다.
    cnt = 0
    for row in range(N):
        for col in range(M):
            if 0 < dMap[row][col] & dMap[row][col] <= L:
                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    # N,M은 지하 터널의 세로, 가로 크기 / R,C는 뚜껑위치, L은 소요된 시간
    N, M, R, C, L = list(map(int, input().split()))
    start = (R, C) # 출발점
    arr = [list(map(int, input().split())) for _ in range(N)]
    dMap = [[0]*M for _ in range(N)] # N시간 후에 갈 수 있는 지점들을 나타낸다.
    vMap = [[0]*M for _ in range(N)] # 이미 방문했는지를 나타낸다.

    # 주의 : 탈출 후, 1시간에 터널입구에 들어갔다
    q = []
    q.append(start)
    dMap[start[0]][start[1]] = 1  # 탈출 1시간 후에 맨홀뚜겅을 들어갔으므로
    bfs(q)
    # pprint.pprint(dMap)
    result = count_p(L)

    print(f'#{tc} {result}')