# GOLD4
def solution(arr, point):


R, C = map(int, input().split())
arr = [[]*C for _ in range(R)]

for i in range(R):
    arr[i] = list(input())

# 사방 탐색. 완전 탐색
for row in range(R):
    for col in range(C):
        solution([row, col])