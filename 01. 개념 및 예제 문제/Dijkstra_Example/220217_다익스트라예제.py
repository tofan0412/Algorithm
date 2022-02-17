import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정이다.

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
# 주의) 1번 노드 ~ n번 노드에 맞추기 위해 n+1까지 리스트의 크기를 설정하였다.
graph = [[] for _ in range(n + 1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n + 1)
distance = [INF] * (n + 1) # start 노드를 기준으로, 각 노드에 이동하기 위해 필요한 비용을 기록하는 리스트이다.

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())  # a번 노드에서 b번 노드로 가는 비용이 c라는 뜻이다.
    graph[a].append([b, c])


# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0  # 가장 최단 거리가 짧은 노드 (인덱스)
    for i in range(1, n + 1): # 1번 노드에서부터 n번 노드 중에서 비용이 가장 작은 노드를 선택한다.
        if distance[i] < min_value and not visited[i]: # 방문할 수 없는 노드에 대해서, 거리값은 INF이다.
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]: # 시작 노드에 인접한 모든 노드에 대해 조사한다.
        distance[j[0]] = j[1] # 현재 노드를 기준으로, 인접한 노드의 거리값을 계산한다.

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복한다.
    # 마지막 노드에 대해선, 마지막 노드를 제외한 나머지 노드를 모두 방문했으므로 거리값을 갱신안해도 된다. (이미 fixed)
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost


# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한 (INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
