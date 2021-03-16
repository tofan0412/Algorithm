# 길찾기 문제
for tc in range(1,11):
    T, V = list(map(int, input().split()))
    adjacency = []
    for i in range(100):
        adjacency.append(list([]))

    info = list(map(int,input().split())) # 이 때 이 리스트의 길이는 V이다.
    for i in range(0,V*2,2):
        adjacency[info[i]].append(info[i+1])

    visited = [False]*100
    stack = []

    # 시작점은 0, 도착점은 99로 표현된다.
    pointer = 0 # 가장 처음 포인터는 시작점을 가리킨다.

    while True:
        visited[pointer] = True # 방문했으므로 True로 변경한다.

        # 인접한 노드를 조사한다.
        for i in adjacency[pointer]:
            if visited[i] != True: # 이전에 방문한 적이 없다면
                stack.append(pointer)
                pointer = i
                break
            else:
                continue
        else: # 인접한 노드가 없거나, 이웃한 노드를 모두 방문한 경우 이곳으로 오게 된다.
            if len(stack) == 0: # 스택에 쌓인 노드가 없는 경우 while을 중지한다.
                break
            pointer = stack[-1]
            stack.pop(-1)

    if visited[99]: # 99가 True이면 DFS 탐색동안 갈 수 있었다는 뜻이다.
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')






