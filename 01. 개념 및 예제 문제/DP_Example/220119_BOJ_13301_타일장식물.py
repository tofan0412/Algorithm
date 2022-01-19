# BRONZE1

# 타일의 개수는 곧 n번째 피보나치 수를 의미한다.
memo = [-1] * 81
memo[1] = 4
memo[2] = 6


def solution(n):
    if n == 1 or n == 2:
        return memo[n]

    if memo[n] == -1:
        memo[n] = solution(n-1) + solution(n-2)
        return solution(n-1) + solution(n-2)
    else:
        return memo[n]


n = int(input())
solution(n)
print(memo[n])