# GOLD4
import heapq

# 방의 크기가 최대 100 by 100이다. 이 경우 최대 방의 개수는 100000이다. -> heapq 쓰자.
col, row = map(int, input().split()) # m은 가로 크기, n은 세로크기
INF = int(1e9)
maze = [list(map(int,input())) for _ in range(row)]
counts = [[INF] * col for _ in range(row)] # distance[i][j]는 기준점으로부터 i,j로 이동하기 위해 벽을 부순 개수를 뜻한다.

# 출발점은 (0, 0)이고 도착점은 (row-1, col-1)이다.
# 상하좌우로만 이동 가능하다.
# 따라서 graph를 할 필요가 없다. 기준 노드 주변 상하좌우 4칸만 인접 노드이기 때문에..
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 기준은 해당 노드로 이동하기 까지 몇 개의 벽을 부쉈느냐가 되어야 한다.
def dijkstra(start):
    counts[start[0]][start[1]] = 0
    q = []

    heapq.heappush(q, (0, start)) # 튜플의 첫번째는 해당노드까지 오기 위해 부순 벽의 개수이고, start는 좌표 i,j를 뜻한다.
    while q:
        cnt, now = heapq.heappop(q)

        if cnt < counts[now[0]][now[1]]:
            continue

        # 인접 노드 조사한다. 해당 노드로 가기까지 부숴야 하는 벽의 개수 기준으로 갱신...
        for i in range(4):
            move_to_row = now[0] + dr[i]
            move_to_col = now[1] + dc[i]
            # 1. 해당 벽이 미로 안에 있는가?
            if 0 <= move_to_row < row and 0 <= move_to_col < col:
                # 2. 미로 안에 있다면 벽인지 벽이 아닌지 판단한다.
                # 만약 벽이라면
                cost = 0
                if maze[move_to_row][move_to_col] == 1:
                    cost = counts[now[0]][now[1]] + 1
                else:
                    cost = counts[now[0]][now[1]]
                if cost < counts[move_to_row][move_to_col]:
                    counts[move_to_row][move_to_col] = cost
                    heapq.heappush(q, (cost, (move_to_row, move_to_col)))


dijkstra((0, 0))
print(counts[row-1][col-1])

