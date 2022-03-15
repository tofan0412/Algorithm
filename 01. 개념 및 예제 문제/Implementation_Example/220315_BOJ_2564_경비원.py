# SILVER1
width, height = map(int, input().split())
cnt_store = int(input())

route = [0 for _ in range((width + height) * 2)]
store_indexs = []
for _ in range(cnt_store):
    way, idx = map(int, input().split())
    if way == 1: # 북쪽인 경우
        route[idx] = 1
        store_indexs.append(idx)
    if way == 2: # 남쪽인 경우
        route[width + height + (width - idx)] = 1
        store_indexs.append(width + height + (width - idx))
    if way == 3:
        route[width + height + width + (height - idx)] = 1
        store_indexs.append(width + height + width + (height - idx))
    if way == 4:
        route[width + idx] = 1
        store_indexs.append(width + idx)

# 마지막으로 경비 위치 표시
way, idx = map(int, input().split())
std_point = 0
if way == 1:
    route[idx] = 2
    std_point = idx
if way == 2:
    route[width + height + (width - idx)] = 2
    std_point = width + height + (width - idx)
if way == 3:
    route[width + height + width + (height - idx)] = 2
    std_point = width + height + width + (height - idx)
if way == 4:
    route[width + idx] = 2
    std_point = width + idx

# 이제 세면 된다.
result = 0
for store in store_indexs:
    if store < std_point:
        # 1. 시계방향으로 재보기
        dist1 = std_point - store
        # 2. 반시계 방향으로 재보기
        dist2 = store + (len(route) - std_point)
        result += min(dist1, dist2)
    elif store > std_point:
        # 1. 시계방향으로 재기
        dist1 = (len(route) - store) + std_point
        # 2. 반시계 방향으로 재기
        dist2 = store - std_point
        result += min(dist1, dist2)

print(result)






