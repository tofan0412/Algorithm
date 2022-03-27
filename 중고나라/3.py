def binary_search(arr, value, start, end):
    # 아래의 경우는 배열의 길이가 짝수일 때 가능한 경우이다. 홀수인 경우 start == end일수도 있다.
    if start == end:
        return start + 1
    elif start > end:
        return end

    mid = (start + end) // 2

    # arr[mid]값이 value보다 작거나 같다면? 오른쪽 범위에 대해 찾는다.
    if arr[mid] <= value:
        return binary_search(arr, value, mid + 1, end)

    # arr[mid]값이 value보다 크거나 같다면? 왼쪽 범위에 대해 찾아야 한다.
    elif arr[mid] > value:
        return binary_search(arr, value, start, mid - 1)


def merge_sort(arr, start, end):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid], start, mid - 1)
    right = merge_sort(arr[mid:], mid, end)

    # 합치자.
    pointer1 = 0
    pointer2 = 0
    merged = []

    while pointer1 != len(left) and pointer2 != len(right):
        if left[pointer1] < right[pointer2]:
            merged.append(left[pointer1])
            pointer1 += 1
        else:
            merged.append(right[pointer2])
            pointer2 += 1

    if pointer1 == len(left):
        while pointer2 != len(right):
            merged.append(right[pointer2])
            pointer2 += 1
    elif pointer2 == len(right):
        while pointer1 != len(left):
            merged.append(left[pointer1])
            pointer1 += 1
    return merged


def solution(A, B):
    # B 데이터 정렬
    B = merge_sort(B, 0, len(B) - 1)  # 병합정렬 시간 복잡도 nlogn

    answer = 0

    for score in A:
        # 1. 해당 스코어보다 큰 점수가 있는가?
        if B[-1] <= score:
            B.pop(0)
            continue
        else:
            idx = binary_search(B, score, 0, len(B))
            B.pop(idx)
            answer += 1
    return answer


print(solution([5,1,3,7], [2,2,6,8]))
