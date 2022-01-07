def binary_search(arr, target, start, end):
    if start >= end:
        return None
    mid = (start + end) // 2

    if arr[mid] == target:
        return min
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)