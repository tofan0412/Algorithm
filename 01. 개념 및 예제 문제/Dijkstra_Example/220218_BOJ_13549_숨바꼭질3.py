import heapq
# GOLD5
INF = int(1e9)
n, k = map(int, input().split())
# 1. 다익스트라로 풀려고 한다면?
# 이 경우 한 노드에 대한 인접 정보를 제공하는 graph는 필요없다. -> n과 2n에 대한 간선, n - n+1, n - n-1에 대한 간선 정보로 고정
# 도시(좌표)의 개수가 최대 10만개이므로, O(N^2) 풀이가 아닌 O(ElogV) 풀이를 통해 접근하자.
# 이 경우 힙을 사용하게 되므로 visited 또한 필요없다.
distance = [INF] * 100001


def dijkstra(start):
    # 1. 기준 노드에 대해 처리한다.
    q = []
    heapq.heappush(q, (0, start)) # 튜플의 0번째는 해당 노드에 방문하기 위해 필요한 비용, 1번째는 노드번호(=좌표)이다.
    distance[start] = 0

    while q:
        # 인접 노드 조사. 이때 인접노드는 3가지이다. n-1, n+1, 2n
        dist, now = heapq.heappop(q)

        # 만약 이미 방문한 곳이라면? 다음으로..
        if distance[now] < dist:
            continue
        adj = [now-1, now+1, now*2]
        cost_arr = [1, 1, 0]
        for i in range(3):
            if 0 <= adj[i] < 100001:
                cost = distance[now] + cost_arr[i]
                if cost < distance[adj[i]]:
                    distance[adj[i]] = cost
                    heapq.heappush(q, (distance[adj[i]], adj[i]))


dijkstra(n)

print(distance[k])



