from pprint import pprint
# GOLD5
n, m = map(int, input().split())
r, c, direction = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]


# 0북, 1동, 2남, 3서
def dfs():
    stack = list()
    stack.append((r, c))

    # dr, dc를 서, 남, 동, 북 기준으로 설정한다.
    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    d = direction
    cnt = 0
    while stack:
        nr, nc = stack.pop()
        # 1. 현재 위치를 청소한다.
        # 후진해서 방문했을 경우도 있으므로 최초로 청소하는 경우에만 치워야 한다.

        if not visited[nr][nc]:
            visited[nr][nc] = True
            cnt += 1

        is_blocked = True
        # 2. 현재 위치에서 현재 방향을 기준으로, 왼쪽 방향부터 차례대로 인접한 칸을 탐색한다.
        for way in range(4):
            # 방향에 따라 탐색 구역이 달라진다.
            idx = (4 - d + way) % 4
            gr = nr + dr[idx]
            gc = nc + dc[idx]

            if 0 <= gr < n and 0 <= gc < m:
                if maps[gr][gc] == 0 and not visited[gr][gc]:
                    # 방향 전환
                    d = 3 - idx
                    # 해당 위치로 이동
                    is_blocked = False
                    stack.append((gr, gc))
                    break
        # 4방향 모두 탐색한 결과 갈 곳이 없다면
        if is_blocked:
            # 후진할 수 있으면 후진한다.
            # 0북, 1동, 2남, 3서
            # 서, 남, 동, 북 (dr의 인덱스 순서)
            # 0이면 1이 나와야 하고
            # 1이면 0이 나와야 하고
            # 2이면 3이 나와야 하고
            # 3이면 2가 나와야 한다.

            j = (4 - d + 1) % 4
            br = nr + dr[j]
            bc = nc + dc[j]
            if 0 <= br < n and 0 <= bc < m:
                if maps[br][bc] == 0:
                    stack.append((br, bc))
                else:
                    break
            else:
                break
    return cnt


print(dfs())
