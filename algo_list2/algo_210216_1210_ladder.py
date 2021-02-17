# Answer : 목적지를 기준으로 해서, 찾아보자!

T = 10
for tc in range(1, T+1):
    case_num = int(input())
    arr = [[1,0,0,1],
           [1,0,0,1],
           [1,0,0,1],
           [1,0,0,1],
           [1,1,1,1],
           [1,0,0,1],
           [1,1,1,1],
           [1,0,0,1],
           [1,0,0,2]]

    std_row = 0
    std_col = 0
    # 도착지가 있는 열의 정보를 파악한다.
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 2:
                std_col = j
                std_row = i
    while True:
        right = std_col +1
        left = std_col -1
        # 검사
        if right >= len(arr[0]):
            print("오른쪽 열이 존재하지 않습니다.")
            # 왼쪽값과 위쪽값을 비교하면 된다.
            # 1. 둘다 1인경우
            if
            # 2. 둘중 하나만 1인 경우


        if left < 0:
            print("왼쪽 열이 존재하지 않습니다.")




