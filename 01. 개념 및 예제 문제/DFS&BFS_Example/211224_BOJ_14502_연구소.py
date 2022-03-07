# GOLD5
# 바이러스의 확산을 막기 위해 연구소에 벽을 세우려고 한다.

# 연구소는 크기가 NxM인 직사각형으로 나타낼 수 있으며 직사각형은 1x1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈칸, 벽으로 이루어져 있으며 벽은 칸 하나를 가득 차지한다.

# 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 곳이다.
# 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈 캄으로 모두 퍼져나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 총 3개이며, 반드시 3개를 모두 사용해야 한다.
from collections import deque

def bfs(maps):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    result = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작점을 등록한다. -> 시작점을 매번 변경해야 하는거 아닌가..?
    queue.append([0, 0])
    visited[0][0] = True

    while queue:
        now = queue.popleft()
        # 사방 탐색 실시한다.
        for way in range(4):
            row_to = now[0] + dr[way]
            col_to = now[1] + dc[way]

            # 맵 영역 안인지 검사한다.
            if 0 <= row_to < n and 0 <= col_to < m:
                # 방문하지 않았으면서, 안전영역인지 검사한다.
                if maps[row_to][col_to] == 0 and not visited[row_to][col_to]:
                    queue.append([row_to, col_to])
                    visited[row_to][col_to] = True
                    result += 1

    return result


def solution(n, m, cnt, maps): # cnt는 현재까지 세운 벽의 개수를, maps는 연구소 지도를 뜻한다.
    global max_result
    if cnt == 3:
        # 모든 벽을 세운 경우에는 안전 영역의 개수를 세봐야 한다.
        safe_cnt = bfs(maps)
        if max_result < safe_cnt:
            max_result = safe_cnt
        return

    tmp = list(maps) # Deep Copy
    # 벽을 아직 3개 세우지 않은 경우..
    for row in range(n):
        for col in range(m):
            # 해당 포인트에 벽을 세운다.
            tmp[row][col] =




n, m = map(int, input().split()) # n은 3보다 크고, M은 8보다 작다.
lab = [list(map(int, input().split())) for _ in range(n)]

max_result = -12345

# 3개의 벽을 세울 수 있는 모든 경우의 수를 파악해보자.
# 3개의 벽을 모두 세운 후에는, BFS를 통해 안전 영역의 크기를 센다.