width = int(input())
buildings = list(map(int, input().split()))

result = 0
for idx in range(0, width):
    # 빌딩 높이가 0이어선 안된다.
    if buildings[idx] > 0:
        # 양쪽의 건물 중에서 높은 건물을 기준으로 잡는다.
        if buildings[idx-1] > buildings[idx + 1]:
            higher1 = buildings[idx - 1]
        else:
            higher1 = buildings[idx + 1]

        if higher1 > buildings[idx]:
            continue
        else:
            cnt = buildings[idx] - higher1

        # 2칸 떨어져 있는 건물에 대해서도 판단한다.
        if buildings[idx - 2] > buildings[idx + 2]:
            higher2 = buildings[idx - 2]
        else:
            higher2 = buildings[idx + 2]

        if higher2 > higher1:
            cnt = (buildings[idx] - higher1) - (higher2 - higher1)
            if cnt > 0:
                result += cnt
        # 양옆 건물보다 낮은 건물인 경우, 계산할 필요가 없다.
        else:
            result += cnt

print(f'#{T} {result}')