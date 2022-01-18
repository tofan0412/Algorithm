# BRONZE1
# 최대한 적은 봉투로 배달하려고 한다.
N = int(input())
tmp = N
x_limit, y_limit = 0, 0
while True:
    tmp -= 5
    if tmp >= 0:
        x_limit += 1
    else:
        break

tmp = N
while True:
    tmp -= 3
    if tmp >= 0:
        y_limit += 1
    else:
        break

# 이제 완전 탐색
min_cnt = -1
for x in range(x_limit+1):
    for y in range(y_limit+1):
        result = (5 * x) + (3 * y)
        if result == N:
            # 유효한 (x, y) 조합이 이미 만들어진 경우 개수를 비교해 봐야 한다.
            if min_cnt != -1 and x + y < min_cnt:
                min_cnt = x + y
            # 유효한 (x, y) 조합이 만들어지지 않았다면 그냥 바로 고고
            else:
                min_cnt = x + y

print(min_cnt)


