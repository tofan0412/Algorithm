for tc in range(1, 11):
    tc_num = int(input())

    arr = [list(input()) for i in range(100)] # list로 만들지 않으면 열 우선 탐색이 안된다.
    end_row = False
    end_col = False
    ans_row = 0
    ans_col = 0

    # 행 우선 탐색 - 길이가 10인 회문부터 순차적으로 찾는다.
    for k_row in range(25,0,-1): # 회문의 길이가 100인 대상부터 1인 대상까지 찾는다.
        for i in range(len(arr)):
            for j in range(len(arr[i]) - k_row + 1):
                tmp = "" # 회문
                answer = "" # 원본

                # k는 회문의 길이를 의미한다.
                for l in range(j + k_row - 1, j - 1, -1):
                    tmp += arr[i][l]

                for m in range(j, j + k_row):
                    answer += arr[i][m]

                if tmp == answer:  # 펠린드롬이다.
                    ans_row = k_row
                    end_row = True
                    break
            if end_row:
                break
        if end_row:
            break

    # 열에 대해서 우선 탐색
    for k_col in range(25,0,-1): # 회문의 길이가 100인 대상부터 찾는다.
        for j_col in range(len(arr)):
            for i_col in range(len(arr) - k_col + 1):
                tmp = "" # 회문
                answer = "" # 원본

                # k는 회문의 길이를 의미한다.
                for l_col in range(i_col+k_col-1, i_col-1, -1):
                    tmp += arr[l_col][j_col]

                for m_col in range(i_col, i_col + k_col):
                    answer += arr[m_col][j_col]

                if tmp == answer:  # 펠린드롬이다.
                    ans_col = k_col
                    end_col = True
                    break
            if end_col:
                break
        if end_col:
            break

    if ans_row > ans_col:
        print(f'#{tc} {ans_row}')
    else:
        print(f'#{tc} {ans_col}')
