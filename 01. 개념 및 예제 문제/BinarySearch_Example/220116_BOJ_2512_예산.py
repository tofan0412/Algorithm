# SILVER3
def binary_search(arr, start, end, limit):
    global max_limit
    # 같은 경우에는 냅둔다. 이 조건을 명확히 하는게 굉장히 중요하다.
    if start > end:
        return

    mid = (start + end) // 2

    # mid를 기준으로 예산을 측정해 본다.
    total = 0
    for budget in arr:
        if budget >= mid:
            total += mid
        else:
            total += budget

    if total <= limit:
        max_limit = mid
        # 한번 올려서도 진행해보자.
        binary_search(arr, mid+1, end, limit)
    # 만약 total이 초과한 경우에는 정수 상한액을 낮춰야 한다.
    elif total > limit:
        binary_search(arr, start, mid-1, limit)


N = int(input()) # 지방의 수
budgets = list(map(int, input().split()))
M = int(input()) # 총 예산을 나타내는 정수

# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
if sum(budgets) < M:
    print(max(budgets))

# 2. 모든 요청이 배정될 수 없는 경우에는, 특정한 정수 상한액을 계산하여 예산을 배정한다.
else:
    max_limit = 0
    binary_search(budgets, 0, max(budgets), M) # start값을 min으로 잡아선 안된다..!
    print(max_limit)
