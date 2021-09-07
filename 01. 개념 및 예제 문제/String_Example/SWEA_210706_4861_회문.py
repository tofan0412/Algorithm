# 회문은 가로로 존재할 수도 있고, 세로로 존재할 수도 있다.
# NxN의 글자판에서 길이가 M인 회문을 찾아 출력하시오.

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(input()) for _ in range(N)]

    # 행 우선 탐색, 열 우선 탐색을 각각 진행한다.
    InitialIdx = 0
    startIdx = 0
    endIdx = 0
    result = ""

    # 열 우선 탐색
    for i in range(N):
        for j in range(M):
            startIdx, InitialIdx = j
            endIdx = j + (M - 1)
            # IndexError 방지
            if endIdx < N:
                # Index 조건을 충족하면 회문 검사 시작
                while True:
                    if board[i][startIdx] == board[j][endIdx]:
                        startIdx += 1
                        endIdx -= 1
                        # 만약 startIdx와 endIdx가 일치하면 회문이라는 뜻이다.
                        if startIdx == endIdx:
                            result = board[i][InitialIdx:InitialIdx+M]
                            print()
                            break
                    else:
                        break
