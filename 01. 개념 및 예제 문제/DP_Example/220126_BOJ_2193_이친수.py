# SILVER3

N = int(input())

memo = [0] * 91
memo[1], memo[2] = 1, 1

num = 3
while True:
    if memo[N] != 0:
        break

    memo[num] = memo[num-1] + memo[num-2]

    num += 1

print(memo[N])
