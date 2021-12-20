# SILVER2

def dfs(node):
    global visited
    stack = []
    stack.append(node)
    visited[node] = 1
    while stack:
        now = stack.pop()
        for adj_node in adj[now]:
            if visited[adj_node] == 0:
                stack.append(adj_node)
                visited[adj_node] = 1
    return 1

N, M = map(int, input().split()) # 정점의 개수 M과 간선의 개수 M
adj = [[] for _ in range(N+1)] # 0번 노드는 없으므로
visited = [0] * (N + 1)
result = 0

for i in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 1번부터 출발하자.
for node in range(1, N+1):
    # 방문한 적이 없다면
    if visited[node] == 0:
        result += dfs(node)

print(result)