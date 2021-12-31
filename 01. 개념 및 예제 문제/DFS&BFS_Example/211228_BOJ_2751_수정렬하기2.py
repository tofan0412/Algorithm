# SILVER5
# 주의할 점 : N의 최대 수가 1,000,000이다
def quick_sort(arr, start, end):
    pivot = (end - start) // 2

    # 종료 조건을 설정하자.
    if start >= end:
        return

    left = start + 1
    right = end
    while left <= right:
        # 왼쪽 -> 오른쪽으로는 피벗보다 큰 수를 찾자.
        while left <= right and arr[start] <= arr[pivot]:
            left += 1
        # 오른쪽 -> 왼쪽으로는 피벗보다 작은 수를 찾자.
        while right > start and arr[end] >= arr[pivot]:
            right -= 1

        # 이제 비교해보자.
        if left <= right:
            arr[right], arr[left] = arr[left], arr[right]
        else:
            arr[right], arr[pivot] = arr[pivot], arr[right]

    # 왼쪽, 오른쪽에 대해 각각 퀵 정렬 재수행
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


N = int(input())
arr = []
for i in range(N):
    number = int(input())
    arr.append(number)

# 3. 퀵 정렬을 이용해보자.
quick_sort(arr, 0, len(arr) - 1)

# 문제점 : 퀵 소트의 피벗 값을 start로 하게 되면, 문제가 발생한다...

for number in arr:
    print(number)