T = int(input())

for tc in range(1,21):
    tmp = input()
    tmp = tmp.replace("()","▼")

    case = list(tmp)

    cnt = 0
    j = 0

    while "(" in case:
        if case[j] == "(":
            # 바로 레이저가 오는 합판, 즉 최상단 합판부터 조각낸다.
            if case[j+1] == "▼":
                # 해당 합판이 몇개의 레이저를 거치는지 확인한다.
                k = 0
                cnt_raser = 0
                while case[j+1+k] != ')' and case[j+1+k] != "(":
                    cnt_raser += 1
                    k += 1

                if case[j+1+k] == ")":
                    del case[j+1+k]
                    cnt += cnt_raser + 1
                    del case[j]
                    j = 0

                if case[j + 1 + k] == "(":
                    cnt_raser = 0
                    j += 1
            else:
                j += 1
        else:
            j += 1
    print('#{} {}'.format(tc, cnt))

