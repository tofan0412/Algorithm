def dfs(arr, visited, point):
    count = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 상, 하, 좌, 우 순서로 사방 탐색해야 한다.
    stack = []
    stack.append(point)
    while stack:
        now = stack.pop()
        # 방문 처리 한다.
        if visited[now[0]][now[1]] == 0:
            visited[now[0]][now[1]] = 1
            # 집 갯수를 카운트한다.
            count += 1
        else:
            continue
        # 사방 탐색 실시
        for i in range(4):
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            # IndexError 고려
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] != '0' and visited[nr][nc] == 0:
                        stack.append([nr, nc])
    # while문이 끝나면 하나의 집을 찾았다는 뜻이다.
    return count


N = int(input())
arr = [[]*N for _ in range(N)]

for i in range(N):
    row = list(input())
    arr[i] = row

visited = [[0]*N for _ in range(N)]
danji = 0
building_number = []
# 1. 2차원 배열에 대해 완탐 실시
for i in range(N):
    for j in range(N):
        if arr[i][j] != '0':
            # 2. 0이 아닌 (i,j) 지점을 기준으로 DFS 통해 사방 탐색 시작.
            # 단, 이미 방문했는지 여부를 확인해야 한다.
            if visited[i][j] != 1:
                # dfs를 수행한 횟수는 단지 수가 되고, dfs의 return 값은 하나의 단지 내 건물 수가 된다.
                building_number.append(dfs(arr, visited, [i, j]))
                danji += 1

print(danji)
# building_number sort
building_number.sort()
for count in building_number:
    print(count)