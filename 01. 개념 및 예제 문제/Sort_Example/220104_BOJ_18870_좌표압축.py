# SILVER2
def merge_sort(arr, arr2):
    if len(arr) <= 1:
        return arr, arr2

    mid = len(arr) // 2

    # arr, arr2를 모두 반환하므로 굳이 나눌 필요가 없다.
    returned_left = merge_sort(arr[:mid], arr2[:mid])
    returned_right = merge_sort(arr[mid:], arr2[mid:])

    left = returned_left[0]
    right = returned_right[0]
    left_index = returned_left[1]
    right_index = returned_right[1]

    i = 0
    j = 0
    merged = []
    merged_index = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            merged_index.append(left_index[i])
            i += 1
        else:
            merged.append(right[j])
            merged_index.append(right_index[j])
            j += 1

    if i == len(left):
        while j < len(right):
            merged.append(right[j])
            merged_index.append(right_index[j])
            j += 1
    if j == len(right):
        while i < len(left):
            merged.append(left[i])
            merged_index.append(left_index[i])
            i += 1

    return merged, merged_index


N = int(input())
array = list(map(int, input().split()))
origin_index = [i for i in range(len(array))]

# 병합 정렬로 정렬하자. 정렬할 때, origin_index 값도 맞춰서 함께 변경해줘야 한다.
result = merge_sort(array, origin_index)
compress_index = [-1]

index = 0 # iterable을 위한 인덱스
before_number = 1000000001
while len(compress_index) < len(result[0]) + 1:
    number = result[0][index]

    if before_number == number:
        compress_index.append(compress_index[-1])
    else:
        compress_index.append(compress_index[-1] + 1)
    before_number = number
    index += 1

# 이제 마지막으로, compress_index를 원래 순서대로 정렬해 준다.
compress_index = compress_index[1:] # 첫번째 -1은 빼준다.
answer = [0] * len(compress_index)

for (index, order) in enumerate(result[1]):
    answer[order] = compress_index[index]

answer_str = ''
for ans in answer:
    answer_str += str(ans) + ' '

print(answer_str)