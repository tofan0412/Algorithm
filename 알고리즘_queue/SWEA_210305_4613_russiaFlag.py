T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    flag = [list(input()) for _ in range(N)]
    cnt = 0

    for i in range(M):
        if flag[0][i] != 'W':
            flag[0][i] = 'W'
            cnt += 1
    for i in range(M):
        if flag[N-1][i] != 'R':
            flag[N - 1][i] = 'R'
            cnt += 1

    blue_cnt = [0] * N
    cost = [2000] * N
    for row in range(N):
        for col in range(M):
            if flag[row][col] == 'B':
                blue_cnt[row] += 1

    for row in range(len(blue_cnt)):
        if blue_cnt[row] != 0:
            cost[row] = 0
            cost[row] += M - blue_cnt[row]

            for i in range(0, row):
                for j in range(M):
                    if flag[i][j] != 'W':
                        cost[row] += 1
            for i in range(row+1, N):
                for j in range(M):
                    if flag[i][j] != 'R':
                        cost[row] += 1

    blue_row = cost.index(min(cost))
    for i in range(M):
        if flag[blue_row][i] != 'B':
            flag[blue_row][i] = 'B'
            cnt += 1

    for row in range(1, blue_row):
        other_c = 0
        blue_c = 0
        for col in range(M):
            if flag[row][col] == 'B':
                blue_c += 1
            else:
                other_c += 1
        if blue_c >= other_c:
            for col in range(M):
                if flag[row][col] != 'B':
                    flag[row][col] = 'B'
                    cnt += 1
        else:
            for col in range(M):
                if flag[row][col] != 'W':
                    flag[row][col] = 'W'
                    cnt += 1

    for row in range(blue_row+1, N):
        other_c = 0
        blue_c = 0
        for col in range(M):
            if flag[row][col] == 'B':
                blue_c += 1
            else:
                other_c += 1
        if blue_c >= other_c:
            for col in range(M):
                if flag[row][col] != 'B':
                    flag[row][col] = 'B'
                    cnt += 1
        else:
            for col in range(M):
                if flag[row][col] != 'R':
                    flag[row][col] = 'R'
                    cnt += 1

    print(f'#{tc} {cnt}')