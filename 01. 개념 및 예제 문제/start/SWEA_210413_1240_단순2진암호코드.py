# 1. 정상적인 암호코드인지, 비정상적인 암호코드인지 구별해야 한다.
code_dict = {'0001101': '0', '0011001': '1', '0010011': '2',
             '0111101': '3', '0100011': '4', '0110001': '5',
             '0101111': '6', '0111011': '7', '0110111': '8',
             '0001011': '9'}

def checkCode(code):
    # 8자리 코드로 변환해야 한다.
    change_to_code = ''
    odd_number_sum = 0
    even_number_sum = 0

    tmp = ''
    for i in range(len(code)):
        tmp += code[i]
        if len(tmp) == 7:
            change_to_code += code_dict[tmp]
            tmp = ''
            continue

    for i in range(len(change_to_code)):
        if i % 2 == 0 and i != len(change_to_code)-1: # 홀수일때
            odd_number_sum += int(change_to_code[i])
        elif i % 2 % 2 != 0 and i != len(change_to_code)-1:
            even_number_sum += int(change_to_code[i])

    result = odd_number_sum * 3 + even_number_sum + int(change_to_code[-1])

    if result % 10 == 0:
        return odd_number_sum + even_number_sum + int(change_to_code[-1])
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(input()) for _ in range(N)]
    result = 0

    # 뒤에서부터 찾는다.
    for row in range(N):
        tmp = ''
        for col in range(M-1, -1, -1):
            if arr[row][col] == '1': # 모든 암호문은 가장 마지막 부분이 1로 끝난다.
                tmp = arr[row][col-55:col+1]
                result = checkCode(tmp)
                break # 다음 줄로 넘어간다.

    print(f'#{tc} {result}')

