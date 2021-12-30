# SILVER5
# 주의할 점 : N의 최대 수가 1,000,000이다
import random

def quick_sort(arr, start, end):
    # pivot = start
    pivot = random.randint(start, end)

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

# 1. 이전과 동일하게, 선택 정렬로 정렬해보자.
# 결과 : 시간 초과
# for i in range(N):
#     min_index = i
#     for j in range(i+1, N):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     arr[i], arr[min_index] = arr[min_index], arr[i]

# 2. 삽입 정렬도 테스트 해보자.
# 결과 : 시간 초과
# for i in range(1, len(arr)):
#     for j in range(i, 0, -1):
#         # 삽입 정렬의 특징 : i 인덱스부터 0번째 인덱스까지 오름차순으로 정렬되어 있다고 가정하기 때문에
#         # 왼쪽 또는 오른쪽 한 곳만 비교하면 된다.
#         if arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#         # 이미 오름차순으로 정렬되어 있는 경우이므로 (arr[j] > arr[j-1]) 다음으로 넘어간다.
#         else:
#             break

# 3. 퀵 정렬을 이용해보자.
quick_sort(arr, 0, len(arr) - 1)

# 문제점 : 퀵 소트의 피벗 값을 start로 하게 되면, 문제가 발생한다...

for number in arr:
    print(number)




