T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [[0]*(N+2) for i in range(N+2)] # NxN 크기의 바둑판 만들기 & 벽 두르기
    arr[0][:] = [99]*(N+2)
    arr[-1][:] = [99]*(N+2)
    for i in range(N+2):
        arr[i][0] = 99
        arr[i][-1] = 99

    # 4개의 돌을 기본적으로 배치한다.
    center = len(arr) // 2
    arr[center][center] = 2
    arr[center][center - 1] = 1
    arr[center - 1][center] = 1
    arr[center - 1][center - 1] = 2
    # 돌 개수 집계하기 위한 변수
    white_cnt = 0
    black_cnt = 0

    for i in range(M):
        # M번동안 돌을 놓기 시작한다.
        # 1은 흑돌, 2이면 백돌을 의미한다.
        col,row,color = list(map(int, input().split()))
        # 벽을 세웠기 때문에 안 더해줘도 된다.

        other_color = 9999
        if color == 1:
            other_color = 2
        else:
            other_color = 1
        # 돌을 뒀다는건, 사이 혹은 대각선에 상대방의 돌이 존재한다는 뜻이다.
        arr[row][col] = color

        if arr[row - 1][col] == other_color:
            # 위쪽 방향으로 진행한다.
            idx = row - 1

            chk = False
            # 상단에 닫아주는 값이 있는지를 확인해야 한다.
            for i in range(idx, -1, -1):  # 다음값부터 확인한다.
                if arr[i][col] == color:
                    chk = True
            if chk:
                while arr[idx][col] == other_color:
                    arr[idx][col] = color
                    idx -= 1

        if arr[row + 1][col] == other_color:
            # 아래쪽 방향으로 진행한다.
            idx = row + 1

            chk = False
            # 하단에 닫아주는 값이 있는지를 확인해야 한다.
            for i in range(idx, len(arr)): # 다음값부터 확인한다.
                if arr[i][col] == color:
                    chk = True

            if chk:
                while arr[idx][col] == other_color:
                    arr[idx][col] = color
                    idx += 1

        if arr[row][col - 1] == other_color:
            # 왼쪽 방향으로 진행한다.
            idx = col - 1

            chk = False
            # 좌측에 닫아주는 값이 있는지를 확인해야 한다.
            for i in range(idx, -1, -1):  # 다음값부터 확인한다.
                if arr[row][i] == color:
                    chk = True
            if chk:
                while arr[row][idx] == other_color:
                    arr[row][idx] = color
                    idx -= 1

        if arr[row][col + 1] == other_color:
            # 오른쪽 방향으로 진행한다.
            idx = col + 1

            chk = False
            for i in range(idx, len(arr)):  # 다음값부터 확인한다.
                if arr[row][i] == color:
                    chk = True
            if chk:
                while arr[row][idx] == other_color:
                    arr[row][idx] = color
                    idx += 1

        # 대각선 방향 검사
        # 왼쪽위방향 검사
        if arr[row - 1][col - 1] == other_color:
            r = row - 1
            c = col - 1
            chk = False
            while arr[r][c] != 99:
                if arr[r][c] == color:
                    chk = True
                r -= 1
                c -= 1
            r = row - 1
            c = col - 1
            if chk:
                while arr[r][c] == other_color:
                    arr[r][c] = color
                    r -= 1
                    r -= 1

        # 오른쪽위방향 검사
        if arr[row - 1][col + 1] == other_color:
            r = row - 1
            c = col + 1
            chk = False
            while arr[r][c] != 99:
                if arr[r][c] == color:
                    chk = True
                r -= 1
                c += 1

            r = row - 1
            c = col + 1
            if chk:
                while arr[r][c] == other_color:
                    arr[r][c] = color
                    r -= 1
                    c += 1

        #왼쪽아래방향 검사
        if arr[row + 1][col - 1] == other_color:
            r = row + 1
            c = col - 1
            chk = False
            while arr[r][c] != 99:
                if arr[r][c] == color:
                    chk = True
                r += 1
                c -= 1

            r = row + 1
            c = col - 1
            if chk:
                while arr[r][c] == other_color:
                    arr[r][c] = color
                    r += 1
                    c -= 1

        #오른쪽아래방향 검사
        if arr[row + 1][col + 1] == other_color:
            r = row + 1
            c = col + 1
            chk = False
            while arr[r][c] != 99:
                if arr[r][c] == color:
                    chk = True
                r += 1
                c += 1
            r = row + 1
            c = col + 1
            while arr[r][c] == other_color:
                arr[r][c] = color
                r += 1
                c += 1

    # 마지막에 흑돌, 백돌 개수 세기
    for row in range(N+2):
        for col in range(N+2):
            if arr[row][col] == 1:
                black_cnt += 1
            elif arr[row][col] == 2:
                white_cnt += 1

    print(f'#{tc} {black_cnt} {white_cnt}')







