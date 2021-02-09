# 첫 줄에 테스트 케이스의 수 T가 주어진다.
# 각 케이스의 첫줄에 양수의 개수 N이 주어진다.
# 다음 줄에 N개의 양수 aj가 주어진다.
tc_num = int(input())
for tc in range(1,tc_num+1):
    num_length = int(input())
    numbers = list(map(int, input().split()))

    max = numbers[0]
    min = numbers[0]
    # 가장 큰 수와 작은 수 찾기
    for number in numbers:
        if max < number:
            max = number
        if min > number:
            min = number

    result = max - min
    print(f'#{tc} {result}')
