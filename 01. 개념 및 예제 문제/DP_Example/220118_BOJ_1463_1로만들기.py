# SILVER3
import sys
sys.setrecursionlimit(250000)


def solution(N):
    if N == 1 or N == 2:
        return memo[N]

    if memo[N] != 10000005:
        return memo[N]

    if not N % 3:
        # 다음은 min()을 사용하여 코드를 간결화한 것이다.
        # 다만 이 코드의 경우, RecursionError가 발생한다.
        memo[N] = min(memo[N], solution(N // 3) + 1)
    if not N % 2:
        memo[N] = min(memo[N], solution(N // 2) + 1)
    if N:
        memo[N] = min(memo[N], solution(N - 1) + 1)
    return memo[N]


N = int(input())
memo = [10000005] * 1000001
memo[1], memo[2] = 0, 1
solution(N)
print(memo[N])
