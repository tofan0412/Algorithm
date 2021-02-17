for tc in range(1, 11):
    num = int(input())
    # 입력받기
    arr = []
    for row in range(0,100):
        tmp = list(map(int,input().split()))
        arr.append(tmp)

    result = []
    # 가로합을 계산해보자.
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            sum += arr[i][j]
        result.append(sum)

    # 세로합을 계산해보자.
    for i in range(len(arr)):
        sum = 0
        for j in range(len(arr)):
            sum += arr[j][i]
        result.append(sum)

    # 대각선의 합을 계산해보자. ( 아래로 내려가는 대각선 )
    sum = 0
    for i in range(len(arr)):
        sum += arr[i][i]
    result.append(sum)

    sum = 0
    for i in range(len(arr)):
        sum += arr[i][len(arr)-1-i]
    result.append(sum)

    print(f'#{num} {max(result)}')

