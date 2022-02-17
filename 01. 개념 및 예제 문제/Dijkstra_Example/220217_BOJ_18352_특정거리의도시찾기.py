import heapq
import sys
# SILVER2
# n은 노드의 개수, m은 간선의 개수, k는 기준, start는 시작도시
input = sys.stdin.readline
INF = int(1e9)

n, m, k, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    city1, city2 = map(int, input().split())
    graph[city1].append(city2)


# def get_smallest_node():
#     min_value = INF
#     index = 0
#     for i in range(n+1):
#         if not visited[i] and distance[i] < min_value:
#             min_value = distance[i]
#             index = i
#
#     return index

# O(V^2)의 시간 복잡도
# def dijkstra(start):
#     # 1. 기준 노드 방문 처리 및 distance 설정
#     distance[start] = 0
#     visited[start] = True
#
#     # 2. 기준 노드 주변 인접 노드에 대한 거리값 계산
#     for v in graph[start]:
#         distance[v] = 1 # 모든 도로의 거리는 1이며, 기준 노드의 비용은 0이기 때문에 0 + 1이다.
#
#     # 3. 거리값 계산했으면 인접한 노드 중에서 방문할 노드를 찾아야 한다.
#     for i in range(n+1):
#         now = get_smallest_node()
#         # 방문할 노드 찾았으면 방문처리
#         visited[now] = True
#
#         # 방문한 노드에 대해 주변 노드 조사하고 다시 거리값 계산
#         for v in graph[now]:
#             cost = distance[now] + 1 # start 노드 기준으로 얼마나 비용이 발생하는지 계산해야 한다.
#
#             # 코스트 갱신해야 한다.
#             if cost < distance[v]:
#                 distance[v] = cost


# O(ElogV)의 시간복잡도를 갖는 개선된 다익스트라 알고리즘
def dijkstra2(start):
    q = []
    heapq.heappush(q, (0, start)) # 튜플의 첫번째 요소는 해당 노드로 이동하기까지 필요한 비용, 2번째 요소는 노드번호
    distance[start] = 0

    # 1. 인접 노드를 조사하여, 인접노드에 대한 distance를 수정한다.
    # 2. 인접 노드 중 비용이 최소화되는 노드를 선택한다.
    # 3. 해당 노드의 인접 노드에 대해 distance를 갱신한다.
    # 4. 가장 짧은 노드를 선택하여 heapq.heappush

    while q:
        dist, now = heapq.heappop(q) # 이 때 now는 (해당 노드 비용, 인덱스)이다.

        # 만약 이미 처리한 적이 있다면 넘어간다.
        if distance[now] < dist:
            continue
        # 2. 인접 노드에 대한 distance를 수정한다.
        for j in graph[now]:
            cost = distance[now] + 1 # 도로의 가중치는 무조건 1이다.
            if cost < distance[j]:
                distance[j] = cost
                heapq.heappush(q, (distance[j], j))


dijkstra2(start)

result = []
for i, dis in enumerate(distance):
    if dis == k:
        result.append(i)

if len(result) > 0:
    for s in result:
        print(str(s))
else:
    print(-1)

