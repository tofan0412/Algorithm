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

# Answer

T = int(input())

for tc in range(1, T+1):
    # N : 카드의 개수
    N = int(input())

    card = input()

    # count 배열 생성
    count = [0] * 10

    max_count = -1
    max_num = -1

    for i in card:
        count[int(i)] += 1
        if max_count < count[int(i)]:
            max_count = count[int(i)] # 어떤 카드가 가장 많은 카드인지 알고 있다면..?

    # for i in range(len(count)):
    #     if max_count <= count[i]: # 등호가 왜 있지?? 뒤에서부터 세게 되면, 등호를 넣으면 안된다.
    #         max_num = i
    #         max_count = count[i]


    for i in range(len(count)-1, -1, -1):
        # 어떤 카드가 가장 많은지를 이미 알고 있는경우, 다른 경우는 해볼 필요도 없다.
        if max_count == count[i]:
            max_num = i
            break
