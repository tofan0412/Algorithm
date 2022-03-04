# N x N 의 체스판에서 N개의 퀸을 두는 경우의 수를 구해라.
# https://sso-feeling.tistory.com/415?category=913126

def adjacent(x): # x번째 row에 대해 검사한다.
    for i in range(x): # 모든 행에 대해 검사한다.
        # 이 때 row[x]는 x행에 위치한 퀸의 열 위치(col)이다.
        # row[x] == row[i]는 0번째 ~ x번째 row까지 겹치는 열이 있는지 검사하는 것이다.
        # abs(row[x] - row[i])는 두 포인트 사이의 열의 차이이고, x - i는 행의 차이이다.
        # 대각선인 경우 ! 행의 차이 = 열의 차이이다.
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i: # 열이 같거나, 대각선이 같은 경우 False
            return False
    return True


def dfs(x): # 이 때 x는 row를 뜻한다.
    global result

    if x == N:
        result += 1
    else:
        # 각 행의 i번째 열에 퀸 놓기
        for i in range(N): # i는 col, 즉 열을 의미한다.
            row[x] = i
            if adjacent(x): # 행, 열, 대각선 체크후 true이면 백트래킹 안하고 계속 진행
                dfs(x+1) # 다음 row로 가서 유망한 곳을 탐색한다.


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)
