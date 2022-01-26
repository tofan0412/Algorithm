# SILVER3
# https://daimhada.tistory.com/181
N = int(input())
stairs = [] # 1,2,3,4,5,6
for _ in range(N):
    stairs.append(int(input()))

stairs = [0] + stairs
memo = [0] * len(stairs)
# 첫번째 칸에 올라왔을 때 최대값은 stairs[0]이다.
memo[1] = stairs[1]
# 두번째 칸에 올라왔을 때 최대값은 둘 중 하나다. 연속으로 2칸 올라왔거나, 한번에 2칸 올라왔거나

for stair in range(2, N+1):
    # 직전칸에서 올라온 경우의 최댓값 / 전전칸에서 올라온 경우의 최대값
    memo[stair] = max(stairs[stair] + stairs[stair-1] + memo[stair-3], stairs[stair] + memo[stair-2])

print(memo[-1])




