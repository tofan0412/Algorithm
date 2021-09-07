def count_best(now, idx, cnt):
    tmp = 0
    if idx == len(schedule)-1: # 마지막 스케줄까지 왔으므로, 다음 스케줄이 존재하지 않는다.
        result.append(cnt)
        return

    for i in range(idx, len(schedule)-1):
        if schedule[i+1][0] < now[1]: # 현재 작업의 종료시간보다 다음 작업의 시작시간이 빠르다면..
            continue
        else:
            cnt += 1
            idx = i+1
            now = schedule[idx]
            count_best(now, idx, cnt)
    # 여기까지 왔다는건, 더이상 적절한 대상이 없다는 뜻이다.
    result.append(cnt)
    return


T = int(input())
for tc in range(1, T+1):
    schedule = []
    N = int(input())
    for i in range(N):
        schedule.append(list(map(int, input().split())))

    # 종료 시간으로 정렬한다.
    # 선택 정렬
    for j in range(len(schedule)):
        min_endTime = schedule[j][1]
        min_idx = j
        for i in range(j+1, len(schedule)):
            if schedule[i][1] <= min_endTime:
                min_endTime = schedule[i][1]
                min_idx = i
        schedule[j], schedule[min_idx] = schedule[min_idx], schedule[j]


    now = (schedule[0])
    result = []
    count_best(now, 0, 1) # 현재 작업중인 시간대와 인덱스
    print(f'#{tc} {max(result)}')
