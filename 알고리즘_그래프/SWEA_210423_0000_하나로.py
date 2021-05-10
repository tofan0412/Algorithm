def find_set(x, p):
    while x != p[x]:
        x = p[x]
    return x


def Kruskal(N):
    p = [i for i in range(N)] # 대표 원소 초기화
    L2 = 0
    cnt = 0

    for w, u, v in edge:
        if find_set(u, p) != find_set(v, p):
            p[find_set(v)] = find_set(u)
            cnt += 1
            L2 += w
            if cnt == N - 1: # N-1개의 edge가 선택이 되었다면
                return L2


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    # 완전 그래프 정리
    adj = [[0] * N for _ in range(N)] # 인접행렬
    for i in range(N):
        for j in range(N):
            adj[i][j] = (X[i] - X[j])**2 + (Y[i] - Y[j])**2
            adj[j][i] = adj[i][j]   # 무향 그래프

    edge = [] # 간선 정보 기준 저장
    for i in range(N):
        for j in range(i+1, N): # 무향 그래프이기 때문에 절반만 추가했다.
            edge.append(((X[i]- X[j])**2 + (Y[i] - Y[j])**2), i, j)
    edge.sort()

