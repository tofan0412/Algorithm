# SILVER1
from collections import deque

def solution(arr, point):
    global distance
    global visited
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    queue.append(point)
    visited[point[0]][point[1]] = 1
    distance[point[0]][point[1]] = 1 # 출발지와 목적지 칸을 포함해야 하므로

    while queue:
        now = queue.popleft()

        # 사방 탐색 실시
        for way in range(4):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]

            # IndexError 고려
            if 0 <= nr < N and 0 <= nc < M:
                # visited 고려. 또한 arr[nr][nc]인 부분만, 지나갈 수 있다.
                if visited[nr][nc] == 0 and arr[nr][nc] == '1':
                    # queue에 삽입하자. 이후 방문 처리 한다.
                    queue.append([nr, nc])
                    visited[nr][nc] = 1
                    # 시작점으로부터 얼마나 떨어졌는지, 거리를 표시해 둔다.
                    # 이 때, 주의해야 할 사항은 최소 거리를 구하는 것이다.
                    if distance[nr][nc] > distance[now[0]][now[1]] + 1:
                        distance[nr][nc] = distance[now[0]][now[1]] + 1
    print(distance[len(arr)-1][len(arr[0])-1])


N, M = map(int, input().split()) # N은 row, M은 column을 나타낸다.
arr = [[]*M for _ in range(N)]
for row in range(N):
    arr[row] = list(input())

distance = [[101]*M for _ in range(N)] # 거리 표시
visited = [[0]*M for _ in range(N)] # 방문 여부 표시

solution(arr, [0, 0])