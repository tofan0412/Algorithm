# SILVER1
N, M = map(int, input().split())
arr = [[]*M for _ in range(N)]
for row in range(N):
    arr[row] = list(input())

print(arr)