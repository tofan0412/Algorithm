# SILVER4
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 1. 먼저 divide
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 병합하면서 정렬하자.
    i, j = 0, 0
    merged = []
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


def binary_search(arr, target, start, end):
    if start > end:
        return 0

    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    else:
        return binary_search(arr, target, start, mid - 1)


N = int(input())
array = list(map(int, input().split())) # 정렬되어 있지 않다.
M = int(input())
array2 = list(map(int, input().split()))

# array2의 수가 array에 있는지 출력하면 된다.
# 1. 가장 먼저 array를 정렬하자.
# 병합 정렬을 이용하자.
array = merge_sort(array)
# 2. 이제 array2의 원소 하나 하나에 대해 이진탐색(or 이분탐색)을 통해 있는지 파악하자.
for num in array2:
    result = binary_search(array, num, 0, len(array) - 1)
    print(result)
