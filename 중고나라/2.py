# 2개 이상의 점을 연결하여 연결된 점들을 없애는 게임이다.
# 같은 색의 점만 연결할 수 있고, 상하좌우로 이동하며 연결할 수 있다. 점은 4가지 색상이 존재한다.
# BFS 문제이다.
# 점들을 가장 길게 연결할 수 있는 경우를 찾으려고 한다.
def solution(board):
    answer = -1
    height = len(board)
    width = len(board[0])

    # board의 모든 점에 대해 DFS를 수행해야 한다.
    for row in range(height):
        for col in range(width):
            number = board[row][col]  # DFS를 시작할 기준점의 숫자값

            stack = list()
            visited = [[False] * width for _ in range(height)]  # board와 동일한 크기의 visited를 만든다.
            distance = [[0] * width for _ in range(height)]  # 거리를 저장할 배열을 만든다.

            stack.append((row, col))
            visited[row][col] = True  # 현재 점 방문 처리
            distance[row][col] = 1  # 현재 위치의 거리값을 1로 설정한다.

            # 4방 탐색
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            while stack:
                now = stack.pop()

                for way in range(4):
                    gr = now[0] + dr[way]
                    gc = now[1] + dc[way]

                    # 인덱스 검사
                    if 0 <= gr < height and 0 <= gc < width:
                        # 상하좌우 탐색해서, 같은 값이면 저장
                        if board[gr][gc] == number and not visited[gr][gc]:  # 방문하지 않은 곳 중에서
                            stack.append((gr, gc))
                            visited[gr][gc] = True
                            dist = distance[now[0]][now[1]] + 1
                            if answer < dist:
                                answer = dist
                            distance[gr][gc] = dist
                            break  # DFS라면 여기서 break을 해줘야 한다.
    return answer