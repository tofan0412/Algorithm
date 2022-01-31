# SILVER3
# nCm을 출력한다. -> n개 중 m개 뽑기

memo = [0] * 101
n, m = map(int, input().split())
# 공식을 풀기 -> 팩토리얼을 풀어야 한다.


def factorial(n, origin, multiple):
    if n == 1:
        memo[origin] = multiple
        return multiple

    elif memo[n] != 0:
        return multiple * memo[n]

    else:
        return factorial(n-1, origin, multiple * n)


result = factorial(n, n, 1) // (factorial(m, m, 1) * factorial(n-m, n-m, 1))
print(result)



