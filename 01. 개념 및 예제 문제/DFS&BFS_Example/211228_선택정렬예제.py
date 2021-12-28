# 다음의 정렬을 선택 정렬을 이용하여 오름차순으로 정렬하세요.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(0, len(arr)):
    # 탐색 영역 내에서 가장 작은 값의 인덱스 값을 저장해야 한다.
    # 최초에는 기준 자리의 값이 기준 최소값이 된다.
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print(arr)
