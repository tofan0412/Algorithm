T = int(input())

for tc in range(1, T+1):
    # 배열의 크기
    N = int(input())
    # 각 row에서 어떠한
    array = [list(map(int, input().split())) for i in range(N)]
    log = [] # 각 row에서 어떤 col의 값을 선택했는지를 기록한다.
    cand_all = []

    # 가장 먼저, 기준이 될 최소값의 합을 구한다.

    for row in range(N):
        min_value = 100
        min_idx = 0
        for col in range(N):
            if col not in log: # 최소값이 있는 col에 기록되어 있지 않으면서
                if min_value >= array[row][col]:
                    min_value = array[row][col]
                    min_idx = col
            else:
                continue
        # 최소값만 픽픽
        cand_list = []
        for j in range(N):
            if array[row][j] == min_value:
                cand_list.append(array[row][j])
        cand_all.append(cand_list)
    print(cand_all)