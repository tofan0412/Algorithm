T = int(input())

for tc in range(1,T+1):
    tmp = input()
    tmp = tmp.replace("()","▼")
    case = list(tmp)
    cnt = 0 # 잘라진 합판의 개수

    i = 0  # 포인터.
    while "(" in case:
        if i == len(case): # 포인터가 끝까지 이동했으므로, 다시 처음으로 돌려준다.
            i = 0
            continue

        if case[i] == "(":
            if case[i+1] == "▼": # 레이저인 경우에 카운트를 시작한다.
                j = i+1
                cnt_raser = 0
                while case[j] != ")":
                    cnt_raser += 1
                    j += 1
                # 여기로 내려왔다는 건, )를 만났다는 뜻이다.
                cnt += cnt_raser + 1
                del case[j] # 오른쪽 )를 삭제한다.
                del case[i] # 왼쪽 (를 삭제한다.
            else: # (를 만난 경우
                i += 1
        else: # ")"를 만났거나, 레이저를 바로 만난 경우
            i += 1

    print(f'#{tc} {cnt}')