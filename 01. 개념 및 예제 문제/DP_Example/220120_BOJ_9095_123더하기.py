# SILVER3
# n은 11보다 작다.


T = int(input())
for tc in range(T):
    memo = [0] * 11
    memo[1] = 1
    memo[2] = 2
    memo[3] = 4

    N = int(input())
    num = 4
    while True:
        if num > N:
            break
        memo[num] = memo[num - 1] + memo[num - 2] + memo[num - 3]
        num += 1

    print(memo[N])
