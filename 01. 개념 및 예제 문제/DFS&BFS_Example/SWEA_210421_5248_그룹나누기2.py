# 대표원소를 찾는다.
def Find_set(x):
    if x == parent[x]:
        return x
    else:
        return Find_set(parent[x])


# y의 부모를 x의 부모로 교환한다.
def Union_set(x, y):
    parent[Find_set(y)] = Find_set(x)


T = int(input())
for tc in range(1, T + 1):
    # N번까지 / M은 신청서의 개수
    N, M = map(int, input().split())
    # 최초에는 자기 자신이 부모이다.
    parent = [i for i in range(N+1)]
    data = list(map(int, input().split()))

    for i in range(0, M):
        Union_set(data[2*i], data[2*i+1])

    # print(parent)

    result = []
    for i in range(len(parent)):
        tmp = Find_set(i)
        if tmp not in result:
            result.append(tmp)
    # print(result)

    print(f'#{tc} {len(result)-1}') # 0은 빼야 한다.