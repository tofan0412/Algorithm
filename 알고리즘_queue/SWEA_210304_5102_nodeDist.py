T = int(input())

for tc in range(1, T+1):
    V, E = list(map(int, input().split()))
    v_info = []
    for i in range(V+1):
        v_info.append([])

    for i in range(E):
        # 이 때 s, e는 간선으로 연결된 양쪽 노드 번호이다.
        n1, n2 = list(map(int, input().split()))
        v_info[n1].append(n2)
        v_info[n2].append(n1)

    start, end = list(map(int, input().split()))
    visited = [False] * (V+1)
    node_distance = [0] * (V+1)
    node_distance[start] = 0 # 출발점의 거리는 0이다.
    queue = []
    queue.append(start)
    visited[start] = True

    while queue:
        t = queue.pop(0) # 1,2,3,4,5,6이 t에 올 수 있다.
        # t번과 연결되어 있는 노드는 어떠한 것이 있는지 조사한다.
        for v in v_info[t]:
            if visited[v] == False: # 아직 방문하지 않았다는 것을 뜻한다.
                queue.append(v)
                node_distance[v] = node_distance[t] + 1
                visited[v] = True

    if visited[n2] == False:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {node_distance[end]}')

