T= int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for i in range(N)] # list로 만들지 않으면 열 우선 탐색이 안된다.

    # 회문 검사 시작
    for i in range(len(arr)): # 행 우선 탐색
        for j in range(len(arr[i]) - M + 1): # 알파벳 하나마다 검사
            tmp = ""
            answer = ""
            for k in range(j+M-1, j-1,-1):
                tmp += arr[i][k]

            for l in range(j, j+M):
                answer += arr[i][l]

            if tmp == answer: # 펠린드롬이다.
                print(f'#{tc} {tmp}')
                break

    # 열 우선 탐색
    for j in range(len(arr)):
        for i in range(len(arr) - M + 1): # 알파벳 하나마다 검사
            tmp = ""
            answer = ""
            for k in range(i+M-1, i-1,-1):
                tmp += arr[k][j]

            for l in range(i, i+M):
                answer += arr[l][j]

            if tmp == answer:
                print(f'#{tc} {tmp}')
                break