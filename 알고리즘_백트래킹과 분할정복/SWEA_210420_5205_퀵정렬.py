def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot-1)
        qsort(a, pivot+1, high) # pivot으로 하면 low < high가 되서 안 끝난다.


def partition(arr, pivot, right):
    # 최초의 pivot 위치는 0번째 인덱스이다.
    i = pivot + 1
    j = right
    while True:
        # 피봇을 제외한 첫번째에서부터 피봇보다 작은 값을 찾는다.
        while i < right and arr[i] < arr[pivot]:
            i += 1
        # 피봇을 제외한 오른쪽에서부터 왼쪽으로 피봇보다 큰 값을 찾는다.
        while j > pivot and arr[j] > arr[pivot]:
            j -= 1
        # i와 j의 위치 결정이 끝난 시점이다.
        # 만약 j가 i보다 앞에 있다면 while을 종료한다.
        if j <= i:
            break
        # 그렇지 않다면, i와 j의 위치를 서로 변경하고 다시 while문을 반복한다.
        arr[i], arr[j] = arr[j], arr[i]
        # 위에서 Swap 했으므로 i, j를 모두 변경한다.
        i += 1
        j -= 1
    # j와 i의 위치가 교차되어 있는 경우
    # i의 왼쪽은 모두 피봇보다 큰 값이고, j는 피봇보다 큰 값을 기준으로 이동한다.
    # 따라서 i는 피봇보다 큰 값이고. j는 피봇보다 작은 값이므로 경계지점이다.
    arr[pivot], arr[j] = arr[j], arr[pivot]
    return j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    qsort(arr, 0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')