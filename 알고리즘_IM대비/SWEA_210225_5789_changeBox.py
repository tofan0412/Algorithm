# 현주의 상자 바꾸기
T = int(input())

for tc in range(1, T+1):
    N, Q = list(map(int, input().split()))
    arr = ['0']*N

    # Q번 작업을 진행하면서
    for i in range(1,Q+1):
        L, R = list(map(int, input().split()))
        # 첫번째가 0번째이므로
        L -= 1
        for j in range(L, R):
            arr[j] = str(i)
    print(f'#{tc} {" ".join(arr)}')
