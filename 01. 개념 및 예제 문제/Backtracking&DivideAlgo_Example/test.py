def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high) # 피봇을 결정한다.
        qsort(a, low, pivot-1) # 피봇을 기준으로 왼쪽에 대해 다시 퀵정렬
        qsort(a, pivot+1, high) # 피봇을 기준으로 오른쪽에 대해 다시 퀵정렬


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:
            i += 1
        while j > pivot and a[j] > a[pivot]:
            j -= 1
        if j <= i:
            break
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    a[pivot], a[j] = a[j], a[pivot]
    return j


a = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
print('정렬 전:\t', a)
qsort(a, 0, len(a)-1)
print('정렬 후:\t', a)