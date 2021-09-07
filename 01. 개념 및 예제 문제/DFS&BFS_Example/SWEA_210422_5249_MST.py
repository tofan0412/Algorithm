def make_set(V):
    return [i for i in range(V+1)]


def find_set(x):
    if x == parent[x]:
        return x
    else:
        return find_set(parent[x])


# y의 부모요소를 x로 선택한다.
def union_set(x, y):
    parent[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    # 마지막 노드번호 V(0번부터 시작한다)와 간선의 개수 E
    V, E = map(int, input().split())
    # 데이터의 각 원소는 리스트이며, 처음 2개 요소는 양 끝 노드 번호, 마지막 요소는 가중치를 의미한다.
    data = [list(map(int, input().split())) for _ in range(E)]

    data.sort(key= lambda x : x[2])
    # 부모 요소를 나타내는 리스트 생성
    parent = make_set(V)

    idx = 0
    cnt = 0
    result = 0
    # 모든 정점을 방문해야 한다.
    while cnt < E:
        # 사이클을 형성해선 안된다.
        node1, node2, weight = data[idx][0], data[idx][1], data[idx][2]

        val1 = find_set(node1)
        val2 = find_set(node2)
        # val1과 val2가 같으면, 사이클을 생성한다. 따라서 이 간선은 선택할 수 없다.
        if val1 == val2:
            idx += 1
            # 해당 간선은 선택하지 않는다.
            cnt += 1
            continue
        else:
            union_set(node1, node2)
            result += weight
            # 간선 선택했으므로 +1
            cnt += 1
            # 다음 간선으로 넘어간다.
            idx += 1

    print(f'#{tc} {result}')