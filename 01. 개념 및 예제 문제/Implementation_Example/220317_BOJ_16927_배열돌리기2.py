from collections import deque
# GOLD5
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * m for _ in range(n)]

# 굳이 다 회전시킬 필요가 없다. cnt % (n * m -4) 만큼 회전시키면 된다.
for cnt in range(r % ((n - 1) * 2 + (m - 1) * 2)):



# 선형 리스트를 만들어 복제하는 방법 : 80 x 40만 해도 1초 이상의 시간이 소요된다.