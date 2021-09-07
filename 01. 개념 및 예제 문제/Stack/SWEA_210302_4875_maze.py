T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for i in range(N)]

    # 출발지는 2로 표시한다.
    #  도착지는 3으로 시작한다.

    # 델타를 이용한다.
    # 상, 하, 좌, 우를 모두 고려한다.
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 시작점과 도착점을 찾는다.
    start = []
    end = []
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                start = [row, col]
            if maze[row][col] == '3':
                end = [row, col]

    # 시작점에서 출발한다.
    # 더이상 이동할 수 없으면 끝난다.

    # stack을 이용하는 방법과
    # 재귀함수를 이용하는 방법이 존재한다.
    stack = []
    stack.append(start)
    while len(stack) != 0:
        # stack의 top이 현재 위치이다.
        # 4방향을 모두 검사한다.
        now = stack.pop(-1)

        up = now[0] + dr[0]
        down = now[0] + dr[1]
        left = now[1] + dc[2]
        right = now[1] + dc[3]

        # 이제 이동할 수 있는 방향을 찾는다.
        # 한방향부터 확인하는 것이 아닌, 전방향을 모두 확인한다.
        if 0 <= up and up < N: # 이동가능한가?
            if maze[up][now[1]] == '3':
                print(f'#{tc} 1')
                break
            if maze[up][now[1]] == '0':
                stack.append([up, now[1]])
                maze[up][now[1]] = '99'

        if 0 <= down and down < N: # 이동가능한가?
            if maze[down][now[1]] == '3':
                print(f'#{tc} 1')
                break
            if maze[down][now[1]] == '0':
                stack.append([down, now[1]])
                maze[down][now[1]] = '99'

        if 0 <= left and left < N: # 이동가능한가?
            if maze[now[0]][left] == '3':
                print(f'#{tc} 1')
                break
            if maze[now[0]][left] == '0':
                stack.append([now[0], left])
                maze[now[0]][left] = '99'

        if 0 <= right and right < N:
            if maze[now[0]][right] == '3':
                print(f'#{tc} 1')
                break
            if maze[now[0]][right] == '0':
                stack.append([now[0], right])
                maze[now[0]][right] = '99'

    # 여기까지 왔다는건, 찾지 못했다는 뜻이다.
    else:
        print(f'#{tc} 0')



