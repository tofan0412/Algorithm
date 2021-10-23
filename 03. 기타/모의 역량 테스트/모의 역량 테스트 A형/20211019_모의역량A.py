T = int(input())

# 상,하,좌,우 순서이다.
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def solution(x, y):
    # 4방향 탐색을 실시한다.
    result = 0
    nowPos = [x, y]
    for way in range(4):
        while (0 < nowPos[0] and nowPos[0] < N) and (0 < nowPos[1] and nowPos[1] < N):
            # 다음으로 이동할 위치.
            nextPos = [nowPos[0] + dr[way], nowPos[1] + dc[way]]
            if myList[nextPos[0]][nextPos[1]] != 0:
                # 너머에 잡을 수 있는 알이 있는지 파악한다.






    return result


for tc in range(T+1):
    N = int(input())
    myList = [list(map(int, input().split())) for _ in range(N)]
    # 제일 먼저 현재 포의 위치를 찾는다.
    myPos = [0, 0]
    for i in range(N):
        for j in range(N):
            if myList[i][j] == 2:
                myPos[0] = i
                myPos[1] = j

    solution(myPos[0], myPos[1])



