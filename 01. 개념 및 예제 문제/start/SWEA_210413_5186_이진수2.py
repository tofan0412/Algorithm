from decimal import Decimal

T = int(input())
for tc in range(1, T+1):
    # 0 ~ 1 사이의 십집수 N을 이진수로 바꾸기..
    N = float(input())

    # 소수점 자리 구하기
    num_len = 0
    tmp_len = N
    while True:
        tmp_len = Decimal(str(tmp_len)) * 10
        num_len += 1
        if tmp_len % 1 == 0: # 더이상 남는 소수점이 없다는 뜻이다.
            break
        else:
            tmp_len = tmp_len % 1

    result = ''
    # 주어진 수소를 2를 곱하여, 정수부분을 취한다.
    # 소수 부분이 0일때까지 계속해야 한다.
    while True:
        if N == 0:
            break
        if len(result) >= 13:
            result = 'overflow'
            break

        tmp = N * 2
        if int(tmp) == 1:
            result += '1'
            N = tmp - 1
        else:
            result += '0'
            N = tmp

    print(f'#{tc} {result}')
