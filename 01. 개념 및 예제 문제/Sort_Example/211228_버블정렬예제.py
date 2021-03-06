# 다음의 배열을 버블 정렬을 이용하여 오름차순으로 정렬하세요.
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 버블 정렬은 인접한 두 수를 비교하여 정렬하는 것이다.

# 첫번째 for문의 경우, N개의 원소가 있는 배열의 경우 비교는 N-1번만 하면 된다.
for i in range(0, len(arr)):
    # 두번째 for문의 경우, 배열의 마지막 인덱스가 최대값이므로 점차 영역을 좁혀가야 한다.
    # -1을 하는 이유는, 마지막 원소의 경우 오른쪽에 비교할 원소가 없기 때문에 제외해야 한다.
    for j in range(0, len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)
