def BFS(sV):
    Q = [[sV, 0]]
    visited = [False] * (V+1)
    visited[sV] = True

    while Q:
        v, dist = Q.pop(0)
        if v == eV:
            return dist

        for i in range(1, V+1):
            if adj_arr[v][i] == 1 and visited == False:
                Q.append([i, dist + 1 ])
                visited[i] = True
    # 도달하지 못하는 경우도 생각해야 한다.
    return 0

def BFS2(sV):
    Q = [sV]
    visited = [False] * (V + 1)
    visited[sV] = True

    dist = 0
    while Q:
        size = len(Q) # 사이즈로 묶어서 돌린다!
        for i in range(size):
            v = Q.pop(0)
            if v == eV: return dist

            for i in range(1, V+1):
                if not visited[i] and adj_arr[v][i]:
                    Q.append(i)
                    visited[i] = True
        dist += 1
    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = list(map(int, input().split()))

    # 인접행렬을 이용하여 작성해보자.
    adj_arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        a, b = map(int,input().split())
        #무방향이므로 양쪽 연결
        adj_arr[a][b] = 1
        adj_arr[b][a] = 1

    # 시작점, 끝접
    sV, eV = map(int, input().split())

    print(f'#{tc} {BFS(sV)}')

