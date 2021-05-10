def dijkstra(s):
    D = [0xffffff] * (N + 1)    # 정점 사이의 거리를 매우 큰 초기값으로 설정
    P = [i for i in range(N + 1)]   # 부모를 표시할 곳
    visited = [0] * (N + 1)     # 방문을 했는지를 통해서 한번만 계산
    D[s] = 0    # 처음 시작하는 곳은 자기자신과의 거리임으로 0으로 설정
    cnt = 0 # 0번 정점에서 출발

    while cnt < N:
        u, MIN = 0, 0xffffff    # 임의의 값 설정 prim과 비슷
        for i in range(N + 1):
            if not visited[i] and MIN > D[i]:
                u, MIN = i, D[i]
        visited[u] = 1  # 방문 체크를 통해 다음에는 안해도 됨

        for v, w in G[u]:
            if not visited[v] and D[v] > D[u] + w:
                D[v] = D[u] + w     # 선택한 정점의 인접 정점에서 바로 가는 것과 경유하는 것중 어느것이 빠른지 저장
                P[v] = u    # 경유하는 부모 저장(경유를 하면 바뀌고 경유하지 않으면 자기 자신)
        cnt += 1

    return D[N]     # 시작점에서 N번까지 갈 때 최단 경로


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(E)]
    for i in range(E):
        # u는 출발 정점, v는 도착 정점, w는 가중치
        u, v, w = map(int, input().split())
        G[u].append([v, w])

    print('#{} {}'.format(tc, dijkstra(0)))