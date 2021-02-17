T = int(input())

for tc in range(0, T+1):
    # 오목인지 판별하기 위해선 총 8가지 방향으로 검사를 해야 한다.
    # 가로 2방향, 세로 2방향, 대각선 4방향 - 진행 순서에 따라 또 나뉜다.
    size = int(input())

    grid = [] # 바둑판 정보를 입력할 리스트.
    # 바둑판의 크기만큼 입력을 받아야한다.
    for i in range(0, size):
        list.extend(list(map(int,input().split())))

    tmp = 0

    # 2차원 좌표에 대해서 검사해야 하므로, 시간복잡도는 O(n**2) 이다.
    for col in range(0, size): # column 방향
        for row in range(0, size): # row 방향
            # 1. 가로방향에 대해서 검사한다. 가로 방향의 첫번째가 없으면 오목일 수가 없다.
            if grid[col][row] == 'o'

