# GOLD5
from collections import deque
from copy import deepcopy


def cnt_safe_area(maps):
    global n, m
    result = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                result += 1
    return result


def bfs(maps):
    # 여기서도 DeepCopy를 해줘야 한다.
    global n, m
    queue = deque()

    maps_tmp = deepcopy(maps)
    for i in range(n):
        for j in range(m):
            if maps_tmp[i][j] == 2:
                queue.append([i, j])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        virus_now = queue.popleft()

        for way in range(4):
            goto_row = virus_now[0] + dr[way]
            goto_col = virus_now[1] + dc[way]

            if 0 <= goto_row < n and 0 <= goto_col < m:
                if maps_tmp[goto_row][goto_col] == 0:
                    queue.append([goto_row, goto_col])
                    maps_tmp[goto_row][goto_col] = 2

    result = cnt_safe_area(maps_tmp)
    return result


def solution(now_r, now_c, cnt_wall, maps):
    global n, m, max_result

    if cnt_wall == 3:
        cnt_safe = bfs(maps)
        if max_result < cnt_safe:
            max_result = cnt_safe
        return

    if now_r == n:
        return

    next_row, next_col = 0, 0
    if now_c + 1 < m:
        next_col = now_c + 1
        next_row = now_r
    else:
        next_col = 0
        next_row = now_r + 1

    maps_copy = deepcopy(maps)
    # 1. 벽을 세울 수 있다면 세운다.
    if maps_copy[now_r][now_c] == 0:
        maps_copy[now_r][now_c] = 1
        solution(next_row, next_col, cnt_wall + 1, maps_copy)
        maps_copy[now_r][now_c] = 0
        solution(next_row, next_col, cnt_wall, maps_copy)
    # 현재 위치가 바이러스이거나, 벽인 경우에는 벽을 설치할 수 없다.
    else:
        solution(next_row, next_col, cnt_wall, maps_copy)


n, m = map(int, input().split()) # n은 3보다 크고, M은 8보다 작다.
lab = [list(map(int, input().split())) for _ in range(n)]

max_result = -12345
solution(0, 0, 0, lab)
print(max_result)
# 문제점 : 벽을 모두 세운 후, bfs()를 하는 과정에서 deepCopy를 하지 않아서 발생..