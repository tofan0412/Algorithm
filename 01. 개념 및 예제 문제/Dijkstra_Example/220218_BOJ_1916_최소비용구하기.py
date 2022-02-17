# GOLD5
import sys
input = sys.stdin.readline
INF = int(1e15)

n = int(input()) # 도시의 개수가 1000개이다. -> O(N^2)으로 풀어보자.
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split()) # u는 출발 도시, v는 도착 도시, w는 버스 비용이다.
    graph[u].append([v, w]) # 같은 버스 노선에 대해, 비용만 다른 경우가 있을 수 있다.

start, end = map(int, input().split()) # 출발 도시와 도착 도시


def find_smallest_node():
    min_value = INF
    index = 0
    for v in range(n+1):
        if not visited[v] and distance[v] < min_value:
            min_value = distance[v]
            index = v
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True

    for i in graph[start]:
        # 중복 노선이 있을 수 있기 때문에...
        if i[1] < distance[i[0]]:
            distance[i[0]] = i[1]

    for i in range(n-1): # 마지막 노드는 방문 안해도 된다.
        # 거리를 조사한 인접노드 중에서 방문노드를 찾는다.
        now = find_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
print(distance[end])
