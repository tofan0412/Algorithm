# 스도쿠 검증하기
T = int(input())

for tc in range(1, T+1):
    sudoku = []
    for i in range(9):
        sudoku += [list(map(int,input().split()))]
    result = 1
    #1. 가로 방향에 대해서 검사하기
    for i in range(len(sudoku)):
        cnt = [0] * 9
        for j in range(len(sudoku)):
            cnt[sudoku[i][j]-1] += 1

        # 한 줄의 검사가 끝나면 이곳으로 내려온다.
        # cnt의 모든 원소값이 1이어야 한다.
        if 0 in cnt:
            result = 0
            break # 바깥 for문을 중단.

    # 2. 세로 방향에 대해서 검사한다.
    for col in range(len(sudoku)):
        cnt = [0] * 9
        for row in range(len(sudoku)):
            cnt[sudoku[row][col]-1] += 1
        if 0 in cnt:
            result = 0
            break # 바깥 for문을 중단.

    # 3. 9개의 칸에 대해서 검사한다. - 기준점을 잡는다.
    std = [[0, 0],[0, 3],[0, 6],
           [3, 0],[3, 3],[3, 6],
           [6, 0], [6, 3], [6, 6]]

    for i in std:
        cnt = [0] * 9
        s = i[0]
        e = i[1]
        for j in range(s, s+3): # row방향
            for k in range(e, e+3): # col방향
                cnt[sudoku[j][k]-1] += 1
        if 0 in cnt:
            result = 0
            break # 기준점에 대한 for문을 종료한다.

    print(f'#{tc} {result}')
