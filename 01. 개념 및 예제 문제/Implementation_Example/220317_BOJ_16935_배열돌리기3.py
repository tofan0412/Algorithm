import pprint
from copy import deepcopy
# SILVER1
def reverse_vertical(b):
    a = deepcopy(b)
    n = len(b)
    m = len(b[0])
    for row in range(n // 2):
        for col in range(m):
            a[row][col], a[n-1-row][col] = a[n-1-row][col], a[row][col]
    return a


def reverse_horizon(b):
    a = deepcopy(b)
    n = len(b)
    m = len(b[0])
    for col in range(m // 2):
        for row in range(n):
            a[row][col], a[row][m-1-col] = a[row][m-1-col], a[row][col]
    return a


def rotate_right(a):
    result = []
    n = len(a)
    m = len(a[0])
    for col in range(m):
        line = []
        # 한 col의 마지막 원소부터 읽으면서, 추가한다.
        for row in range(n-1, -1, -1): # 인덱스이므로, n-1부터 시작해야 한다.
            line.append(a[row][col])
        # 끝나면 result에 추가한다.
        result.append(line)
    return result


def rotate_left(a):
    result = []
    n = len(a)
    m = len(a[0])
    for col in range(m-1, -1, -1):
        line = []
        for row in range(n):
            line.append(a[row][col])
        result.append(line)
    return result


# 사분면을 시계방향으로 회전
def rotate_quadrant_right(b):
    points = read_quadrant(b)
    total = []
    n = len(b)
    m = len(b[0])

    for p in points:
        std_r = p[0]
        std_c = p[1]
        tmp = []
        for row in range(n // 2):
            line = []
            for col in range(m // 2):
                line.append(b[std_r + row][std_c + col])
            tmp.append(line)
        total.append(tmp)
    tmp = list()
    tmp.append(total[2])
    tmp.append(total[0])
    tmp.append(total[3])
    tmp.append(total[1])

    result = list()
    for i in range(n // 2):
        # 4 사분면과 1 사분면을 합치고
        line1 = tmp[0][i] + tmp[1][i]
        result.append(line1)
    for i in range(n // 2):
        line1 = tmp[2][i] + tmp[3][i]
        result.append(line1)
    return result


# 사분면을 반시계방향으로 회전
def rotate_quadrant_left(b):
    points = read_quadrant(b)
    total = []
    n = len(b)
    m = len(b[0])

    for p in points:
        std_r = p[0]
        std_c = p[1]
        tmp = []
        for row in range(n // 2):
            line = []
            for col in range(m // 2):
                line.append(b[std_r + row][std_c + col])
            tmp.append(line)
        total.append(tmp)
    tmp = list()
    tmp.append(total[1])
    tmp.append(total[3])
    tmp.append(total[0])
    tmp.append(total[2])

    result = list()
    for i in range(n // 2):
        # 4 사분면과 1 사분면을 합치고
        line1 = tmp[0][i] + tmp[1][i]
        result.append(line1)
    for i in range(n // 2):
        line1 = tmp[2][i] + tmp[3][i]
        result.append(line1)
    return result

# 배열을 사분면으로 구별하여 읽는 함수
def read_quadrant(b):
    n = len(b)
    m = len(b[0])
    p1 = (0, 0)
    p2 = (0, m // 2)
    p3 = (n // 2, 0)
    p4 = (n // 2, m // 2)

    return p1, p2, p3, p4


N, M, cnt = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
kind = list(input().split()) # num에 따른 각각의 연산

for k in kind:
    if k == '1':
        arr = reverse_vertical(arr)
    if k == '2':
        arr = reverse_horizon(arr)
    if k == '3':
        arr = rotate_right(arr)
    if k == '4':
        arr = rotate_left(arr)
    if k == '5':
        arr = rotate_quadrant_right(arr)
    if k == '6':
        arr = rotate_quadrant_left(arr)

for row in range(len(arr)):
    for col in range(len(arr[0])):
        print(str(arr[row][col]) + " ", end="")
    print()

# 테스트 코드
# print("원래 배열은")
# pprint.pprint(arr)
# print("상하반전")
# pprint.pprint(reverse_vertical(arr))
# print("좌우반전")
# pprint.pprint(reverse_horizon(arr))
# print("오른쪽으로 90도 회전")
# pprint.pp(rotate_right(arr))
# print("왼쪽으로 90도 회전")
# pprint.pp(rotate_left(arr))
# print("각 사분면의 기준점은")
# print(read_quadrant(arr))
# print("사분면 오른쪽 회전 결과")
# pprint.pprint(rotate_quadrant_right(arr))
# print("사분면 왼쪽 회전 결과")
# pprint.pprint(rotate_quadrant_left(arr))


