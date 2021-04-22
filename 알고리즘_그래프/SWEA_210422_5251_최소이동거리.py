def travel(point, weight):
    global result
    # 목적지에 도착했다면 종료한다.
    if point == N:
        result = weight
        return

    min_weight = (N) * 10
    min_node = 0
    for E in road_info:
        start = E[0]
        end = E[1]
        e_weight = E[2]

        # 인접하다면
        if point == start:
            # 이전 노드의 최단거리 + 간선의 가중치가 더 작으면 갱신, 아니라면 냅둔다.
            if e_weight + distance_info[point] < distance_info[end]:
                distance_info[end] = e_weight + distance_info[point]

            # 이동할 정점에 부여된 가중치가 min값보다 작다면
            if distance_info[end] <= min_weight:
                min_weight = distance_info[end]
                min_node = end
    travel(min_node, min_weight)


T = int(input())
for tc in range(1, T + 1):
    # N은 지점의 끝번호(0번 ~ N번까지) / E는 도로의 개수
    N, E = map(int, input().split())
    # 시작 구간 s, 끝 지점 e, 구간 거리 w가 주어진다.
    road_info = [list(map(int, input().split())) for _ in range(E)]
    # 출발 지점은 0번이다.

    # 출발 지점으로부터 자신에게 이르는 경로의 길이를 기록할 배열을 만들자.
    distance_info = [float('inf')] * (N+1)
    distance_info[0] = 0
    result = 0
    travel(0, distance_info[0])

    print(f'#{tc} {result}')
