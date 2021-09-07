# Brute Force를 이용하자
T = int(input())

for tc in range(1, T+1):
    p = input()
    t = input()

    N = len(t)
    M = len(p)

    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

    if j == M: print(f'#{tc} 1')
    else: print(f'#{tc} 0')
