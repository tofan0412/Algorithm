T = int(input())

for tc in range(1, T+1):
    N = int(input())

    numbers = list(map(int, input().split()))

    # 가장 큰수, 가장 작은수, 가장큰수, 가장작은수,,
    for i in range(0,len(numbers),2): # i는 0, 2, 4, 6 ... 순으로 변화한다.

        # 최대값 찾기
        max_num = -9999
        max_idx = i
        for j in range(i,len(numbers)):
            # 최대값 찾기
            if max_num < numbers[j]:
                max_num = numbers[j]
                max_idx = j

        # 범위 내에서 최대값, 최소값을 찾으면 바꿔준다.
        numbers[i], numbers[max_idx] = numbers[max_idx], numbers[i]


        # 최소값 찾기
        min_num = 9999
        min_idx = i + 1
        for j in range(i, len(numbers)):
            if min_num > numbers[j]:
                min_num = numbers[j]
                min_idx = j
        numbers[i + 1], numbers[min_idx] = numbers[min_idx], numbers[i + 1]

    result = ""
    for i in range(0,10):
        result += str(numbers[i]) + " "
    print(f'#{tc} {result}')