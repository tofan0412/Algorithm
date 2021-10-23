from collections import deque
'''
N x M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려 있는 부분끼리 상,하,좌,우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
생서되는 총 아이스크림 개수를 구해보자.
'''

# 스타트 지점은 (0,0)으로 한다.
# 상하좌우로 탐색해야 한다.
def BFS(icebox, start, visited):
    global result

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    # 큐에 삽입하고 방문처리를 한다.
    queue.append(start)
    visited[start[0]][start[1]] = True

    # 큐에 노드가 존재하는 동안 작업한다.
    while queue:
        # 큐에서 꺼낸다.
        point = queue.popleft()
        # 4방향 탐색 실시
        for way in range(4):
            row_to_move = point[0] + dr[way]
            col_to_move = point[1] + dc[way]

            # IndexError 검사
            if (row_to_move < 0 or row_to_move >= N) or (col_to_move < 0 or col_to_move >= M):
                continue
            else:
                # 0이고 아직 방문하지 않은 곳이라면
                if icebox[row_to_move][col_to_move] == 0 and visited[row_to_move][col_to_move] != True:
                    # 큐에 삽입하고 방문 처리를 한다.
                    queue.append([row_to_move, col_to_move])
                    visited[row_to_move][col_to_move] = True
    # 여기 왔다는 것은 큐가 비었다는 것을 의미한다.
    result += 1

N, M = map(int, input().split())
visited = list([0] * M for _ in range(N))
icebox = [list(map(int, input())) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(M):
        if icebox[i][j] == 0 and visited[i][j] != True:
            BFS(icebox, [i, j], visited)
        else:
            continue

print(result)