# SILVER3
def binary_search(arr, max_k, min_k, N):
    global result
    # 종료 조건 입력
    if max_k < min_k:
        return None

    mid = (max_k + min_k) // 2
    # mid가 0이 나오는 경우?

    # mid 값을 기준으로 잘랐을 때 나오는 조각을 모두 더해보자.
    sum_lan = 0
    for line in arr:
        sum_lan += line // mid

    if sum_lan >= N:
        result = mid
    # 기준치보다 개수가 부족한 경우 기준 길이를 줄여야 한다.
    if sum_lan < N:
        return binary_search(arr, mid-1, min_k, N)
    # 기준치보다 개수가 많은 경우 기준 길이를 올린다. (우리의 목표는 최대 길이를 구하는 것이기 때문에)
    else:
        return binary_search(arr, max_k, mid+1, N)


K, N = map(int, input().split()) # 항상 K <= N
lengths = []
for i in range(K):
    lengths.append(int(input()))

# 이분 탐색을 통해 K를 구해보자.
maxk = max(lengths)

result = 0
binary_search(lengths, maxk, 1, N)
print(result)



