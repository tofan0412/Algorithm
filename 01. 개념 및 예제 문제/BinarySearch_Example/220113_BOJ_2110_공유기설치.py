import sys
# GOLD5
def binary_search(arr, start, end): # start는 첫번째 집의 좌표, end는 마지막 집의 좌표
    global result, C

    if start > end:
        return

    mid = (start + end) // 2 # 기준이 될 거리값이다.

    # 첫번째 집에 설치한다.
    visited = [False] * N
    visited[0] = True
    cnt = 1 # 공유기를 설치한 집의 개수
    last_i = 0 # 마지막으로 공유기를 설치한 집의 인덱스 번호
    # 1. target 거리 혹은 그 이상으로 모든 집을 배치할 수 있는가?
    for i in range(1, len(arr)):
        if cnt == C: # 더이상 설치할 수 없음.
            break
        # 1-1. 마지막으로 공유기를 설치한 집과의 거리 차이가 mid 이상이면 섫치한다.
        if arr[i] - arr[last_i] >= mid and not visited[i]:
            last_i = i
            cnt += 1
            visited[i] = True
    # 2. 이 과정 이후 False가 visited에 없다면? Target 거리 이상으로 공유기를 설치할 수 있다는 뜻이다.
    if cnt == C:
        # 해당 거리값을 기록해 둔다.
        if result < mid:
            result = mid
        binary_search(arr, mid+1, end)
    else:
        binary_search(arr, start, mid-1)


N, C = map(int, sys.stdin.readline().rstrip().split())
arr = sorted([int(sys.stdin.readline()) for _ in range(N)])

result = -int(1e9)
max_dist = arr[-1] - arr[0]
binary_search(arr, 1, max_dist)

print(result)



