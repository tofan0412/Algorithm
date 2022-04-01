import sys

def binary_search(arr, start, end): # start는 구간의 시작 높이값, end는 구간의 종료 높이를 뜻한다.
    global height, cases

    # 종료 조건을 설정해야 한다.
    if start >= end:
        return

    mid = (start + end) // 2
    criterion = mid + 0.5

    cnt = 0
    for i, obs in enumerate(arr):
        # 1. i가 짝수인 경우 석순이고
        if i % 2 == 0:
            if obs > criterion:
                cnt += 1
        # 2. i가 홀수인 경우 종유석이다.
        else:
            if criterion > (height - obs):
                cnt += 1

    cases.append(cnt)
    # 모든 cnt는 기록해 둔다. 단 이진탐색을 통해 탐색하고 있으므로, h의 높이에 대해 모든 구간을 확인하는 건 절대 아니다.
    # 아래 방향 탐색
    binary_search(arr, start, mid)
    binary_search(arr, mid+1, end)


width, height = map(int, sys.stdin.readline().rstrip().split())
obstacles = []
for _ in range(width):
    obstacles.append(int(sys.stdin.readline().rstrip()))

cases = []
binary_search(obstacles, 0, height)

# 이제 케이스에서 가장 min값을 찾고, 해당 min값이 몇번 출현했는지 세본다.
cases.sort()
min_val = cases[0]
result = 0
for case in cases:
    if case != min_val:
        break
    result += 1

print(str(min_val) + " " + str(result))
