# SILVER3
# N은 1 ~ 백만, M은 1에서 20억 사이이다.
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    if i == len(left):
        while j < len(right):
            merged.append(right[j])
            j += 1
    if j == len(right):
        while i < len(left):
            merged.append(left[i])
            i += 1
    return merged


def binary_search(arr, H, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if arr[mid] == H or arr[mid] > H:
        return mid
    elif arr[mid] < H:
        return binary_search(arr, H, mid + 1, end)
    elif arr[mid] > H:
        return binary_search(arr, H, start, mid - 1)


N, M = map(int, input().split())
height = list(map(int, input().split()))
height = merge_sort(height)

H = height[-1] - 1
min_h = 0

# 나무의 최대 개수는 최대 100만개이다.
# 임의의 절단 높이 H에 대해, 절단한 후 나무 길이의 총합을 구하는 시간 복잡도는 O(N^2)이다.
# 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
for h in range(H, -1, -1):
    i = binary_search(height, h, 0, len(height) - 1)

    length = 0
    for j in range(i, len(height)):
        length += height[j] - h
        # 더하면서 계산
        if length >= M:
            min_h = h
            print(h)
            break
    if min_h != 0:
        break
