# BRONZE1
# 여기서 n은 n번째 피보나치를 의미한다.
N = int(input())

memo = [-1] * 91
memo[0] = 0
memo[1] = 1
memo[2] = 1


def fibo(n):
    if n == 1 or n == 2:
        return memo[n]
    # 이미 값이 저장된 경우
    elif memo[n] != -1:
        return memo[n]
    # 값이 저장되지 않은 경우
    else:
        memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]


print(fibo(N))

