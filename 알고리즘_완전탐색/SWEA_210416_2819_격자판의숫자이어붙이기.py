def BFS(queue, str):
    global mem
    if len(str) == 7:
        if str not in mem: # set을 이용할 수도 있다!!
            mem.append(str)
        return
    # 재귀 호출로 푼다.
    point = queue.pop(0)
    for i in range(4):
        move_to_row = point[0] + dr[i]
        move_to_col = point[1] + dc[i]

        check1 = 0 <= move_to_row and move_to_row < N
        check2 = 0 <= move_to_col and move_to_col < N
        if check1 and check2:
            queue.append((move_to_row, move_to_col))
            tmp = str
            tmp += grid[move_to_row][move_to_col] # 다음 지점
            BFS(queue, tmp)
            queue = [] # 큐 비우기


T = int(input())
for tc in range(1, T+1):
    N = 4
    grid = [list(input().split()) for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    mem = []

    for row in range(N):
        for col in range(N):
            queue = []
            queue.append((row, col))
            # 2번째 인자는 만들고 있는 수의 형태, 3번째 인자는 방문 횟수
            str = ''
            str += grid[row][col]
            BFS(queue, str)
    print(f'#{tc} {len(mem)}')