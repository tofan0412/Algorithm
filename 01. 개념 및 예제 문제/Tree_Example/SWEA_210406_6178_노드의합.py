T = int(input())
for tc in range(1, T+1):
    N, M, L = list(map(int, input().split())) # N은 노드의 개수, M은 리프 노드의 개수, 값을 출력할 노드 번호 L
    # M개의 줄에 걸쳐 리프노드 번호와 1000 이하의 자연수가 주어진다.
    nodes = [0] * (N + 1)
    for i in range(M):
        leaf_node_idx, value = list(map(int, input().split()))
        nodes[leaf_node_idx] = value

    # leaf node의 부모의 값을 채워야 한다.
    for i in range(len(nodes)-1, -1,-1):
        parent = i // 2
        nodes[parent] += nodes[i]
    result = nodes[L]
    print(f'#{tc} {result}')

