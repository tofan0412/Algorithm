tc_num = int(input())

for tc in range(1, tc_num+1):
    info = list(map(int, input().split()))
    N = info[0] # 박스의 개수
    Q = info[1] # 반복 횟수
    box_list = [0]*N

    for i in range(1,Q+1): # 지정한 Q번만큼 박스의 숫자를 새기는 동작 실행
        range_info = list(map(int, input().split()))
        left_limit = int(range_info[0])-1
        right_limit = int(range_info[1])-1

        for j in range(left_limit, right_limit+1):
            box_list[j] = i

    result = ''
    for num in box_list:
        result += str(num) + ' '
    print(f'#{tc} {result}')