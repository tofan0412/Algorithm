# count 하는 배열을 만든다.
# 0점부터 100점까지 101의 길이를 갖는다.
n = int(input())
for tc in range(0, n):
    score_cnt = [0] * 101
    test_case_index = int(input()) # 테스트 케이스 번호를 의미한다.
    scores = list(map(int, input().split()))
    # 이 때 학생수가 1000명이므로, scores 역시 1000개이다.
    for score in scores:
        score_cnt[score] += 1

    # 최빈값을 찾는다.
    max_val = score_cnt[0]
    max_idx = 0
    for i, cnt in enumerate(score_cnt):
        if cnt > max_val:
            max_val = cnt
            max_idx = i

    # 최빈수가 여러 개 일때를 고려해야 한다...
    print(f'#{test_case_index} {score_cnt.index(max_val)}')