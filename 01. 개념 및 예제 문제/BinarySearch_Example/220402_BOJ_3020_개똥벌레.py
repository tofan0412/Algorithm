# GOLD5
width, height = map(int, input().split()) # 이 때 n은 항상 짝수이다.
obstacles = []
for _ in range(width):
    obstacles.append(int(input()))

# 주의해야 할 건, 짝수번째 index에 있는 대상은 석순의 높이이고,
# 홀수번째 인덱스에 있는 대상은 종유석의 깊이이다.

# 특정 높이를 선택해야 한다.
# 높이가 h일 때, 구간 또한 h개가 존재한다.

def binary_search():
    


