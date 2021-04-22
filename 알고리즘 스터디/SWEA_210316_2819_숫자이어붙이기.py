T = int(input())
for tc in range(1, T+1):
    dr, dc = [-1,1,0,0], [0,0,-1,1]
    N = 4
    grid = [list(input().split()) for _ in range(N)]
    result = []

    def check(idx, arr, pos, string=''):
        row, col = pos
        string += grid[row][col] # 현재 내 위치값 tmp에 추가하기
        if idx == 7:
            result.append(string)
            tmp = ''  # 임시값의 초기화
            return

        for i in range(4): # 사방 탐색을 실시한다.
            row_to, col_to = row + dr[i], col + dc[i]
            factor = (0 <= row_to and row_to < N) and (0 <= col_to and col_to < N)  # grid 범위 안에 존재한다.
            if factor:  # 사방 중 값이 존재하는 대상에 대해
                idx += 1
                string += grid[row_to][col_to]
                pos = [row_to, col_to]
                check(arr, pos, string)

    # 각각의 항목에 대해서 확인한다.
    for row in range(len(grid)):
        for col in range(len(grid)):
            check(0, grid, [row, col], '')
    print('#{} {}'.format(tc, len(result)))

