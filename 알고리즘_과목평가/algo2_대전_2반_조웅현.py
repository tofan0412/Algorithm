# 문제2. 보드게임

# 테스트 케이스의 수 T를 입력받는다.
T = int(input())

for tc in range(1,T+1): # 테스트 케이스의 개수만큼 반복문을 수행한다.
    # 가장 먼저, 첫번째로 주사위를 굴리는 사람이 누구인지 주어진다.
    game_starter = input() # 먼저 시작할 사람을 입력받는다.
    game_later = '' # 나중에 시작할 사람을 저장할 변수를 선언한다.

    if game_starter == 'A': # 만약 먼저 시작하는 사람이 A라면, 나중에 시작하는 사람은 B가 되고
        game_later = 'B'
    else: # 먼저 시작하는 사람이 B라면, 나중에 시작하는 사람은 A가 된다.
        game_later = 'A'

    # 누가 주사위를 먼저 던지느냐에 따라, 입력받는 순서를 바꾼다..
    if game_starter == 'A': # A가 먼저 주사위 눈금을 던지는 경우
        first_case = list(map(int,input().split())) # A의 주사위 수
        last_case = list(map(int, input().split())) # B의 주사위 수
    else: # B가 먼저 주사위 눈금을 던지는 경우
        last_case = list(map(int, input().split())) # A의 주사위 수
        first_case = list(map(int, input().split())) # B의 주사위 수

    game_board_first = ['0']*20 # 선발주자의 게임보드판 현황
    game_board_last = ['0']*20  # 후발주자의 게임보드판 현황
    # A,B 모두 0번째 인덱스에서 출발하므로 0번째 인덱스에 각각의 말을 표시해둔다.
    game_board_first[0] = game_starter
    game_board_last[0] = game_later

    winner = "AB" # 이기는 사람을 기록할 str을 변수로 저장한다. 둘 중 아무도 이기지 못한 경우 AB를 출력해야 하므로 기본값은
    # AB로 저장한다.
    for i in range(10): # A,B 모두 10번동안 주사위를 굴린다.
        # 시작은 선발주자부터!
        moveTo_f = game_board_first.index(game_starter) + first_case[i] # first_case는 i번째 주사위 눈금을 나타낸다.
        # movoTo_f는 선발주자가 주사위를 굴린 후 주사위 눈금만큼 이동할 위치를 나타낸다.
        # 이 때 a.index(b)는 a 리스트에서 b라는 요소의 인덱스값을 반환하는 내장함수이다.

        # 만약 moveTo가 보드의 총 길이보다 크거나 같다면? 승자가 된다.
        if moveTo_f >= 19:
            winner = game_starter
            # 여기서 끝내지 않으면 에러 발생. ( IndexError ) moveTo_f의 값이 보드의 최대 인덱스 값보다 커질 수 있다.
            break # 반복문을 종료한다.

        # 1. 이동할 위치에 이미 상대말이 존재한다면?
        if game_board_last[moveTo_f] != '0':
            # 잡힌 말은 보드의 처음 위치로 돌아간다. ( swap해준다! )
            game_board_last[0], game_board_last[moveTo_f] = game_board_last[moveTo_f], game_board_last[0]

        # 이후 주사위 눈금만큼 말의 위치를 이동한다. 마찬가지로 swap을 이용한다.
        # \의 경우 코드가 너무 길어지는 경우 다음 줄로 커서를 옮기기 위해 사용한다.
        game_board_first[game_board_first.index(game_starter)], game_board_first[moveTo_f] = \
            game_board_first[moveTo_f], game_board_first[game_board_first.index(game_starter)]

        # 이후 후발주자도 주사위 눈금만큼 이동한다.
        moveTo_l = game_board_last.index(game_later) + last_case[i]

        # 마찬가지로 보드 마지막 위치를 도착하거나 넘어서면 승자가 된다
        if moveTo_l >= 19:
            winner = game_later
            break

        # 이동할 위치에 이미 상대말이 존재한다면 잡은것이다! (swap을 통해 상대방의 말 위치를 0번째 인덱스로 옮긴다. )
        if game_board_first[moveTo_l] != '0':
            game_board_first[0], game_board_first[moveTo_l] = game_board_first[moveTo_l], game_board_first[0] # swap 통해 말을 처음 위치로 되돌리기

        # 주사위 눈금만큼 말을 이동시킨다. ( 현재 말의 위치와 moveTo_l 인덱스값의 위치를 swap 해준다. )
        game_board_last[game_board_last.index(game_later)], game_board_last[moveTo_l] = \
            game_board_last[moveTo_l], game_board_last[game_board_last.index(game_later)]

    # 테스트 케이스의 번호와 승자를 함께 출력한다.
    print(f'#{tc} {winner}')














