dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def search():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i,j

def BFS(r, c):
    # 선형 큐를 이용해서 작성을 해보자.
    Q = [0] * 1000000
    front = -1
    rear = 0 # 약간 편법
    Q[rear] = (r, c)

    dist = [[-1] * (N) for _ in range(N)]
    dist[r][c] = 0

    # 선형큐에서의 공백검사
    while front != rear:
        front += 1
        curr_r, curr_c = Q[front]
        if maze[curr_r][curr_c] == '3':
            return dist[curr_r][curr_c] - 1
        # 사방검사
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            # 벽으로 둘러싸지 않았기 때문에 범위 검사를 해야 한다.
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            else:
                # 벽이 아니면서, 거리를 갱신하지 않았다면 좌표를 넣고 갱신한다.
                if maze[nr][nc] != '1' and dist[nr[nc]] == -1:
                    dist[nr][nc] == dist[curr_r][curr_c] + 1
                    rear += 1
                    Q[rear] = (nr, nc)
    # 도착하지 못했을 때의 결과값을 0으로 출력한다.
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 미로의 크기
    maze = [list(input()) for _ in range(N)]

    stR, stC = search()
    print(f'#{tc} {BFS(stR, stC)}')





