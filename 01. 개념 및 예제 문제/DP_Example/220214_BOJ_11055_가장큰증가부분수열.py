# SILVER2
N = int(input())
arr = list(map(int, input().split()))

# 1. 완전 탐색으로 풀어보자.

d = [0] * N # d[k]는 arr[k]를 마지막 원소로 갖는 증가 부분 수열 중, 가장 길이가 긴 증가 부분 수열의 길이를 뜻한다.
d[0] = 1
# ex) d[3] -> arr[3]을 마지막 원소로 갖는 증가 부분 수열 중 LIS의 길이
for i in range(1, N):
    candidates = [] # arr[i]가 붙을 수 있는 D[i-1]의 후보를 찾는다.
    for j in range(0, i):
        if arr[j] < arr[i]:
            candidates.append(d[j])
    if len(candidates) > 0:
        d[i] = max(candidates) + 1
    else:
        d[i] = 1

print(max(d))

# 2. DP를 이용하여 풀어보자.