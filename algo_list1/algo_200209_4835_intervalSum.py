t_num = int(input())
for tc in range(1, t_num + 1):
    info = list(map(int, input().split()))
    cnt = info[0] # 숫자의 개수
    interval = info[1] # 구간

    numbers = list(map(int, input().split()))
    result = []

    for idx in range(0,cnt-interval+1):
        interval_sum = 0
        for number in numbers[idx:interval+idx]:
            interval_sum += number

        result.append(interval_sum)

    # 최저와 최고를 찾아, 차를 반환한다.
    max = result[0]
    min = result[0]
    for sum in result:
        if sum > max:
            max = sum
        if sum < min:
            min = sum

    print(f'#{tc} {max-min}')
