import sys
import heapq

input = sys.stdin.readline
# GOLD5
# 현서는 찬홍이에게 택배를 배달해줘야 한다.
# 평화롭게 가려면, 가는 길에 만나는 모든 소에게 여물을 줘야 한다.
# 물론 현서는 구두쇠라, 최소한의 소들을 만나며 지나가고 싶다.
# 현서는 헛간 1에 있고, 찬홍이는 헛간 N에 있다.
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)


def is_duplicated(u, v, w):
    min_value = INF

    for i in graph[u]:
        if i[0] == v and i[1] < min_value:
            min_value = i[1]

    if min_value > w:
        return True
    else:
        return False


# 헛간의 최대 개수가 50000개이므로 heap을 이용한다.
for _ in range(m):
    u, v, w = map(int, input().split())

    can_insert = is_duplicated(u, v, w)
    if can_insert:
        # 양방향이므로 둘 다 넣어줘야 한다.
        graph[u].append((v, w))
        graph[v].append((u, w))
    else:
        continue


def dijkstra(start):
    # 1. 기준 노드에 대한 설정
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문한 곳이면 pass
        if distance[now] < dist:
            continue

        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (distance[j[0]], j[0]))


dijkstra(1)
print(distance[n])


