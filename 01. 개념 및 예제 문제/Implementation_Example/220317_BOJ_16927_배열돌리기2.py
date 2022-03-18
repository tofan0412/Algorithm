from collections import deque
# GOLD5
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]

# 지정된 횟수만큼 수행해야 한다..
for cnt in range(r):
    for i in range(n // 2):
        # 좌측 대각선을 기준으로 2개의 기준점을 잡고 시작한다.
        sr, sc = (i, i)
        er, ec = n-1-i, m-1-i # 실제 인덱스. 단 끝 범위로 입력할 때는 +1을 해야 한다.

        line = deque()
        # 1. 최상단 row에 대해 진행
        for col in range(sc, ec+1):
            line.append(arr[sr][col])

        # 2. 우측 col에 대해 진행
        for row in range(sr+1, er+1):
            line.append(arr[row][ec])

        # 3. 최하단 row에 대해 진행
        for col in range(ec-1, sc-1, -1):
            line.append(arr[er][col])

        # 4. 좌측 col에 대해 진행
        for row in range(er-1, sr, -1):
            line.append(arr[row][sc])

        # line이 만들어졌으면 맨 앞의 걸 뒤로 뺀다.
        tmp = line.popleft()
        line.append(tmp)

        # result에 다시 붙인다.
        pointer = 0
        for col in range(sc, ec+1):
            result[sr][col] = line[pointer]
            pointer += 1

        for row in range(sr+1, er+1):
            result[row][ec] = line[pointer]
            pointer += 1

        for col in range(ec-1, sc-1, -1):
            result[er][col] = line[pointer]
            pointer += 1

        for row in range(er-1, sr, -1):
            result[row][sc] = line[pointer]
            pointer += 1

    # 모든 과정이 끝나면 arr을 result로 변환해야 한다.
    arr = result
# 마지막으로 출력만 잘 해주면 된다.
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()


