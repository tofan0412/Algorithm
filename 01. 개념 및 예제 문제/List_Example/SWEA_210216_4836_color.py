T = int(input())

# 이 때, arr는 11 X 11의 배열이다.

for tc in range(1, T+1):
    arr = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    N = int(input()) # 색칠할 영역의 개수
    result = 0

    # N의 수만큼 info를 받아야 한다.
    for i in range(0, N):
        info = list(map(int, input().split()))

        x = [info[0],info[2]+1] # x값의 범위. +1 하는 이유 : 좌표가 아닌 칸으로 생각하므로..
        y = [info[1],info[3]+1] # y값의 범위
        color = info[4]

        # p1 ~ p2 사이에 해당하는 영역을 color로 marking한다.
        for i in range(x[0], x[1]+1):
            for j in range(y[0], y[1]+1):
                arr[i][j] += color # color값을 더해야 한다.

    # 찾기
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[i][j] == 3:
                if arr[i+1][j+1] == 3:
                    result += 1

    print(f'#{tc} {result}')


# Answer

arr = [list(map(int, input().split())) for i in range(N)]

arr_r = [[0]*10 for i in range(10)]

cnt = 0
for i in range(N):
    r1 = arr[i][0]
    c1 = arr[i][1]
    r2 = arr[i][2]
    c2 = arr[i][3]

    for x in range(r1, r2+1):
        for y in range(c1, c2 + 1):
            arr_r[x][y] += arr[i][4]

    for i in range(10):
        for j in range(10):
            if arr_r[i][j] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')