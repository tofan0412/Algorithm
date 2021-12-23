# SILVER1
from collections import deque
def solution(arr, queue):
    day = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        tmt = queue.popleft()

        if tmt == ['dayEnd']:
            # 'dayEnd'를 pop하고 만약 queue에 남은 대상이 없다면 끝내야 한다.
            if len(queue) == 0:
                break
            else:
                day += 1
                queue.append(['dayEnd'])
        else:
            for way in range(4):
                nr = tmt[0] + dr[way]
                nc = tmt[1] + dc[way]

                # 사방탐색 실시한다.
                # 1. IndexError 고려하기
                if 0 <= nr < N and 0 <= nc < M:
                    # 익지 않은 토마토라면..
                    if arr[nr][nc] == 0:
                        queue.append([nr, nc])
                        arr[nr][nc] = 1 # 익은 토마토로 수정
    # queue가 끝났음에도, 0이 남아있다면 이는 주변에 토마토가 없기 때문이다.
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] == 0:
                return -1
    return day


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
# 1. 저장될 때부터 모든 토마토가 익어있다면, 0을 출력한다. 즉, arr 내에 0이 없어야 한다.
finish = False

for row in range(N):
    for col in range(M):
        # 익지 않은 토마토가 하나라도 있는지 확인한다.
        if arr[row][col] == 0:
            finish = True
        elif arr[row][col] == 1:
            # 익은 토마토의 위치를 저장한다.
            queue.append([row, col])

# 최초로 익은 토마토 위치를 모두 파악했으면, 구분자를 넣는다.
queue.append(['dayEnd'])

if not finish:
    print(0)
else:
    print(solution(arr, queue))



