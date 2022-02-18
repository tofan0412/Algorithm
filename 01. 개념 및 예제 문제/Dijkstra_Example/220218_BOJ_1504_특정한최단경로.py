# GOLD4
# 방향성이 없는 그래프가 주어진다.
# 세준이는 1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.
# 또한 세준이는 2가지 조건을 만족하면서 이동하는 특정한 최단 경로를 구하고 싶은데,
# 그것은 바로 임의로 주어진 두 정점은 반드시 통과해야 한다는 것이다.

# 세준이는 한번 이동했던 정점은 물론, 한번 이동했던 간선도 다시 이동할 수 있다.
# 하지만 반드시 최단 경로로 이동해야 한다는 사실에 주의하라.
import sys
import heapq


input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # n은 노드의 개수, m은 간선의 개수를 의미한다.
graph = [[] for _ in range(n+1)] # 노드 번호가 없으므로 n+1로 하지 말자.
distance = [INF] * (n+1)
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

v1, v2 = map(int, input().split()) # 두 정점 v1, v2는 반드시 통과해야 한다.


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 한번 방문했던 정점은 물론, 간선도 재방문할 수 있다..
        if distance[now] < dist: # 이게 있으면 재방문을 허용하지 않는다..
            continue

        # 인접 노드를 탐색한다.
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


result, result2 = 0, 0
arr = [1, v1, v2, n]
arr2 = [1, v2, v1, n]

for i in range(3):
    # 1번 노드에서 v1으로 가는 최단 경로를 구하고, v1에서 v2로 가는 최단 경로를 구한다. (이 과정에서 v1 -> v2로 다이렉트로갈 수도 있고, 없을 수도 있다.)
    # 이후 v2를 기준으로 n까지 가는 최단 경로를 구하며, 이 과정에서 구한 모든 최단 경로를 합하여 출력한다.

    distance = [INF] * (n + 1)
    dijkstra(arr[i])

    if distance[arr[i+1]] != INF:
        result += distance[arr[i+1]]
    else:
        result = INF
        break

for i in range(3):
    distance = [INF] * (n + 1)
    dijkstra(arr2[i])

    if distance[arr2[i + 1]] != INF:
        result2 += distance[arr2[i + 1]]
    # 도중 하나라도 -1이 나온다면? 아예 갈 수 없는 경우이다.
    else:
        result2 = INF
        break

# 만약 둘 다 -1인 경우에는 두 정점을 지나고 n까지 갈 수 없으므로 -1을 출력한다.
if result == result2 == INF:
    print(-1)
# 둘 중 하나가 -1이 아니라면
else:
    print(min(result, result2))


# 애초에 다익스트라 알고리즘이 Greedy 알고리즘이기 때문에,
# 두 정점을 지나는 경우도 Greedy하게 생각했다.
# 즉 출발점 -> v1 -> v2 -> n의 과정에서 필요한 최소 경로를 모두 더하는 것과
# 출발점 -> v2 -> v1 -> n의 과정에서 필요한 최소 경로를 모두 더하여 두 가지 중 작은 경우를 출력하는 것이다.
# 이 때 두 경우 모두 INF가 나오는 경우에는 결코 두 정점을 지나면서 목적지에 도착할 수 없는 경우이므로 -1을 출력하고
# 둘 중 하나라도 INF가 아닌 경우에는 해당 값을 출력하도록 하였다.


