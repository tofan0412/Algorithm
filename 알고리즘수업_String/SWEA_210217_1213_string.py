for tc in range(1, 11):
    tc_num = int(input())

    p = input()
    t = input()

    # while문을 이용하여 풀어보자.
    N = len(t)
    M = len(p)

    cnt = 0
    i = 0
    j = 0 # 포인터
    while j < M and i < N: # 단어가 여러개가 올 수 있으므로, j가 M이 될 때마다 초기화를 해줘야 한다.
        if t[i] != p[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        if j == M: # 만약 j가 keyword의 길이만큼 증가했다는건, 해당 단어를 찾았다는 뜻이다.
            cnt += 1
            j = 0 # j의 포인터를 다시 0으로 만들어준다.

    print(f'#{tc_num} {cnt}')
