def select(idx, sum_val):
    global choosed, result
    a = 0
    if idx == N: # 모든 원소를 다 선택했다는 뜻이다.
        result.append(sum_val)
        return
    else:
        # 선택해야 한다.
        for col_num in range(N):    # i는 0에서부터 N-1까지 가능하다.
            # 이전에 이미 선택했다면 선택할 수 없다.
            if col_num not in choosed:
                # 이 열을 선택했을 때의 합계가 result에 존재하는 값보다 커지면 더이상 할 필요가 없다.
                sum_after = sum_val + tables[idx][col_num]
                if sum_after <= result[-1]:
                    choosed.add(col_num)
                    choice[idx] = col_num  # i번째 인덱스는 i를 선택했다는 뜻이다.
                    select(idx+1, sum_after)
                    choice[idx] = 0
                    choosed.remove(col_num)
                # result의 마지막보다 큰 경우에는 종료
                else:
                    continue
            # 이미 선택한 열이라면 다음 열로 넘어간다.
            else:
                continue


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tables = [list(map(int, input().split())) for _ in range(N)]

    # 최소 생산 비용을 구하자.
    choice = [0] * N # N개의 제품이 있으면 N개의 공장이 존재한다.
    choosed = set() # 0부터 N-1까지 와야 한다. 최종적으로 길이는 N이 되어야 한다.
    result = [10000000]

    select(0, 0)
    print(f'#{tc} {min(result)}')