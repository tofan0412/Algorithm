# 후위순회로 하기!
# 완전 이진 트리가 아니다..
def inorder(n): # 이 때, n은 노드 번호를 의미한다.
    if n != 0:
        if ch1[n] != 0:
            inorder(ch1[n])
            inorder(ch2[n])

        if type(tree[n]) == str:
            if tree[n] == '-':
                tree[n] = tree[ch1[n]] - tree[ch2[n]]
            if tree[n] == '+':
                tree[n] = tree[ch1[n]] + tree[ch2[n]]
            if tree[n] == '*':
                tree[n] = tree[ch1[n]] * tree[ch2[n]]
            if tree[n] == '/':
                tree[n] = tree[ch1[n]] / tree[ch2[n]]


for tc in range(1, 11):
    N = int(input()) # 트리가 갖는 정점의 총수. 이 때 간선의 개수는 N-1개이다.
    # 정점이 단순한 수이면 정점번호와 해당 양의 정수가 주어지고
    # 정점이 연산자이면 정점번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점번호가 차례대로 주어진다.
    tree = [0] * (N+1)
    ch1 = [0] * (N+1)
    ch2 = [0] * (N+1)

    for i in range(N):
        node_info = list(input().split())
        if len(node_info) == 4: # 연산자, 왼쪽 자식노드와 오른쪽 자식 노드 인덱스 번호를 포함한다.
            tree[int(node_info[0])] = node_info[1] # 부모 노드는 연산자.
            ch1[int(node_info[0])] = int(node_info[2])
            ch2[int(node_info[0])] = int(node_info[3])
        else: # 잎 노드 번호와 그 값만 알려주는 경우.
            tree[int(node_info[0])] = int(node_info[1])

    inorder(1)
    print(f'#{tc} {round(tree[1])}')