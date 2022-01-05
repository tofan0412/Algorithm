# SILVER2
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    pointer1 = 0
    pointer2 = 0
    merged = []

    while pointer1 < len(left) and pointer2 < len(right):
        if left[pointer1] < right[pointer2]:


N = int(input())
array = list(map(int, input().split()))
indexes = []
# 병합 정렬로 정렬하자.

