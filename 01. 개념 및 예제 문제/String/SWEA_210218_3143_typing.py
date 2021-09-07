T = int(input())

for tc in range(1, T+1):
    A,B = list(input().split())

    # A에서 B가 몇개 있는지를 찾는다
    i = 0 # A의 포인터
    j = 0 # B의 포인터

    N = len(A)
    M = len(B)
    cnt = 0
    while j < M and i < N:
        if A[i] != B[j]:
            i = i - j
            j = -1
        i += 1
        j += 1

        if j == M:
            j = 0
            cnt += 1

    result = cnt + len(A) - cnt*len(B)
    print(f'#{tc} {result}')
