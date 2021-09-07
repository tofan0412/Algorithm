def inorder(n):
    global result
    if adjacency[n] != 0: # 인접한 노드가 있을 경우에만
        inorder(int(adjacency[n][0]))
        # print(alphabet[n], end='')
        result += alphabet[n]
        if len(adjacency[n]) > 1:
            inorder(int(adjacency[n][1]))
    else:
        # print(alphabet[n], end='')
        result += alphabet[n]
for tc in range(1, 11):
    N = int(input())
    alphabet = [0] * (N+1)
    adjacency = list([] for _ in range(N+1))
    result = ''

    for i in range(N):
        node_info = list(input().split()) # 첫번째는 해당하는 인덱스, 두번째는 알파벳, 이후는 인접한 정점이다.
        alphabet[int(node_info[0])] = node_info[1]
        v_info = node_info[2:]
        for j in v_info:
            adjacency[int(node_info[0])].append(j)
    # 인접한 대상 없으면 0 처리
    for i in range(len(adjacency)):
        if len(adjacency[i]) == 0:
            adjacency[i] = 0
    # ROOT NODE는 반드시 1부터이다.
    # 중위순회로 탐색을 시작한다.
    inorder(1)
    print(f'#{tc} {result}')