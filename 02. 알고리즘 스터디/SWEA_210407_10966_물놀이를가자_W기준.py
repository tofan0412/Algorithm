# L부터 찾지 말고 W부터 찾자..!
def BFS(queue, D):
    global result
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue:
        point = queue.pop(0)
        for i in range(4):
            row_move_to = point[0] + dr[i]
            col_move_to = point[1] + dc[i]

            check1 = 0 <= row_move_to and row_move_to < N
            check2 = 0 <= col_move_to and col_move_to < M
            if check1 and check2 and waterpark[row_move_to][col_move_to] != 'W':
                if D[point[0]][point[1]] + 1 < D[row_move_to][col_move_to] or D[row_move_to][col_move_to] == 0:
                    D[row_move_to][col_move_to] = D[point[0]][point[1]] + 1
                    queue.append((row_move_to, col_move_to))
            else:
                continue

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    waterpark = [list(input()) for _ in range(N)]
    D = [[0] * M for _ in range(N)]
    queue = []
    result = 0
    for row in range(N):
        for col in range(M):
            queue = []
            if waterpark[row][col] == 'W':
                queue.append((row, col))
                BFS(queue, D)
            else:
                continue

    for i in range(N):
        for j in range(M):
            result += D[i][j]
    print(f'#{tc} {result}')
