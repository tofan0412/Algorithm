# 0에서 9까지 적힌 N장의 카드가 주어진다.
# counting sort를 이용한다.

tc_num = int(input())

for tc in range(1, tc_num + 1):
    number_cnt = [0]*10
    card_num = int(input()) # 카드의 개수를 의미한다.
    cards = input()

    # 카드 별로 개수 세기
    for card in cards:
        number_cnt[int(card)] += 1

    # 가장 많이 나온 카드 확인하기
    max = -1 # 카드 개수
    number = -1 # 카드에 적힌 숫자
    for i, cnt in enumerate(number_cnt):
        # 만약 카드의 개수가 같다면 ? 카드에 적힌 숫자를 기준으로 해야 한다.
        if max == cnt and i > number: # 카드의 수는 같은데 카드에 적힌 숫자가 더 크다면
            max = cnt
            number = i

        if max < cnt:
            max = cnt
            number = i

    print(f'#{tc} {number} {max}')