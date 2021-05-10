def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])


def union_set(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1 ,T + 1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(M)]
    p = [i for i in range(N+1)] # 부모 요소
    cnt = 0

    for i in range(len(data)):
        union_set(data[i][0], data[i][1])

    for i in range(1, N + 1):
        if p[i] == i:
            cnt += 1

    print(f'#{tc} {cnt}')


