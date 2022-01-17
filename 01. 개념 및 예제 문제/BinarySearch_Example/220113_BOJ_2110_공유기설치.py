# GOLD5
# 참고 코드 : https://hongcoding.tistory.com/3
def binary_search(arr, start, end):
    global C, setup, min_dis

    if start >= end or len(setup) == C:
        return

    mid = (start + end) // 2

    # 만약 중간에 설치할 수 있다면 설치
    if mid in coord and mid not in setup:
        setup.append(mid)
        binary_search(arr, arr[0], mid)
    # 만약 설치할 수 없다면 : mid보다 더 먼 집에 설치할 수 있는지를 따져야 한다.
    else:
        # 1. mid보다 더 먼 집에 설치할 수 있는 경우
        if arr[-1] > mid:
            binary_search(arr, mid, end)
        # 2. mid보다 더 먼 집에 설치할 수 없는 경우
        else:
            binary_search(arr, start, mid - 1)


# N은 집의 개수, C는 공유기의 개수
N, C = map(int, input().split())
coord = [] # 집이 위치한 좌표 배열
setup = [] # 공유기를 설치한 집의 배열
for _ in range(N):
    coord.append(int(input()))

# 전제 조건. 이진탐색이므로 coord는 반드시 정렬되어야 한다.
coord = sorted(coord)
min_dis = 0

setup.append(coord[0])
binary_search(coord, coord[0], coord[-1])
print(setup)

# 최대 거리값을 찾자.
