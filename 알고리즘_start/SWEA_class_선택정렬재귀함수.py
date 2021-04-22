def selectionSort(idx, k): # k는 최소값을 위치할 기준 인덱스이다.
    global min_num, min_idx
    if idx == N:
        arr[k], arr[min_idx] = arr[min_idx], arr[k]
        return
    if k == N-1:
        return

    if arr[idx] <= min_num:
        min_num = arr[idx]
        min_idx = idx
    selectionSort(idx+1, k)
    # 다음 자리에 대해서 수행한다. 이 때 k가 N이 되면 안해도 된다.
    min_num = arr[k+1]
    min_idx = 0
    selectionSort(k+1, k+1)

arr = [5, 4, 1, 100, 95, 43, 2, 10, 52]
N = len(arr)
# 선택 정렬을 재귀함수로 작성하여 정렬해보자.

min_num = arr[0]
min_idx = 0
selectionSort(0, 0)
print(arr)




