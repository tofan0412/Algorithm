# GODL5
import sys
from pprint import pprint
from collections import deque


def bfs(arr, point, m, n, h): # point는 layer, row, col 순이다.
    # visited 또한 3차원 배열로 설정해야 한다.
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]

    queue = deque()

    queue.append(point)
    queue.append((-99, -99, -99)) # 일수를 카운트하기 위한 대상이다.
    visited[point[0]][point[1]][point[2]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    dh = [-1, 1]

    # Queue에다가 하루가 지났음을 알리는 대상을 넣자.
    # 토마토가 모두 익었다는 건, queue에 더이상 대상이 없다는 뜻이다.
    day = 0

    while queue:
        layer, nr, nc = queue.popleft()

        if layer == nr == nc == -99:
            day += 1
            continue

        # 1. 한 layer에 대해 사방탐색
        for way in range(4):
            gr = nr + dr[way]
            gc = nc + dc[way]

            if 0 <= gr < n and 0 <= gc < m:
                if arr[gr][gc] == 0 and not visited[layer][gr][gc]:
                    queue.append((layer, gr, gc))
                    visited[layer][gr][gc] = True

        # 2. 인접한 양 layer에 대해 탐색.
        for way in range(2):
            gh = layer + dh[way]

            # IndexError 검사
            if 0 <= gh < h:
                if arr[gh][nr][nc] == 0 and not visited[gh][nr][nc]:
                    queue.append((gh, nr, nc))
                    visited[gh][nr][nc] = True
    # Queue에 대한 사방 탐색이 끝난 이후, 검사해야 한다.
    # 1. 모든 토마토가 익어있는가?
    # 2. 토마토가 모두 익지 못하는 상황인가?
    is_ripen = False


def check_ripend()



M, N, H = map(int, sys.stdin.readline().rstrip().split())
# m은 width, n은 row, h는 height를 의미한다.
arr = []

for _ in range(H):
    board = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().rstrip().split()))
        board.append(row)
    arr.append(board)

# 담기는 순서는 가장 밑의 층부터 ~ 가장 위의 층 순서이다.
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 없는 칸..
