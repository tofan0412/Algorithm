# 재귀로 풀면 계속 최대 재귀 깊이를 초과한다.
from collections import deque


def my_calc(num, calc):
    if calc == 0:
        return num + 1
    elif calc == 1:
        return num - 1
    elif calc == 2:
        return num * 2
    elif calc == 3:
        return num - 10


def BFS(N, M):
    Q = deque()
    Q.append((N, 0))

    while Q:
        num, cnt = Q.popleft()
        for i in range(4):
            next_num = my_calc(num, i)
            if next_num == M:
                return cnt + 1
            elif 1 <= next_num <= 1000000:
                Q.append((next_num, cnt+1))


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {BFS(N, M)}')
