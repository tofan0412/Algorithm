# GOLD5
from itertools import combinations


n, m = map(int, input().split()) # n은 도시의 크기를, m은 가능한 최대 치킨집의 개수를 의미한다.
maps = [list(map(int, input().split())) for _ in range(n)]

# 1. 모든 치킨집의 위치와 집의 위치를 파악한다.
chickens = []
homes = []
for row in range(n):
    for col in range(n):
        if maps[row][col] == 2:
            chickens.append([row, col])
        elif maps[row][col] == 1:
            homes.append([row, col])

# K개 치킨집중 M개의 치킨집 뽑는 모든 경우의 수 계산
candidates = list(combinations(chickens, m))
ans = int(1e9)

for case in candidates:
    total = 0 # 각 케이스에 대한 도시 치킨거리값
    for home in homes:
        cd = int(1e9)
        for chicken in case:
            dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            if cd > dist:
                cd = dist
        total += cd
    if ans > total:
        ans = total

print(ans)
