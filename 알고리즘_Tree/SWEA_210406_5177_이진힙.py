T = int(input())

for tc in range(1, T+1):
    V = int(input()) # 노드의 수
    nums = list(map(int, input().split()))
    nodes = [0]*(V + 1)

    for i in range(1, len(nums)+1):
        nodes[i] = nums[i-1]
        # 부모와 자식 간의 값을 비교해야 한다.
        # 부모 노드의 번호는 자식 노드의 번호 // 2

        # 모든 조상에 대해 다 검사를 해야 함.
        # 오른쪽, 왼쪽 모두 검사해야 함.
        # 자식은 *2(왼쪽) 또는 *2+1(오른쪽)
        parent = i // 2
        child = i
        while True:
            if parent == 0:
                break
            if nodes[parent] > nodes[child]:
                nodes[parent], nodes[child] = nodes[child], nodes[parent]
            child = parent
            parent = parent // 2

    # 조상 노드 찾기
    pointer = len(nodes)-1
    result = 0
    while True:
        if pointer // 2 == 0:
            break
        result += nodes[pointer // 2]
        pointer = pointer // 2
    # print(nodes)
    print(f'#{tc} {result}')