from collections import deque
# GOLD5
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# 박스의 크기에 따라 r 값이 달라진다..! (중요)
# 각각의 박스에 대해 회전시켜보자.
def solution():
    global r
    width = n
    height = m

    for i in range(min(n, m) // 2): # 이 부분 때문에 틀렸다 !
        # 박스의 크기에 따라 r도 변화시켜야 한다.
        rotate((i, i), (n-1-i, m-1-i), arr, r % ((width - 1)*2 + (height - 1)*2))
        # 한번 회전이 끝나면 r도 수정해야 한다.
        width -= 2
        height -= 2


    for row in arr:
        print(*row)


def rotate(start, end, a, cnt):
    sr, sc = start[0], start[1]
    er, ec = end[0], end[1]

    line = deque()
    for col in range(sc, ec+1):
        line.append(arr[sr][col])
    for row in range(sr+1, er+1):
        line.append(arr[row][ec])
    for col in range(ec-1, sc-1, -1):
        line.append(arr[er][col])
    for row in range(er-1, sr, -1):
        line.append(arr[row][sc])

    # 회전 시작 GoGo. 어차피 최대 299이다.
    for _ in range(cnt):
        tmp = line.popleft()
        line.append(tmp)

    pointer = 0
    # 원래에 붙이자.
    for col in range(sc, ec+1):
        arr[sr][col] = line[pointer]
        pointer += 1
    for row in range(sr+1, er+1):
        arr[row][ec] = line[pointer]
        pointer += 1
    for col in range(ec-1, sc-1, -1):
        arr[er][col] = line[pointer]
        pointer += 1
    for row in range(er-1, sr, -1):
        arr[row][sc] = line[pointer]
        pointer += 1


solution()
