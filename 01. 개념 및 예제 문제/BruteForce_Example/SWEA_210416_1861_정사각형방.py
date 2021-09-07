# 재귀를 한다면 최대 100만칸이 존재할 수 있으므로, 불가능하다!

def BFS(queue):
    visited = [[0]*N for _ in range(N)]
    cnt = 0 # 몇 군데를 방문했는지 기록할 곳. 최초 방 방문까지 포함하므로..
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        point = queue.pop(0)
        visited[point[0]][point[1]] = 1 # 방문 처리
        cnt += 1  # 방문한 방의 개수 +1
        # 상하좌우에 대해서 모두 검색해야 한다.
        for i in range(4):
            move_to_row = point[0] + dr[i]
            move_to_col = point[1] + dc[i]

            check1 = 0 <= move_to_row and move_to_row < N
            check2 = 0 <= move_to_col and move_to_col < N
            if check1 and check2 and visited[move_to_row][move_to_col] == 0:
                if info[move_to_row][move_to_col] == info[point[0]][point[1]] + 1:
                    queue.append((move_to_row, move_to_col))
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    # 처음에 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 프로그램을 작성하여라.

    queue = []
    max_cnt = 0
    max_idx = ()
    for row in range(N):
        for col in range(N):
            queue.append((row, col))
            visited_cnt = BFS(queue)
            if max_cnt < visited_cnt:
                max_cnt = visited_cnt
                max_idx = (row, col)
            elif max_cnt == visited_cnt:
                # 주의!! 이동할 수 있는 방의 개수가 최대인 방이 여럿이라면, 그 중에서 적힌 수가 가장 작은 것을 출력
                if info[max_idx[0]][max_idx[1]] > info[row][col]:
                    max_idx = (row, col)

    print(f'#{tc} {info[max_idx[0]][max_idx[1]]} {max_cnt}')


# N,N까지 인덱스를 가진 v 배열을 만들고 0으로 초기화한다.
# 모든 i, j에 대해 A[i][j] 주변에 A[i][j] +1 인 방이 있는지 확인한다.
# 예제에서 1번~9번방까지 있었으므로, 리스트를 [0,0,0,0,0,0,0,0,0] 과 같이 만든다.
# 2의 경우 주변에 2보다 1 큰 3이 존재하므로, 해당하는 리스트의 인덱스에 +1한다.
# 사방 탐색해서 있으면 +1
