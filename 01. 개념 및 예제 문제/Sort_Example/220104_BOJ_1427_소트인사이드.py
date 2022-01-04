# SILVER5
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # merge
    pointer1 = 0
    pointer2 = 0

    merged = []

    # 내림차순으로 정렬해야 한다.
    while pointer1 < len(left) and pointer2 < len(right):
        if left[pointer1] > right[pointer2]:
            merged.append(left[pointer1])
            pointer1 += 1
        else:
            merged.append(right[pointer2])
            pointer2 += 1

    if pointer1 == len(left):
        while pointer2 < len(right):
            merged.append(right[pointer2])
            pointer2 += 1
    if pointer2 == len(right):
        while pointer1 < len(left):
            merged.append(left[pointer1])
            pointer1 += 1
    return merged


N = str(input())
array = list(map(int, N))
array = merge_sort(array)
result = ''
for number in array:
    result += str(number)
print(result)