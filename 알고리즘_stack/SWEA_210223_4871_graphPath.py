T = int(input())

for tc in range(1, T+1):
    V,E = list(map(int, input().split())) # V는 노드의 개수, E는 간선의 개수를 의미한다.

    adjacency_info = []
    for i in range(V+1):
        adjacency_info.append(list([])) # deepcopy를 하지 않으면 주소값이 모두 동일해서 안된다.

    # 인접정보를 받는다.
    for i in range(E):
        n1, n2 = list(map(int, input().split()))
        # n1을 기준으로 adjacency_info에 정보를 채운다.
        adjacency_info[n1].append(n2)

    # 마지막으로 시작점과 도착점 정보를 받는다.

    S,G = list(map(int, input().split()))

    # 시작점 S부터 검사를 시작한다. 이 때, 모든 경로를 검사해서 visited에 도착점이 있다면, 해당 노드까지 갈 수 있는 것이다.
    visited = [] # 방문한 노드 ** True,False로 하는게 낫다.
    stack = [] # 분기점
    target = S # 현재 노드 포인터를 나타낸다.

    # 스택이 비어있지 않은 동안 수행한다.
    while True:
        # # 최초 방문한 경우에만 visited에 추가한다.
        # if target not in visited:
        visited.append(target)

        # 인접한 노드를 조사한다.
        for i in adjacency_info[target]:
            # 이 때, 어디로 갈지는 상관 없다.
            if i not in visited: # 인접한 노드 중 방문한 적이 없는 노드인 경우
                # 현재 포인터에서 방문한 적이 없는 노드가 존재하므로, stack에 현재 포인터를 쌓아둔다.
                stack.append(target)
                target = i
                # 여러 방문 가능한 노드 중 한 곳만 방문해야 하므로 break을 추가한다.
                break
            else: # 다른 애도 검사한다.
                continue
        else: # 인접한 node가 없거나, for문이 끝난 경우!
            # pointer를 stack의 최상단으로 옮기고, pop()한다.
            if len(stack) == 0:
                break
            target = stack[-1]
            stack.pop(-1)
    if G in visited:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')