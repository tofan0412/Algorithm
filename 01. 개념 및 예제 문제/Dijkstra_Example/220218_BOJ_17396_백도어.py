# GOLD5
import sys
import heapq

input = sys.stdin.readline
INF = int(1e15)

n, m = map(int, input().split())
can_approach = list(map(int, input().split())) # 0이면 상대 시야에 안보이고, 1이면 보인다.
# 마지막 넥서스의 경우, 상대 시야가 보이지만 유일하게 갈 수 있는 곳이다.
graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m):
    u, v, w = map(int, input().split())
    # 한 지점에서 다른 지점으로 가는 최대 간선의 개수는 1개이다.
    # 양방향 연결이다.
    graph[u].append((v, w))
    graph[v].append((u, w))


def dijkstra(start):
    # 1. 기준 노드에 대한 처리
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for j in graph[now]: # j의 0번째는 인접 노드 번호, j[1]은 해당노드까지 가는데 필요한 시간이다.
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                # 상대방 시야를 확인해야 한다. 단 마지막은 도착할 수 있다.
                if j[0] != n-1 and can_approach[j[0]] == 0:
                    heapq.heappush(q, (cost, j[0]))
                elif j[0] == n-1:
                    heapq.heappush(q, (cost, j[0]))



dijkstra(0)
if distance[n-1] == INF:
    print(-1)
else:
    print(distance[n-1])

