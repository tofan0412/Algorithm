from collections import deque


def bfs(q, arr, v): # max (row, col)과 min (row, col)을 반환한다.
    INF = int(1e9)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_info = [q[0][0], q[0][0]]
    min_info = [q[0][0], q[0][0]]

    while q:
        now = q.popleft()

        # 사방 탐색 실시
        for way in range(4):
            gr = now[0] + dr[way]
            gc = now[1] + dc[way]

            # IndexError 점검
            if 0 <= gr < len(arr) and 0 <= gc < len(arr[0]):
                if arr[gr][gc] == '.' and not v[gr][gc]:
                    q.append((gr, gc))
                    v[gr][gc] = True

                    # 1. min 정보 검사
                    if gr < min_info[0] and gc < min_info[1]:
                        min_info = [gr, gc]
                    # 2. max 정보 검사
                    elif max_info[0] < gr and max_info[1] < gc:
                        max_info = [gr, gc]
    return max_info, min_info


def solution(arr):
    for case in arr:
        height = len(case)
        width = len(case[0])

        for row in range(height):
            for col in range(width):
                # 만약 흰색 타일인 경우 완탐 실시
                if arr[row][col] == '.':
                    queue = deque()
                    queue.append((row, col))
                    visited = [[False] * width for _ in range(height)]
                    visited[row][col] = True

                    r1, r2 = bfs(queue, arr, visited) # min_info와 max_info를 반환하게 된다.


solution([[".....", ".XXX.", ".X.X.", ".XXX.", "....."],
          ["XXXXX", "XXXXX", "XXX.X", "XXX.X", "XXXXX"],
          ["XXXXX", "X...X", "X.X.X", "X...X", "XXXXX"],
          ["....X", ".....", "XXX..", "X.X..", "XXX.."],
          [".......", "XXX.XXX", "X.X.X.X", "XXX.XXX", "......."],
          ["XXXXX", "XX.XX", "X...X", "XX.XX", "XXXXX"]])
