# 배열의 데이터를 퀵 정렬하는 함수를 작성하고, 테스트 해보시오.

# 입력 예)
# 11 45 23 81 28 34
# 11 45 22 81 23 34 99 22 17 8
# 1 1 1 1 1  0 0 0 0 0

def quickSort(list, left, right):
    if left < right:
        s = partition(list, left, right)
        quickSort(list, left, s-1)
        quickSort(list, s+1, right)


def partition(list, left, right):
    p = list[left] # 왼쪽 끝 값을 피봇으로 설정한다.
    i, j = left, right
    while i <= j: # i는 왼쪽에서 시작해서 오른쪽으로, j는 오른쪽에서 시작해서 왼쪽으로 이동한다.
        while list[i] <= p: # 피봇보다 큰 값을 찾아 이동한다.
            i += 1
        while list[j] >= p:
            j -= 1
        if i < j:
            list[i], list[j] = list[j], list[i]
    list[i], list[j] = list[j], list[i]
    return j

# 어느 시점이 되면 i와 j가 서로 교차할 수 있다. (j가 i보다 앞에 있는 경우)
# 이 경우 j의 위치에 있는 값과 i의 위치에 있는 값을 서로 바꿔준다.
list_0 = [3, 2, 4, 6, 9, 8, 7, 5]
list_1 = [11, 45, 23, 81, 28, 34]
list_2 = [11, 45, 22, 81, 23, 34, 99, 22, 17, 8]
list_3 = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

quickSort(list_0, 0, len(list_0)-1)
quickSort(list_1, 0, len(list_1)-1)
quickSort(list_2, 0, len(list_2)-1)
quickSort(list_3, 0, len(list_3)-1)

print(list_1)
print(list_2)
print(list_3)


