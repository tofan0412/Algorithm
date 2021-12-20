# SILVER3

def dfs(N, visited, adj, V):
    result = 0
    stack = []
    stack.append(V)
    visited[V] = 1
    while stack:
        now = stack.pop()
        # 방문했으므로 카운트
        result += 1
        # 인접 리스트를 통해 주변 노드를 검사한다.
        for i in adj[now]:
            # 아직 방문하지 않았다면 스택에 추가한다.
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1 # 반드시 Stack에 넣으면서 방문처리를 해야, Node가 중복해서 Stack에 쌓이지 않는다.
    return result


N = int(input())
M = int(input())
adj = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)
    adj[node2].append(node1)

# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
print(dfs(N, visited, adj, 1) - 1) # 1번 컴퓨터는 제외한다.