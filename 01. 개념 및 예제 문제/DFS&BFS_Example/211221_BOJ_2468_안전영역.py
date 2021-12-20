def solution(arr, N, height, point):
    global visited
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    stack = []
    stack.append(point)
    visited[point[0]][point[1]] = 1

    while stack:
        now = stack.pop()
        # 사방 탐색 실시
        for way in range(4):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]
            # IndexError 고려
            if 0 <= nr < N and 0 <= nc < N:
                # height 고려
                if arr[nr][nc] > height and visited[nr][nc] == 0:
                    stack.append([nr, nc])
                    visited[nr][nc] = 1
    return 1


N = int(input())
arr = [[0]*N for _ in range(N)]
result = []

for row in range(N):
    arr[row] = list(map(int, input().split()))

# 1. 가장 낮은 높이 min_h와 가장 높은 높이 max_h를 센다.
min_h = 101 # 높이는 1 이상 100 이하의 정수
max_h = 0 # 높이는 1 이상 100 이하의 정수
for row in range(N):
    for col in range(N):
        if arr[row][col] < min_h:
            min_h = arr[row][col]
        if arr[row][col] > max_h:
            max_h = arr[row][col]

# 2. 가능한 높이의 range에서 안전 영역의 개수를 각각 count
for height in range(min_h, max_h):
    count = 0
    for row in range(N):
        for col in range(N):
            visited = [[0]*N for _ in range(N)]
            if visited[row][col] == 0:
                count += solution(arr, N, height, [row, col])
    result.append(count)

print(max(result))


