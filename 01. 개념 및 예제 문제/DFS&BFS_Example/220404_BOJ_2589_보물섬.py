# GOLD5
import sys
from collections import deque
from pprint import pprint


def bfs(arr, point, h, w):
    queue = deque()
    visited = [[False] * width for _ in range(height)]
    distance = [[0] * width for _ in range(height)]

    queue.append(point)
    visited[point[0]][point[1]] = True

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    result = 0 # 현재 (row, col)에서 출발했을 때 나올 수 있는 가장 큰 값

    while queue:
        nr, nc = queue.popleft()

        # 사방 탐색 실시
        for way in range(4):
            gr = nr + dr[way]
            gc = nc + dc[way]

            if 0 <= gr < h and 0 <= gc < w:
                if arr[gr][gc] == 'L' and not visited[gr][gc]:
                    queue.append((gr, gc))
                    visited[gr][gc] = True
                    distance[gr][gc] = distance[nr][nc] + 1
                    # 시간 등록
                    if distance[gr][gc] > result:
                        result = distance[gr][gc]

    # pprint(distance)
    return result


height, width = map(int, sys.stdin.readline().split())

world = []
for row in range(height):
    world.append(list(sys.stdin.readline().strip()))

answer = 0
for row in range(height):
    for col in range(width):
        if world[row][col] == "L":
            mv = bfs(world, (row, col), height, width)
            if mv > answer:
                answer = mv

print(answer)


