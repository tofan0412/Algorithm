# 너비 우선 탐색 실습

v_info = [0, [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [False]*len(v_info)
start = 6
queue = []
result = ''

queue.append(start)
result += str(start) + ' '
visited[start] = True
while queue: # 모든 지점을 다 방문할 때까지 반복 수행한다.
    visit = queue.pop(0)
    for i in v_info[visit]:
        if not visited[i]:
            queue.append(i)
            result += str(i) + ' '
            visited[i] = True # 방문했다고 표시한다.
    print(visited)
print(result)

# 주목해야 할 점: 인접행렬로 표현했을 때는 어떻게 해야 하나?
