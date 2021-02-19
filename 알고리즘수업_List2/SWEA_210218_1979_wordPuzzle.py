# N x N 크기의 단어 퍼즐을 만들려고 한다.
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 만들어라.

T = int(input())

for tc in range(1, T+1):
    # N은 퍼즐의 크기, K는 단어의 길이를 의미한다.
    N,K = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for i in range(N)]
    result = 0

    # 가로에 대해서 행 우선 탐색.
    for i in range(N):
        j = 0
        while j < len(arr[i]):
            if arr[i][j] == 1:
                cnt = 0
                while arr[i][j] != 0:
                    cnt += 1
                    j += 1
                    # j의 범위가 벗어나는 경우 while문을 종료한다.
                    if j >= len(arr[i]):
                        break

                if cnt == K:
                    result += 1
            else:
                j += 1
                continue

    for j in range(N):
        i = 0
        while i < len(arr):
            cnt = 0
            if arr[i][j] == 1:
                cnt = 0
                while arr[i][j] != 0:
                    cnt += 1
                    i += 1
                    # i의 범위가 벗어나는 경우 while문을 종료한다.
                    if i >= len(arr):
                        break

                if cnt == K:
                    result += 1
            else:
                i += 1
                continue

    print(f'#{tc} {result}')


# Answer
ans = 0 # 정답을 위한 변수 선언.

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == 1:
            cnt += 1
        if arr[i][j] or j == N-1: # 끝자리이거나, 값이 1이라면
            # 벽을 만났을 때 그동안 쌓아온 cnt값이 K이어야만 들어갈 수 있다.
            if cnt == K:
                ans += 1
            cnt = 0

    # 열을 검사한다.
    for j in range(N):
        if arr[j][i] == 1:
            cnt += 1
        if arr[j][i] or  j == N-1: # 끝자리이거나, 값이 1이라면
            # 벽을 만났을 때 그동안 쌓아온 cnt값이 K이어야만 들어갈 수 있다.
            if cnt == K:
                ans += 1
            cnt = 0


# 꿀팁
# row방향, col 방향에 벽을 하나 추가하였다.
# 장점 :j == N-1 코드를 고려하지 않아도 된다.
# 인덱스 검사를 하지 않기 위해, 한 폭의 벽을 외부에 추가한다!

# 벽 만들기
puzzle = [list(map(int,input().split()))+[0] for _ in range(N)]

puzzle.append([0]*(N+1))