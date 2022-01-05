import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    i = 0
    j = 0

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


N = int(input())
array = []

for index in range(N):
    array.append(int(input()))

result = merge_sort(array)

for num in result:
    print(num)