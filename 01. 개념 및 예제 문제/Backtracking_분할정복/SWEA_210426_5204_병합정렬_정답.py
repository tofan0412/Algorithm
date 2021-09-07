def mergeSort(s, e):
    global cnt
    if s >= e-1:
        return
    mid = (s + e) >> 1 # (s + e) // 2
    mergeSort(s, mid)   # 왼
    left = arr[mid-1]
    mergeSort(mid, e) # 오
    right = arr[e-1]
    if left > right:
        cnt += 1

    i, j, k = s, mid, s     # 임시변수 설정
    while i < mid and j < e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1; k += 1
        else:
            tmp[k] = arr[j]
            j += 1; k += 1
    # 한쪽이 다 정렬되면 나머지를 넣어줌
    while i < mid:
        tmp[k] = arr[i]
        i += 1; k += 1
    while j < e:
        tmp[k] = arr[j]
        j += 1; k += 1

    for i in range(s, e):
        arr[i] = tmp[i]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tmp = [0] * N
    cnt = 0

    mergeSort(0, N)
    print('#{} {} {}'.format(tc, arr[N//2], cnt))