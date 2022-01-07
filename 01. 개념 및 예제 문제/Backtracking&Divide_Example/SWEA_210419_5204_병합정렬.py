def divide(arr):
    if len(arr) == 1:
        return arr

    middle = len(arr) // 2
    left = divide(arr[:middle])
    right = divide(arr[middle:])
    return merge(left, right)


def merge(left, right):
    global cnt

    left_N, right_N = len(left), len(right)
    result = [0] * (left_N + right_N)
    left_i, right_i = 0, 0
    i = 0

    if left[-1] > right[-1]: # 오른쪽 끝과, 왼쪽 끝을 비교해서, 오른쪽 끝이 더 큰 경우를 비교한다.
        cnt += 1

    while left_i != left_N and right_i != right_N:
        if left[left_i] <= right[right_i]:
            result[i] += left[left_i]
            i += 1
            left_i += 1
        else:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    if left_i != left_N:
        while left_i != left_N:
            result[i] += left[left_i]
            i += 1
            left_i += 1

    if right_i != right_N:
        while right_i != right_N:
            result[i] += right[right_i]
            i += 1
            right_i += 1

    return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    # 1. 리스트이 원소가 1개가 될때까지 쪼갠다.
    divide(arr) # 분할
    print(f'#{tc} {cnt}')