def BFS(queue):
    global result
    # 거리값을 갖는 리스트 초기화
    D = [[0] * M for _ in range(N)]
    while queue: # 큐에 값이 있을 때까지 반복한다.
        point = queue.pop(0) # 큐에서 시작점을 뺀다.
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4): # 사방 탐색 실시
            row_move_to = point[0] + dr[i]
            col_move_to = point[1] + dc[i]

            check1 = 0 <= row_move_to and row_move_to < N
            check2 = 0 <= col_move_to and col_move_to < M
            if check1 and check2 and D[row_move_to][col_move_to] == 0: # 만약 격자 내에 위치하는 곳이고, 방문하지 않은 곳이라면
                # 1. 기준점에서 여기까지의 거리 재기. 이 것이 결국 방문처리 하는 것이다.
                D[row_move_to][col_move_to] = D[point[0]][point[1]] + 1

                # 만약 방문한 곳이 W라면? 거리값을 반환하고 함수 종료.
                # D를 통해 최소한의 거리를 구할 수 있도록 해야 한다.
                if waterpark[row_move_to][col_move_to] == 'W':
                    result += D[row_move_to][col_move_to]
                    return
                queue.append((row_move_to, col_move_to))
    # 격자 내에 반드시 W가 존재한다는 가정이 들어가므로, 반드시 W까지의 거리값을 반환할 것이다.

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    waterpark = [list(input()) for _ in range(N)]
    queue = []
    result = 0
    # 한칸씩 검사한다.
    for row in range(N):
        for col in range(M):
            queue = []  # 큐의 초기화. 시작점 하나만을 담고 있어야 한다.
            if waterpark[row][col] == 'L':
                # queue에 시작점 정보를 넣어둔다.
                queue.append((row, col))
                BFS(queue)

    print(f'#{tc} {result}')


# L부터 찾지 말고 W부터 찾자..!

