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

for h in range(H, 0, -1):
    i = binary_search(height, h, 0, len(height) - 1)

    length = 0
    for j in range(i, len(height)):
        length += height[j] - h
    if length >= M:
        min_h = h
        # 반복문 중지. 최대의 H를 찾는 것이므로 밑 높이에 대해선 고려하지 않아도 된다.
        break
print(min_h)
