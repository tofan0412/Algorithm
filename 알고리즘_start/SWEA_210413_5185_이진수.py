# A는 10, B는 11, C는 12, D는 13, E는 14, F는 15를 의미한다.
T = int(input())
for tc in range(1, T+1):
    N, str = input().split()
    N = int(N)
    result = ''

    for i in range(N):
        number = int(str[i], 16)

        for j in range(3, -1, -1): # 4자리 이진수로 바꿔줘야 한다.
            if number & (1 << j): # 0이 아니라면
                result += '1'
            else:
                result += '0'
    print(f'#{tc} {result}')


