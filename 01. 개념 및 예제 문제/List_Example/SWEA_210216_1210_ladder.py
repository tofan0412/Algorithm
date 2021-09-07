T = 10
for tc in range(1, T+1):
    tc_num = int(input())

    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    answer_col = 0
    # 마지막 행에서 2가 어디에 있는지 찾는다.
    for col in range(0, len(arr[-1])):
        if arr[99][col] == 2:
            answer_col = col # 도착지가 있는 곳의 열을 마킹한다.
            break

    # 현재 위치를 좌표로 저장한다.
    row_now = len(arr)-1
    col_now = answer_col
    while row_now >= 0: # row_now가 0이면 그 때의 col을 반환하면 된다.
        # print(f'현재 row는 {row_now}입니다.')
        if row_now == 0: # 도착했으면 while문을 끝내고, 어떤 col이 정답인지 반환한다.
            print(f"#{tc_num} {col_now}")
            break

        # 포인트 : 왔던 길은 값을 바꿔준다..
        left = col_now - 1
        if left >= 0: # 왼쪽 벽에 붙어있으면 패스
            if arr[row_now][left] == 1:
                # 먼저, 내가 위치한 곳의 값을 바꿔준다.
                arr[row_now][col_now] = 3
                col_now = left
                continue
            else:
                pass

        right = col_now + 1
        if right < 100: # 오른쪽 벽에 붙어있으면 패스
            if arr[row_now][right] == 1:
                arr[row_now][col_now] = 3
                col_now = right
                continue
            else:
                pass

        up = row_now - 1
        if up >= 0:
            if arr[up][col_now] == 1:
                arr[row_now][col_now] = 3
                row_now = up
                continue

# 수정할 수 있는 점 : 한번 다리를 건너기 시작하면, 0이 나올때까지 직진할 수 있다.
# 또한 양쪽에 0이 없는 동안 위로 직진으로 올라갈 수 있다.
# 무한루프 방지 :