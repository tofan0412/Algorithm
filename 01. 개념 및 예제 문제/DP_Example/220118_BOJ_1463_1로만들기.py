# SILVER3
def solution(N):
    if N == 1 or N == 2:
        return memo[N]

    if memo[N] != 10000005:
        return memo[N]

    if not N % 3:
        tmp = solution(N // 3) + 1
        if memo[N] > tmp:
            memo[N] = tmp
        # 만약 이미 기존의 최소값보다 더 큰 cnt가 나왔다면? 거기서 중지
        else:
            return memo[N]
    if not N % 2:
        tmp = solution(N // 2) + 1
        if memo[N] > tmp:
            memo[N] = tmp
        else:
            return memo[N]
    if N:
        tmp = solution(N - 1) + 1
        if memo[N] > tmp:
            memo[N] = tmp
        else:
            return memo[N]
    return memo[N]


N = int(input())
memo = [10000005] * 1000001
memo[1] = 0
memo[2] = 1
solution(N)
print(memo[N])
