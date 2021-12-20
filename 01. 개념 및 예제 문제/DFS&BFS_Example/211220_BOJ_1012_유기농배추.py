# SILVER2

def dfs(N, M, arr, point):
    global visited
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    stack.append(point)
    # stack에 넣을 때 visited 처리
    visited[point[0]][point[1]] = 1
    while stack:
        now = stack.pop()
        # 사방 탐색 실시
        for way in range(4):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]
            # indexError 고려
            if 0 <= nr < N and 0 <= nc < M:
                # 배추가 심어져 있다면 stack에 추가
                if arr[nr][nc] != 0 and visited[nr][nc] == 0:
                    stack.append([nr, nc])
                    visited[nr][nc] = 1
            else:
                continue
    return 1


T = int(input())
info = []
arrs = []
visited_arrs = []

for tc in range(T):
    M, N, K = map(int, input().split()) # 가로길이, 세로길이, 배추가 심어져 있는 곳의 개수
    arr = [[0]*M for _ in range(N)]
    visited = [[0]*M for _ in range(N)]

    for i in range(K):
        col, row = map(int, input().split())
        arr[row][col] = 1

    info.append([M, N, K])
    arrs.append(arr)
    visited_arrs.append(visited)

# 입력 받았으면, 실행하자.
for (index, arr) in enumerate(arrs):
    result = 0
    visited = visited_arrs[index]
    M, N, K = info[index]

    for row in range(N):
        for col in range(M):
            if arr[row][col] != 0 and visited[row][col] == 0:
                result += dfs(N, M, arr, [row, col])
    print(result)