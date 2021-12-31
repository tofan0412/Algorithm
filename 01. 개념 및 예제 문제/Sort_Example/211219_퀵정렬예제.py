# 퀵 정렬을 이용하여 다음의 정렬을 오름차순으로 정렬하세요.
def quick_sort(arr, start, end):
    if start >= end: # 리스트의 크기는 1 이상이어야 한다.
        return
    # 1. 피벗을 설정한다. 피벗은 리스트의 첫번째 원소이다.
    pivot = start

    # 2. 리스트의 왼쪽 -> 오른쪽 방향으로는 피벗보다 큰 수를 찾고,
    # 리스트의 오른쪽 -> 왼쪽 방향으로는 피벗보다 작은 수를 찾는다.
    # left < right일 때까지 반복한다.
    # 최초의 left는 start이고, 최초의 right는 end이다.
    left = start + 1
    right = end

    while left <= right: # 피벗위 위치가 변경되었다는 뜻은 즉 left > right란 뜻이다.
        # 3. 왼쪽 -> 오른쪽 방향으로는 피벗보다 큰 수를 찾는다.
        while left <= end and arr[left] <= arr[pivot]: # 2번째 조건의 등호에 유의한다.
            left += 1
        # 4. 오른쪽 -> 왼쪽 방향으로는 피벗보다 작은 수를 찾는다.
        while right > start and arr[right] >= arr[pivot]: # 2번째 조건의 등호에 유의한다. # 처음에 첫번째 조건을 >=로 하니까 recursion Error 발생. Pivot은 대상에서 제외해야 한다.
            right -= 1

        # 이 위치에 왔으면, 해당하는 두 값의 index 값을 찾았다는 뜻이다.
        # 5. 찾은 두 값의 인덱스를 비교하여, 교차하고 있는지 유무를 판별한다.
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
        else:
            # 만약 left> right라면, 피벗보다 작은 수와 피벗의 위치를 서로 교환한다.
            arr[pivot], arr[right] = arr[right], arr[pivot]

    # 분할 이후, 피벗의 왼쪽 부분과 오른쪽 부분에 대해 각각 퀵 정렬 수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)
