# SILVER4
# 정수 M개가 주어졌을 때, 이 수가 적혀 있는 카드가 N 내에 있는지 아닌지 구별하시오
def binary_search(arr, target, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if arr[mid] == target:
        factor = True
        return 1

    elif arr[mid] < target:
        # 이미 찾았다면, 더 이상 수행할 필요가 없다.
        return binary_search(arr, target, mid+1, end)
    else:
        return binary_search(arr, target, start, mid-1)


N = int(input()) # 숫자 카드 N개. N은 최대 50만개
arr1 = list(map(int, input().split()))
M = int(input()) # 정수 M개. M도 최대 50만개
arr2 = list(map(int, input().split())) # 수 하나의 범위는 -1000만 ~ 1000만

# 이진탐색의 전제조건 : sorting!
arr1 = sorted(arr1)
result = ''

for num in arr2:
    tmp = binary_search(arr1, num, 0, len(arr1) - 1)
    if tmp == -1:
        result += '0 '
    elif tmp == 1:
        result += '1 '
print(result)

# 시간초과 해결 : factor 해소하니깐 됨.