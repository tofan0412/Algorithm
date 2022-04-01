import sys


def binary_search(arr, start, end, target):
    if start >= end:
        return start

    mid = (start + end) // 2

    if arr[mid] <= target:
        binary_search(arr, mid + 1, end, target)
    else:
        binary_search(arr, start, mid, target)


width, height = map(int, sys.stdin.readline().rstrip().split())
obstacles = []
up = [] # 종유석
down = [] # 석순
for i in range(width):
    if i % 2 == 0:
        down.append(int(sys.stdin.readline().rstrip()))
    else:
        up.append(height - int(sys.stdin.readline().rstrip())) # 특정 높이 h에 대해 이 값보다 크다면 무조건 충돌한다.

# 이진 탐색의 기본 전제 조건은 정렬된 상태이다.
# 기존 코드의 문제점 : h에 대해 그냥 완탐을 해버림.. h는 특정 기준값이 없어 절반만 선택하기 애매하다.

up.sort()
down.sort()

min_val = 0
result = 0

# h에 대해선 그냥 linear하게 간다.
for h in range(1, height+1):
    # 1. 종유석에 대해 높이가 h일 때 카운트 해보자. h는 0, 1, 2, ... height이다.
    cnt1 = binary_search(down, 0, len(down), h)
    cnt2 = binary_search(up, 0, len(up), h-1)




