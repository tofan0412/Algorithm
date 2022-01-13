# GOLD5
def binary_search(arr, start, end):
    global setup, C, max_dis
    if start >= end or len(setup) == C:
        return

    mid = (start + end) // 2

    # 만약 중간 좌표에 집이 있다면
    if mid in arr:
        # 1. 공유기 간 최대 거리를 Keep
        max_dis = min(mid - start, end - mid)
        setup.append(mid)
    # 중간 좌표에 집이 없다면? 중간 좌표에서 가장 가까운 점을 찾아 공유기 설치.
    else:
        left, right = mid, mid
        while left not in arr:
            left -= 1
        while right not in arr:
            right += 1
        # 만약 mid 기준 왼쪽에 위치한 집에 공유기를 설치했을 때 인접 공유기간 거리가 더 멀다면
        if (left - start) > (end - right):
            mid = left
            max_dis = left - start
            setup.append(left)
        else:
            mid = right
            max_dis = end - right
            setup.append(right)
    # 공유기 설치할 집을 다시 찾아본다.
    binary_search(arr, start, mid-1)
    binary_search(arr, mid+1, end)


N, C = map(int, input().split())
coord = [] # 집이 위치한 좌표 배열
setup = [] # 공유기를 설치한 집의 배열
for _ in range(N):
    coord.append(int(input()))

# 전제 조건. 이진탐색이므로 coord는 반드시 정렬되어야 한다.
coord = sorted(coord)

# 최초의 두 공유기 사이의 최대 인접 거리
max_dis = coord[-1] - coord[0]

setup.append(coord[0])
setup.append(coord[-1])
# 모든 공유기를 설치할 때까지 이진 탐색을 실시한다. 마지막은 현재 설치한 공유기의 개수를 의미한다.
binary_search(coord, coord[0], coord[-1])
print(max_dis)

