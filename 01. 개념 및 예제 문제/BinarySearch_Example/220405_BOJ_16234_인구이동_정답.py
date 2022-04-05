import sys
from collections import deque
read = sys.stdin.readline

N, L, R = map(int, read().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, read().split())))

def BFS(memo, pos, matrix):

    global N, L, R
    i, j = pos
    memo[i][j] = 1
    nations = [(i, j)]
    q = deque([(i, j)])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        i, j = q.popleft()
        for idx in range(4):
            new_i = i + dx[idx]
            new_j = j + dy[idx]
            if new_i < 0 or new_j < 0 or  new_i >= N or new_j >= N:
                continue
            elif memo[new_i][new_j] == 0 and (L <= abs(matrix[i][j] - matrix[new_i][new_j]) <= R):
                q.append((new_i, new_j))
                nations.append((new_i, new_j))
                memo[new_i][new_j] = 1

    if len(nations) == 1:
        return

    sum_v = 0
    for nation in nations:
        sum_v += matrix[nation[0]][nation[1]]
    avg = sum_v // len(nations)
    for nation in nations:
        matrix[nation[0]][nation[1]] = avg



def divide(matrix):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    global N
    memo = [[0]*N for _ in range(N)]
    k = 0
    for i in range(N):
        for j in range(N):
            if memo[i][j] == 0:
                k += 1
                need_bfs = False

                for idx in range(4):
                    new_i = i + dx[idx]
                    new_j = j + dy[idx]
                    if new_i < 0 or new_j < 0 or  new_i >= N or new_j >= N:
                        continue
                    elif memo[new_i][new_j] == 0 and (L <= abs(matrix[i][j] - matrix[new_i][new_j]) <= R):
                        need_bfs = True
                        break

                if need_bfs:
                    BFS(memo, (i, j), matrix)
                else:
                    memo[i][j] = 1

    return k



cnt = 0
while True:
    nations_list = []
    k = divide(matrix)
    if k == N*N:
        print(cnt)
        sys.exit()
    cnt += 1
