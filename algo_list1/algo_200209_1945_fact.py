tc_num = int(input())
for tc in range(1, tc_num+1):
    N = int(input())
    # 2로 나눴을 때, 나오는 몫을 계속 2로 나눠야 한다. 언제까지 : 2로 나눠지지 않을때까지 ( 몫 % 2 != 0일 때까지.. )

    cnt_2,cnt_3,cnt_5,cnt_7,cnt_11 = 0,0,0,0,0

    # 가장 먼저 11로 나눈다.
    while N % 11 == 0:
        N = N // 11
        cnt_11 += 1

    while N % 7 == 0:
        N = N // 7
        cnt_7 += 1

    while N % 5 == 0:
        N = N // 5
        cnt_5 += 1

    while N % 3 == 0:
        N = N // 3
        cnt_3 += 1

    while N % 2 == 0:
        N = N // 2
        cnt_2 += 1

    print(f'#{tc} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')
