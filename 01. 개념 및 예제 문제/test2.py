from collections import deque

def solution(width, height, diagonals):
    for diagonal in diagonals:
        arr = [[0] * (width + 1) for _ in range(height + 1)]

        queue = deque()
        queue.append([height, 0])

        dr_go = [-1, 0]
        dc_go = [0, 1]
        dr_plus = [1, 0]
        dc_plus = [0, -1]

        while queue:
            now = queue.popleft()
            for way in range(2):
                goto_row = now[0] + dr_go[way]
                goto_col = now[1] + dc_go[way]

                if 0 <= goto_row <= height and 0 <= goto_col <= width:
                    arr[goto_row][goto_col] += 1
                    queue.append([goto_row, goto_col])
    print(arr)


solution(2, 2, [[1,1], [2,2]])


