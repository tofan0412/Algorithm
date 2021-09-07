T = int(input())
for tc in range(1, T+1):
    binary = list(input())
    tmp_binary = list(binary)
    triple = list(input())
    tmp_triple = list(triple)

    binary_possible = []
    triple_possible = []
    for i in range(len(binary)): # i는 틀린 자리
        if binary[i] == '0':
            tmp_binary[i] = '1'
        else:
            tmp_binary[i] = '0'
        result = ''
        for j in range(len(binary)):
            result += tmp_binary[j]

        binary_possible.append(result)
        # 원복해야 함.
        tmp_binary = list(binary)

    for i in range(len(triple)):
        if triple[i] == '0':
            # 2가지로 나뉜다.
            for j in ['1', '2']:
                tmp_triple[i] = j
                result = ''
                for k in range(len(triple)):
                    result += tmp_triple[k]
                triple_possible.append(result)
        elif triple[i] == '1':
            for j in ['0', '2']:
                tmp_triple[i] = j
                result = ''
                for k in range(len(triple)):
                    result += tmp_triple[k]
                triple_possible.append(result)
        else: # 2인 경우
            for j in ['0', '1']:
                tmp_triple[i] = j
                result = ''
                for k in range(len(triple)):
                    result += tmp_triple[k]
                triple_possible.append(result)
        tmp_triple = list(triple)

    # print(binary_possible)
    # print(triple_possible)
    # 매칭.
    for bin in binary_possible:
        for tri in triple_possible:
            if int(bin, 2) == int(tri, 3):
                # print(bin)
                # print(tri)
                print(f'#{tc} {int(bin, 2)}')

# 스마트하게 변경해보자..
