# 가운데 포지션은 N // 2를 통해 잡을 수 있다.

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input())) for i in range(N)]

    center = N // 2 # 가운데 인덱스를 의미한다.
    result = 0
    cnt = len(arr)-1
    for row in range(N):
        tmp = []
        if row < center:
            tmp = arr[row][center-row:center+row+1]
        elif row >= center:
            tmp = arr[row][center-cnt:center+cnt+1]

        for element in tmp:
            result += element
        cnt -= 1

    print(f'#{tc} {result}')

