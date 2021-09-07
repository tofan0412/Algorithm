def dfs(stack):
    while stack:
        point = stack.pop()
        # 방문 처리
        visited[point] = 1
        print(point, end=' ')
        for i in adj[point]:
            # 방문하지 않았다면
            if visited[i] == 0:
                stack.append(i)


info = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
info = list(map(int, info.split()))
N = 7 # 정점의 개수
adj = [[]*i for i in range(N+1)]
visited = [0]*(N+1)
s = []

# 인접 정보 입력하기
for i in range(0, len(info), 2):
    adj[info[i]].append(info[i+1])
    adj[info[i+1]].append(info[i])

s.append(1)
dfs(s)

