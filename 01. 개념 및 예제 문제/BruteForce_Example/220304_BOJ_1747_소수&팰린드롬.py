# SILVER1
# 숫자 n이 주어졌을 때, n보다 크거나 같고, 소수이면서 팰린드롬인 수 중에서 가장 작은 수를 구하시오
import math

n = int(input())
result = -321

while True:
    if n == 1:
        n += 1
        continue

    if result != -321:
        break

    # 1. 먼저 팰린드롬인지 판별하자.
    n_str = list(str(n))
    mid = len(n_str) // 2

    is_palindrome = True
    for i in range(mid):
        if n_str[i] != n_str[-(1 + i)]:
            is_palindrome = False

    if not is_palindrome:
        n += 1
        continue
    elif is_palindrome:
        # 2. 팰린드롬이면 소수인지 판별하자.
        is_prime = True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            result = n
    n += 1
    continue

print(result)
