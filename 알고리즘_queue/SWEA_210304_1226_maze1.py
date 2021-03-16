for tc in range(1, 11):
    tc_num = int(input())

    maze = [list(input()) for i in range(16)]
    s_point = 0
    e_point = 0
    for row in range(16):
        for col in range(16):
            if maze[row][col] == '2':
                s_point = (row, col)
            if maze[row][col] == '3':
                e_point = (row, col)

    queue = []
    queue.append(s_point)

    # 상,하,좌,우를 확인한다.
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    result = 0

    while queue:
        if maze[e_point[0]][e_point[1]] == 99:
            result = 1
            break

        t = queue.pop(0)
        row = t[0]
        col = t[1]

        up = row + dr[0]
        down = row + dr[1]
        left = col + dc[2]
        right = col + dc[3]

        if 0 <= up and up < 16:
            if maze[up][col] == '0' or maze[up][col] == '3':
                maze[up][col] = 99
                queue.append((up, col))

        if 0 <= down and down < 16:
            if maze[down][col] == '0' or maze[down][col] == '3':
                maze[down][col] = 99
                queue.append((down, col))

        if 0 <= left and left < 16:
            if maze[row][left] == '0' or maze[row][left] == '3':
                maze[row][left] = 99
                queue.append((row, left))

        if 0 <= right and right < 16:
            if maze[row][right] == '0' or maze[row][right] == '3':
                maze[row][right] = 99
                queue.append((row, right))
    print(f'#{tc} {result}')