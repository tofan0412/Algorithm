# SILVER3
def binary_search(arr, max_h, min_h, M):
    global result
    sum_of_tree = 0
    if max_h < min_h: # 같은 경우에도 높이 4로 컷할 수 있으므로 같은 경우는 포함되어선 안된다.
        return

    mid = (max_h + min_h) // 2

    for i in range(len(arr)):
        if arr[i] - mid >= 0:
            sum_of_tree += arr[i] - mid

    if sum_of_tree >= M:
        result = mid

    # 목적 : 최대 H를 구하는 것이다.
    # 만약 자른 나무 길이의 합이 M보다 작다면? H를 낮춰야 한다.
    if sum_of_tree < M:
        # 이 때 H를 이진 탐색으로 하자.
        return binary_search(arr, mid-1, min_h, M)
    # 만약 자른 나무 길이의 합이 M보다 많거나 같다면? H를 높여야 한다.
    elif sum_of_tree >= M:
        return binary_search(arr, max_h, mid+1, M)


N, M = map(int, input().split())
height = list(map(int, input().split()))

result = 0
binary_search(height, max(height), 0, M)
print(result)
