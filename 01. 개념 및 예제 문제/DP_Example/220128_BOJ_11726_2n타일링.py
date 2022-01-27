# SILVER3
n = int(input())

memo = [0] * 1001
memo[1] = 1
memo[2] = 2

num = 3
while True:
    if num > n:
        break

    memo[num] = memo[num-1] + memo[num-2]
    num += 1

print(memo[n] % 10007)

