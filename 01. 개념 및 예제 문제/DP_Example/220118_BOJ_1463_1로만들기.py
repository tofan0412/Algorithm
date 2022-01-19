# SILVER3
'''
1. 3로 나누어 떨어지면 3으로 나눈다.
2. 2로 나누어 떨어지면 2로 나눈다.
3. 1을 뺀다.

위와 같은 3가지 행동을 취할 수 있다. 위 연산 3개를 적절히 활용하여 N을 1로 만들려고 할때, (단 N의 범위는 1 ~ 30,000)
연산을 사용하는 회수의 최소값을 출력하시오.
'''
def solution(N):
    if N == 1 or N == 2:
        return memo[N]

    elif memo[N] == -1:
        if N % 3 == 0:
            memo[N] += solution(N // 5)
            return solution(N // 5)
        elif N % 2 == 0:
            memo[N] += solution(N // 3)
        else:
            memo[N] += solution(N - 1)
    else:
        return memo[N]


N = int(input())
memo = [-1] * 30001
memo[1] = 0
memo[2] = 1
solution(N)
print(memo[N])

