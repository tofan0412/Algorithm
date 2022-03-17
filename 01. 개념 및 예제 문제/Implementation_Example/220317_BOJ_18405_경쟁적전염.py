from collections import deque

n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j))
s, x, y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(s, x, y):
    q = deque(virus)
    count = 0
    while q:
        if count == s:
            break
        for _ in range(len(q)):
            prev, r, c = q.popleft()

            for way in range(4):
                gr = r + dr[way]
                gc = c + dc[way]

                if 0 <= gr < n and 0 <= gc < n:
                    if graph[gr][gc] == 0:
                        graph[gr][gc] = prev
                        q.append((graph[gr][gc], gr, gc))
        count += 1
    return graph[x-1][y-1]


virus.sort()
print(bfs(s, x, y))

