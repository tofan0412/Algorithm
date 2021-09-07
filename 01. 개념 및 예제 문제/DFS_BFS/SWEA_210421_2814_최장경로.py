def dfs(s, cnt):
    a = 0
    global max_length
    # 여기로 온 건, 스택에 더이상 없다는 뜻이다.
    if cnt > max_length:
        max_length = cnt

    while s:
        point = s.pop()
        for points in adj[point]:
            # 아직 해당 포인트를 방문하지 않았다면
            if visited[points] == 0:
                visited[point] = 1
                s.append(points)
                dfs(s, cnt+1)
                # 이 한 줄만 추가됐다..
                # 최대경로 탐색이니까 따라서 쭉 갔다가 돌아오면서 방문 없애야 다른 방향으로 탐색 가능할듯
                visited[points] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    adj = [[] * (N+1) for _ in range(N+1)]

    for i in range(M):
        s, e = list(map(int, input().split()))
        adj[s].append(e)
        # 무향 그래프이므로 반대의 경우도 추가한다.
        adj[e].append(s)

    max_length = 0
    # 1번부터 N번까지 경로값을 계산한다.
    for i in range(1, N+1):
        # 시작점이 변경될 때마다, 방문 여부 초기화
        visited = [0] * (N+1)
        s = []
        s.append(i)
        visited[i] = 1
        dfs(s, 1) # 2번째 인자는 방문한 정점의 개수를 의미한다.
    print(f'#{tc} {max_length}')
