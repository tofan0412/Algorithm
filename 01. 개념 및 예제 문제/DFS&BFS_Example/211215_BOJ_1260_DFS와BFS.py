from collections import deque

# 너비 우선 탐색
def bfs(N, adj, V):
    result = []
    visited = [0] * (N+1)
    queue = deque()
    queue.append(V)

    while queue:
        # 꺼낸 후, 방문 처리한다.
        now = queue.popleft()
        visited[now] = 1
        result.append(now)

        # 인접 리스트(adj) 통해 인접한 정점을 확인하고, 아직 방문하지 않았다면 큐에 쌓는다.
        # 단, 인접한 정점 중에서 낮은 번호부터 먼저 방문한다.
        for i in adj[now].sort():
            if visited[i] != 1:
                queue.append(i)
                visited[i] = 1
    return result


def dfs(N, adj, V): # V는 시작 정점
    visited = [0] * (N+1)
    result = ''
    # 깊이 우선 탐색
    stack = []
    stack.append(V)
    # 스택에 데이터가 있는 한 반복한다.
    while stack:
        # 1. stack에서 꺼낸다. 이후 방문 처리한다.
        now = stack.pop()
        visited[now] = 1
        # result에 넣는다.
        result += str(now) + ' '
        # 2. 꺼낸 기준 node를 기준으로 주변을 탐색한다.
        for i in adj[now]:
            # 방문이 아직 되어 있지 않다면 stack에 쌓는다.
            if visited[i] != 1:
                stack.append(i)
                break
    return result


N, M, V = map(int, input().split())  # 정점(node)의 개수 N, 간선(edge)의 개수 M, 시작점 V
adj = [[] for i in range(N+1)] # N이 1에서부터 시작하므로

for i in range(M):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1) # 양방향이므로 모두 넣어줘야 한다.

# 먼저 DFS를 수행한다.
print(dfs(N, adj, V))
# Visited 초기화
visited = [0] * (N+1)
# BFS를 수행한다.
print(bfs(N, adj, V))


