import sys
from collections import deque


def bfs(n, arr, point, l, r):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue.append(point)
    visited[point[0]][point[1]] = True
    nations = [(point[0]), point[1]]
    total = arr[point[0]][point[1]]

    while queue:
        nr, nc = queue.popleft()

        for way in range(4):
            gr = nr + dr[way]
            gc = nc + dc[way]

            if 0 <= gr < n and 0 <= gc < n:
                if l <= abs(arr[gr][gc] - arr[nr][nc]) <= r and not visited[gr][gc]:
                    queue.append((gr, gc))
                    nations.append([gr, gc])
                    visited[gr][gc] = True
                    total += arr[gr][gc]

    return nations, total


N, L, R = map(int, sys.stdin.readline().strip().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

result = 0
while True:
    unions = []
    populations = []

    check = set()

    # 핵심! Union을 먼저 구하고, 마지막에 평균값을 넣어야 함
    for row in range(N):
        for col in range(N):
            if (row, col) not in check:
                # 이 때 union에 있는 대상은 더이상 bfs 안해도 됨..
                v, num = bfs(N, arr, (row, col), L, R) # -1 아니면 리스트 반환

                if v not in unions and len(v) > 1:
                    unions.append(v)
                    populations.append(num)
    if len(unions) == 0:
        print(result)
        break
    else:
        # 이제 평균값으로 인구를 이동시키자.
        for i, union in enumerate(unions):
            for country in union:
                arr[country[0]][country[1]] = populations[i] // len(union)
    result += 1
