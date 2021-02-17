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

# 구한 값을 통해 Bubble sort를 해서 min, max를 구할 수도 있다.

# Answer2 : Window Slicing

# 구간합을 구할 때, 각 구간마다 중복 연산이 있다는 점을 살펴봐야 한다. -> 중복 연산을 피하자!
# [1,4,5,2,8,3,7,10]
# 1,4,5,2,8  합은 20 첫구간의 합은 반드시 구해야 한다.
# 4,5,2,8,3  합은 19 + 3 = 22
# 5,2,8,3,7  합은 18 + 7 = 25
# 합한 결과에서 1을 빼고, 다음 구간에서의 마지막 값을 더하면 우리가 원하는 구간합을 구할 수 있다.
# 이를 통해 중복된 연산을 막을 수 있다..


# 코드 구현해보기.
for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]  # 숫자의 개수
    M = info[1]  # 구간

    numbers = list(map(int, input().split()))

    tmp = 0
    for i in range(M):
        tmp += numbers[i]

    max_value = tmp
    min_value = tmp

    for i in range(M,N):
        # 새로운 구간의 합을 아주아주 간단하게 구할 수 있다.
        tmp = tmp + numbers[i] - numbers[i - M]

