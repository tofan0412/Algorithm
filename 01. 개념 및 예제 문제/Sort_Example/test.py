def solution(N):
    enable_print = 0
    while N > 0:
        if enable_print == 0 and N % 10 != 0: # 출력 불가능한 상태인데, 현재 자리수가 출력가능한 수라면 출력 가능하게 한다.
            enable_print = 1
        if enable_print == 1: # 출력 가능한 상태이면, 출력한다.
            print(N % 10, end="")
        N = N // 10

N = int(input())
solution(N)

# 200과 같은 경우, 0이 출력되어선 안된다.
# 10010과 같은 경우, 끝의 0은 출력되면 안되지만 1과 1 사이의 0은 출력되어야 한다.