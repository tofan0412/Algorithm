# 덱(deque)이 가장 빠른 결과 보여줌.
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
    global test_case
    Q = deque()
    Q.append((N, 0))
    num_lst[N] = test_case
    while Q:
        num, cnt = Q.popleft()
        for i in range(4):
            next_num = my_calc(num, i)
            if next_num == M:
                return cnt + 1
            elif 1 <= next_num <= 1000000 and num_lst[next_num] != test_case:
                Q.append((next_num, cnt + 1))
                num_lst[next_num] = test_case  # 궤적


T = int(input())
num_lst = [0] * 1000001  # 탐색 궤적 리스트 (시간 단축용)
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(test_case, BFS(N, M)))