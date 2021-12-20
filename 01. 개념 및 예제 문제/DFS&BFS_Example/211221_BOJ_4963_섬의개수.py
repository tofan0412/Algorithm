# SILVER2
def solution(arr, point):
    global visited
    # 첫 element부터 팔방탐색을 실시한다. 순서는 상,하,좌,우, 1,2,3,4사분면
    dr = [-1, 1, 0, 0, -1, -1, 1, 1]
    dc = [0, 0, -1, 1, 1, -1, -1, 1]

    stack = []
    stack.append(point)
    visited[point[0]][point[1]] = 1

    while stack:
        now = stack.pop()
        # 팔방탐색 실시
        for way in range(8):
            nr = now[0] + dr[way]
            nc = now[1] + dc[way]

            if 0 <= nr < len(arr) and 0 <= nc < len(arr[nr]):
                # 땅이라면 스택에 넣는다.
                if arr[nr][nc] == '1' and visited[nr][nc] == 0:
                    stack.append([nr, nc])
                    visited[nr][nc] = 1
    return 1

result = []
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        for i in result:
            print(i)
        break
    else:
        arr = [[0]*w for _ in range(h)]
        visited = [[0] * w for _ in range(h)]
        count = 0 # 각 테스트 케이스에 대한 섬의 개수

        for i in range(h):
            arr[i] = input().split()

        for row in range(h):
            for col in range(w):
                if arr[row][col] == '1' and visited[row][col] == 0:
                    count += solution(arr, [row, col])

        result.append(count)