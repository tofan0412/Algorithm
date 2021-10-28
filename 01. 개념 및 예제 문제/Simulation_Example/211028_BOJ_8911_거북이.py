def act(inc):
    global now, head, max_x, max_y, min_x, min_y
    if head == 'N':
        now[1] += inc
    elif head == 'S':
        now[1] -= inc
    elif head == 'W':
        now[0] -= inc
    else:
        now[0] += inc
    # 좌표 구하기
    if now[0] > max_x:
        max_x = now[0]
    if now[0] < min_x:
        min_x = now[0]
    if now[1] > max_y:
        max_y = now[1]
    if now[1] < min_y:
        min_y = now[1]

T = int(input())
for tc in range(T):
    control_program = list(map(str, input()))
    head = 'N'  # 'N' , 'S', 'W', 'E' 로 나뉜다.
    way = ['N', 'E', 'S', 'W']
    now = [0, 0]    # x, y
    max_x = 0
    min_x = 0
    max_y = 0
    min_y = 0
    for move in control_program:
        # F나 B인 경우 좌표 이동
        if move == 'F':
            inc = 1
            act(inc)
        elif move == 'B':
            inc = -1
            act(inc)
        # 방향을 돌리는 L, R인 경우
        # % 이용해서 4 이상인 경우 처리하자.
        elif move == 'L':
            if way.index(head) - 1 < 0:
                head = way[3]
            else:
                head = way[way.index(head) - 1]
        else:
            if way.index(head) + 1 > 3:
                head = way[0]
            else:
                head = way[way.index(head) + 1]

    print(abs(max_x - min_x) * abs(max_y - min_y))
