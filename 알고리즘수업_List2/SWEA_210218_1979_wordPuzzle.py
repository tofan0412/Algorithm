# N x N 크기의 단어 퍼즐을 만들려고 한다.
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 만들어라.

T = int(input())

for tc in range(1, T+1):
    N,K = list(map(int,input().split()))
    arr = [list(map(int,input().split())) for i in range(N)]
    result = 0
    # 가로길이 또는 세로길이가 정확히 3인 지점을 찾아야 한다.
    for i in range(N):
        for j in range(N):
            pass
