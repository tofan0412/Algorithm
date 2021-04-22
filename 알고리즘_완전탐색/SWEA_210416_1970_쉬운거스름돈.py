T = int(input())
for tc in range(1, T+1):
    price = int(input())
    unit = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0]*len(unit)
    for i in range(len(unit)):
        if price // unit[i] > 0:
            cnt[i] = price // unit[i]
            price = price - cnt[i] * unit[i]
        else:
            continue
    print(f'#{tc}')
    for i in range(len(cnt)):
        print(cnt[i], end=' ')
    print() # 커서 내리기


