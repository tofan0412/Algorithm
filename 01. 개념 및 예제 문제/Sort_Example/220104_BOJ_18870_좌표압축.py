# SILVER2
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
        if left[i][0] < right[j][0]:
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
tmp = list(map(int, input().split()))
array = [[v, i] for (i, v) in enumerate(tmp)]

result = merge_sort(array)

result[0].append(0) # 첫 항에 인덱스 기록해둔다.
for (i, v) in enumerate(result):
    # num은 [-10, 2] 와 같이 v와 원본 index를 포함하고 있는 객체이다.
    if i == 0:
        continue

    # 1. 이전 수와 같다면 인덱스 그대로
    if v[0] == result[i-1][0]:
        v.append(result[i-1][2])
    # 2. 이전 수와 다르다면 +1한 인덱스 추가
    else:
        v.append(result[i-1][2] + 1)

# 다시 원래 인덱스 기준으로 정렬하고, 좌표압축 기준 인덱스를 출력한다.
result = sorted(result, key=lambda x:x[1])
for arr in result:
    print(arr[2], end=' ')