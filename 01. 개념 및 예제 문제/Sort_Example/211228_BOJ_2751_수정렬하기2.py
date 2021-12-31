# SILVER5
# 주의할 점 : N의 최대 수가 1,000,000이다
def merge_sort(array, start, end):
    if len(array) <= 1:
        return arr

    mid = len(array) // 2
    left = merge_sort(array[:mid], start, mid-1)
    right = merge_sort(array[mid:], mid, end)

    merged = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    if len(left) > 0:
        while len(left) > 0:
            merged.append(left.pop(0))
    if len(right) > 0:
        while len(right) > 0:
            merged.append(right.pop(0))
    return merged


N = int(input())
arr = []
for i in range(N):
    number = int(input())
    arr.append(number)

# 3. 병합 정렬을 이용해보자.
result = merge_sort(arr, 0, len(arr) - 1)

for number in result:
    print(number)


###############################
# 정답 코드는 다음과 같다.
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0 # i는 left의 pointer, j는 right의 pointer이다. k는 array의 인덱스이다.

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
    return array


# 데이터 입력
n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

num = merge_sort(num)

for i in num:
    print(i)