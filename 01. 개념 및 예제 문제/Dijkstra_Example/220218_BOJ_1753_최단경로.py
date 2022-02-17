# GOLD5
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    u, v, w = map(int, input().split()) # u에서 v로 가는 가중치 w가 존재한다는 뜻이다.
    graph[u].append((v, w))


# 노드의 개수가 20,000개가 넘어가므로 힙을 이용해서 해야 한다.
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 기준 노드
        dist, now = heapq.heappop(q) # dist는 해당 노드에 대한 비용을, now는 노드 번호를 의미한다.
        # 만약 이미 처리했다면..
        if distance[now] < dist: # 노드를 방문한 경우, distance에 기록된 dist보다 값이 작아질 수가 없다.
            continue

        # 인접 노드를 조사해야 한다.
        for j in graph[now]: # j[0] : 인접 노드번호, j[1] : 해당 노드까지 가는데 필요한 비용
            cost = dist + j[1] # 현재 노드의 비용 + 간선값
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


dijkstra(start)


for i in range(1, n+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
