def solution(rsp3):  # rsp3의 최대 길이는 10만
    score = [0] * 3
    for race in rsp3:
        # 1. 모두 같은 경우
        if race[0] == race[1] == race[2]:
            continue
        # 2. 모두 다른 경우
        if race[0] != race[1] and race[1] != race[2] and race[0] != race[2]:
            continue

        # 이외의 경우는 2개는 같고, 하나만 다른 경우이다. => 6가지
        rsp = [0] * 3  # R, S, P
        for s in race:
            if s == 'R':
                rsp[0] += 1
            elif s == 'S':
                rsp[1] += 1
            else:
                rsp[2] += 1

        winner = ''
        # 승자는 바위
        if rsp == [2, 1, 0] or rsp == [1, 2, 0]:
            winner = 'R'
        # 승자는 보
        elif rsp == [2, 0, 1] or rsp == [1, 0, 2]:
            winner = 'P'
        # 승자는 가위
        elif rsp == [0, 2, 1] or rsp == [0, 1, 2]:
            winner = 'S'

        winner_idx = []
        for i in range(len(race)):
            if race[i] == winner:
                winner_idx.append(i)

        # 1명이 이긴 경우에는 2점
        if len(winner_idx) == 1:
            score[winner_idx[0]] += 2
        # 2명이 이긴 경우에는 누적 점수를 비교해야 한다.
        else:
            if score[winner_idx[0]] == score[winner_idx[1]]:
                score[winner_idx[0]] += 1
                score[winner_idx[1]] += 1
            else:
                # 현재 누적 점수가 다른 사람이 final_winner
                if score[winner_idx[0]] > score[winner_idx[1]]:
                    score[winner_idx[1]] += 2
                elif score[winner_idx[0]] < score[winner_idx[1]]:
                    score[winner_idx[0]] += 2
    return score


print(solution(["SSP", "PPS", "SSP", "RPP", "PRP"]))

