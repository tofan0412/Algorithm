# BRONZE1
memo = [[-1, -1]] * 46
memo[0] = [1, 0]
memo[1] = [0, 1]


def solution(cnt):
    a = 3
    if cnt == 0:
        return memo[0] # [1, 0]을 반환한다.
    elif cnt == 1:
        return memo[1] # [0, 1]을 반환한다.

    if memo[cnt] == [-1, -1]:
        tmp1 = solution(cnt - 1)
        tmp2 = solution(cnt - 2)
        memo[cnt] = [tmp1[0] + tmp2[0], tmp1[1] + tmp2[1]]
    return memo[cnt]


K = int(input())
solution(K)
print(f'{memo[K][0]} {memo[K][1]}')
