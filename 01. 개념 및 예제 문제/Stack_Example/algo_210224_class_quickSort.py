def quickSort(arr, begin, end):
    if begin < end:
        p = partition(arr, begin, end)
        # p를 기준으로 왼쪽, 오른쪽을 각각 정렬하게 된다.
        quickSort(arr, begin, p-1)
        quickSort(arr, p+1, end)

# 호어 파티션
def partition(arr, begin, end):
    pivot = (begin + end) // 2 # 가운데 지점을 의미한다. 몫으로 계산하므로 홀수, 짝수 상관 없다.
    L = begin # 왼쪽지점
    R = end # 오른쪽지점
    while L < R:
        while(arr[L] < arr[pivot] and L<R):
            L += 1
        while(arr[R] >= arr[pivot] and L<R):
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            arr[L], arr[R] = arr[R], arr[L]
    a[pivot], arr[R] = arr[R], arr[pivot]
    return R

# L은 피봇을 기준으로 피봇보다 큰 녀석을 찾고
# R은 피봇을 기준으로 피봇보다 작은 녀석을 찾는다.
# L은 배열에서 오른쪽으로 이동하면서 피벗보다 크기가 같은 원소를 찾고,
# R은 배열에서 왼쪽으로 이동하면서 피벗보다 크기가 작은 원소를 찾는다.
# [69, 10 ,30, 2 ,16, 8 , 31, 22]
# 위 예제를 보면 L은 원소 69를 찾았지만, R은 찾지 못해 원소 69에서 L과 만나게 된다.
# L,R이 서로 만났으므로 원소 69를 피봇과 교환하여 피봇 원소2의 위치를 확정한다.

# 이후 피봇 2의 왼쪽 부분집합은 존재하지 않고( 가장 앞에 있으므로 )
# 오른쪽 부분 집합에 대해서 퀵정렬을 수행한다.
# 이 때 L은 10이 되고, R은 22가 된다. 또한 이 때 피봇은 16이 된다.
# L이 찾은 원소 30과 R이 찾은 원소 8을 서로 교환한다.

# 이후 현재 위치에서 L과 R의 작업을 반복한다. 이 때 L은 69라는 16보다 큰 값을 찾았지만,
# R은 16보다 작은 값을 발견하지 못해 69에서 L과 R이 만나게 된다.
# 이 경우 피봇 16과 69의 위치를 교환하며 피봇16의 위치를 확정한다.

#