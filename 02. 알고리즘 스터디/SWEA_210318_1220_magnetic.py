def rotate_90(m):
    N = len(m)
    rotation = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            rotation[c][N-1-r] = m[r][c]
    return rotation

for tc in range(1, 11):
    N = int(input())
    table = [input().split() for _ in range(N)]
    result = 0
    # 1은 N극 자성을 갖는 자성체를, 2는 S극 자성을 갖는 자성체이다.

    # 배열을 오른쪽으로 90도 회전하자. 이 경우 오른쪽이 N극이 되고, 왼쪽이 S극이 된다.
    ret = rotate_90(table)

    # 테이블에 떨어져 나갈 애들은 미리 없앤다.
    # 이 부분이 사실 의미가 없다. 하단에서 처리해도 된다.
    for r in range(N):
        for c in range(N):
            if ret[r][c] == '1': # N극이다. 왼쪽에 다른 극성이 없는 경우 떨어진다.
                if c == 0: # 가장 왼쪽에 있는 경우는 고려하지 않아도 된다.
                    ret[r][c] = '0'
                elif '2' not in ret[r][0:c]:
                    ret[r][c] = '0'
                    for i in range(0, c+1):
                        ret[r][i] = '0'
            elif ret[r][c] == '2': # S극이다. 오른쪽에 다른 극성이 없는 경우 떨어진다.
                if c == N - 1: # 가장 마지막 컬럼인 경우 고려안해도 된다.
                    ret[r][c] = '0'
                elif '1' not in ret[r][c+1:]: # 가장 오른쪽에 있는 대상은 어케?
                    for i in range(c,N):
                        ret[r][i] = '0'

    # 떨어뜨릴 대상을 모두 떨어뜨렸으므로, 이제 교착상태인 대상만 count하면 된다.
    # 하단의 부분은 Stack으로 하면 더 간단하게 할 수 있음
    for r in range(N):
        for c in range(N-1): # 왼쪽에서 오른쪽으로 탐색한다. 따라서 왼쪽에는 반드시 S라는 대상이 막고 있어야 하며, 오른쪽에는 N이라는 대상이 막고 있어야 한다.
            if ret[r][c] == '2':
                for i in range(c, N):
                    # 현재 위치부터 마지막 위치까지 탐색한다.
                    if ret[r][i] == '1':
                        for j in range(0,i):
                            ret[r][j] = '0' # 해당 값까지 0으로 바꿔준다.
                        result += 1
                        break
    print("#{} {}".format(tc, result))

