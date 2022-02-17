# SILVER2
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)] # 노드의 인접정보를 저장한다.
visited = [False] * (n+1) # 각 노드의 방문 정보
distance = [int(1e9)] * (n+1) # 기준 노드에서 각 노드까지 이동하는데 필요한 최소 경로

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


def find_smallest_node():
    min_value = int(1e9)
    index = 0
    for node in range(1, n+1):
        if not visited[node] and distance[node] < min_value:
            min_value = distance[node]
            index = node

    return index


def dijkstra(start):
    # 1. 기준 노드 주변의 인접 노드를 조사하고, distance를 갱신한다.
    visited[start] = True
    distance[start] = 0

    for other_node in graph[start]:
        distance[other_node] = distance[start] + 1

    # 노드는 n개 있으면, n번 선택해야 한다.
    for i in range(1, n+1):
        now = find_smallest_node()
        visited[now] = True
        # now 기준으로 주변 인접 노드를 찾는다.
        for j in graph[now]:
            cost = distance[now] + 1
            if cost < distance[j]:
                distance[j] = cost


dijkstra(x)

result = []
for i, dist in enumerate(distance):
    if dist == k:
        result.append(i)

if len(result) > 0:
    for i in result:
        print(i)
else:
    print(-1)




