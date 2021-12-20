# GOLD5
# 색약이 아닌 경우
def solution(arr, N, point):
    global visited
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    stack.append(point)
    visited[point[0]][point[1]] = 1

    # 색약이 아닌 경우
    while stack:
        now = stack.pop()
        for way in range(4):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]

            if 0 <= nr < N and 0 <= nc < N:
                # 같은 영역인지 확인해야 한다.
                if arr[now[0]][now[1]] == arr[nr][nc] and visited[nr][nc] == 0:
                    stack.append([nr, nc])
                    visited[nr][nc] = 1
    return 1


# 색약인 경우
def solution2(arr, N, point):
    global visited2
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    stack.append(point)
    visited2[point[0]][point[1]] = 1

    # 색약이 아닌 경우
    while stack:
        now = stack.pop()
        for way in range(4):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]

            if 0 <= nr < N and 0 <= nc < N:
                # 같은 영역인지 확인해야 한다.
                if arr[now[0]][now[1]] == 'R' or arr[now[0]][now[1]] == 'G':
                    if (arr[nr][nc] == 'G' or arr[nr][nc] == 'R') and visited2[nr][nc] == 0:
                        stack.append([nr, nc])
                        visited2[nr][nc] = 1
                # 파란색인 경우
                else:
                    if arr[now[0]][now[1]] == arr[nr][nc] and visited2[nr][nc] == 0:
                        stack.append([nr, nc])
                        visited2[nr][nc] = 1
    return 1

N = int(input())
arr = [[0]*N for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited2 = [[0]*N for _ in range(N)]
result = 0
result2 = 0

for i in range(N):
    arr[i] = list(input())

for row in range(N):
    for col in range(N):
        if visited[row][col] == 0:
            # 먼저 색약이 아닌 경우 영역 세기
            result += solution(arr, N, [row, col])

for row in range(N):
    for col in range(N):
        if visited2[row][col] == 0:
            # 먼저 색약이 아닌 경우 영역 세기
            result2 += solution2(arr, N, [row, col])

print(result, result2)
