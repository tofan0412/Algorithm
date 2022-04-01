from collections import deque


def bfs(q, arr, v): # max (row, col)과 min (row, col)을 반환한다.
    INF = int(1e9)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    max_row = q[0][0]
    min_row = q[0][0]
    max_col = q[0][1]
    min_col = q[0][1]

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

                    if gr > max_row:
                        max_row = gr
                    elif gr < min_row:
                        min_row = gr

                    if gc > max_col:
                        max_col = gc
                    elif gc < min_col:
                        min_col = gc

    return max_row, max_col, min_row, min_col


def solution(arr):
    for i, case in enumerate(arr):
        print("현재 케이스는 " + str(i + 1))
        height = len(case)
        width = len(case[0])

        for row in range(height):
            for col in range(width):
                # 만약 흰색 타일인 경우 완탐 실시
                if case[row][col] == '.':
                    queue = deque()
                    queue.append((row, col))
                    visited = [[False] * width for _ in range(height)]
                    visited[row][col] = True

                    maxr, maxc, minr, minc = bfs(queue, case, visited) # min_info와 max_info를 반환하게 된다.
                    print("제일 위쪽 : " + str(minr), end=" ")
                    print("제일 아래쪽 : " + str(maxr), end=", ")
                    print("제일 왼쪽 : " + str(minc), end=" ")
                    print("제일 오른쪽 : " + str(maxc), end=" ")
                    print()


solution([[".....", ".XXX.", ".X.X.", ".XXX.", "....."],
          ["XXXXX", "XXXXX", "XXX.X", "XXX.X", "XXXXX"],
          ["XXXXX", "X...X", "X.X.X", "X...X", "XXXXX"],
          ["....X", ".....", "XXX..", "X.X..", "XXX.."],
          [".......", "XXX.XXX", "X.X.X.X", "XXX.XXX", "......."],
          ["XXXXX", "XX.XX", "X...X", "XX.XX", "XXXXX"]])


# solution([["XXXXX", "XXXXX", "XXX.X", "XXX.X", "XXXXX"]])

# solution([["XXXXX", "XX.XX", "X...X", "XX.XX", "XXXXX"]])
