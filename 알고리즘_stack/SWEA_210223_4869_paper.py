# 종이의 종류 : 1. 10x20 , 20x20
# 교실 바닥의 크기 : 20xN
# 10의 배수인 N이 주어졌을 때, 종이를 붙이는 모든 경우를 찾으려면 테이프로 만듬 표시한 영역을 몇개나 만들어야
# 되는지 계산하는프로그램을 만드시오.

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    result = 0
    if N // 10 % 2 == 0: # 앞자리가 짝수이면
        n = (N // 10)//2
        tmp = 2 ** (2*n) - 1
        result = 2 * tmp / 3 + 1
    else:
        n = (N // 10)//2 + 1
        tmp = 2 ** (2 * n) - 1
        result = tmp / 3

    print(f'#{tc} {round(result)}')
