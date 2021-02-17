t_num = int(input()) # 테스트할 횟수
for tc in range(1, t_num + 1):
    
    info = list(map(int, input().split()))
    length = info[0] # 정수 list의 길이를 의미한다.  
    interval = info[1] # 더할 구간의 크기를 의미한다. 
    
    # 정수 list를 입력받는다.
    numbers = list(map(int, input().split()))
    result = [] # 정수 list에서 나올 수 있는 모든 구간합을 저장할 list이다.
    # list의 크기가 5이고, interval의 크기가 3인 경우에는 3번만 구간합을 구하면 된다.
    # 3 = (list의 크기) - interval + 1
    for idx in range(0,length - interval + 1):
        # 각 구간합을 저장할 변수를 정의한다.
        interval_sum = 0
        for number in numbers[idx:interval+idx]: # a[0:2]와 같이 구간을 선택하면 index가 2인 element는 선택되지 않는다.
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
