case = int(input())
for tc in range(1, case+1):
    # Bubble 정렬을 이용하여 오름차순으로 정렬해보자.
    length = int(input())
    num_list = list(map(int, input().split()))
    for i in range(0, length):
        for j in range(0, len(num_list)-1): # 마지막 원소는 검사할 필요가 없다.
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    result = ''
    for num in num_list:
        result += str(num) + ' '

    print(f'#{tc} {result}')