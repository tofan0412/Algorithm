# 정수 N, M이 주어질 때, M의 이진수 표현의 마지막 N비트가 모두 1로 켜져 있는지, 아닌지를 판별하여 출력하라.
T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # 먼저 M을 이진수로 표현해야 한다.
    idx = 0
    result = ''
    for i in range(N):
        if M & (1 << i):
            result += '1'
        else:
            result += '0'

    factor = 'ON'
    # 이 때, result는 뒤집어져 있다.
    for j in range(N):
        if result[j] == '0':
            factor = 'OFF'
            break

    print(f'#{tc} {factor}')

