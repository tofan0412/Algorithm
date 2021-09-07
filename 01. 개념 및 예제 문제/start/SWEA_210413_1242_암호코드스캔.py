# 1. 정상적인 암호코드인지, 비정상적인 암호코드인지 구별해야 한다.
code_dict = {'3211': '0', '2221': '1', '2122': '2',
             '1411': '3', '1132': '4', '1231': '5',
             '1114': '6', '1312': '7', '1213': '8',
             '3112': '9'}

def checkCode(code):
    # 8자리 코드로 변환해야 한다.
    odd_number_sum = 0
    even_number_sum = 0

    # 이진 코드를 code_dic을 참고하여 변환하기
    # 배율 고려는 어떻게 해야 하는가?
    tmp = ''
    ratio = [0, 0, 0, 0]
    idx = len(code)-1 # 뒤에서부터 처리한다.
    order = 3
    tot_cnt = 0
    after_change = []
    while 0 <= idx:
        if order < 0:
            tmp = ''
            for i in range(len(ratio)):
                tmp += str(ratio[i])
            after_change.insert(0, tmp)
            order = 3
            ratio = [0, 0, 0, 0]

        if code[idx] == '1': # 가장 마지막은 항상 1로 시작한다.
            # 다른 애를 만날때까지 갯수를 센다.
            while code[idx] != '0':
                ratio[order] += 1
                tot_cnt += 1
                idx -= 1
            # 여기 왔다는건, 0을 만났다는 뜻이다.
            order -= 1
            while code[idx] != '1' and 0 <= idx: # 뒤에서 시작했을 때 반드시 0에서 끝나므로.
                tot_cnt += 1
                ratio[order] += 1
                idx -= 1
                if tot_cnt % 7 == 0:
                    break

            order -= 1
        else:
            idx -= 1
            continue
    # while문을 나왔다는 건, 모든 16진수를 2진수로 변환했다는 뜻이다.
    result = []
    for i in range(len(after_change)):
        result.append(int(code_dict[after_change[i]]))
    # print(result)

    for i in range(len(result)):
        if i % 2 == 0 and i != len(result)-1: # 홀수번째이다.
            odd_number_sum += result[i]
        elif i % 2 != 0 and i != len(result)-1: # 짝수이면서 마지막 수가 아닐 때..
            even_number_sum += result[i]
    final = odd_number_sum * 3 + even_number_sum + result[-1]
    if final % 10 == 0:
        return sum(result)
    else:
        return 0

    # for i in range(len(change_to_code)):
    #     if i % 2 == 0 and i != len(change_to_code)-1: # 홀수일때
    #         odd_number_sum += int(change_to_code[i])
    #     elif i % 2 % 2 != 0 and i != len(change_to_code)-1:
    #         even_number_sum += int(change_to_code[i])
    #
    # result = odd_number_sum * 3 + even_number_sum + int(change_to_code[-1])
    #
    # if result % 10 == 0:
    #     return odd_number_sum + even_number_sum + int(change_to_code[-1])
    # else:
    #     return 0


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N은 세로 크기, M은 가로크기
    arr = [list(input()) for _ in range(N)]
    code_list = []

    # 일단 16진수를 2진수로 먼저 변환하자.
    for row in range(N):
        tmp = ''
        for col in range(M):
            if arr[row][col] != '0': # 16진수를 만났다면
                tmp2 = ''
                # 16진수를 4자리 이진수로 먼저 변환해줘야 한다.
                val = int(arr[row][col], 16)
                for i in range(3, -1, -1):
                    if val & (1 << i): # 만약 1이라면
                        tmp2 += '1'
                    else:
                        tmp2 += '0'
                # print('tmp2는 {}'.format(tmp2))
                tmp += tmp2
        # print('------------------')
        # 한줄 검사가 끝난후..
        if len(tmp) > 0 and tmp not in code_list: # 16진수를 2진수로 변환한 대상을 리스트에 넣는다.
            code_list.append(tmp)

    # 이제 모든 코드에 대해서 유효한 코드인지 검증을 해야 한다.

    result = 0
    for code in code_list:
        result += checkCode(code)

    print(f'#{tc} {result}')



