# 큐 생성
# 방문 표시 리스트 생성
# 시작점 인큐
def bfs(N, M):
    v = [0] * 1000001 # 방문 기록이면서, 최초 지점으로부터 거리값을 기록한다.
    q = [0] * 1000001 # 큐의 크기를 고정해놓는다.
    front, rear = -1, -1
    rear += 1
    q[rear] = N # 큐에 시작 노드 인큐
    v[N] = 1 # 시작 노드 방문 표시
    while front != rear: #  큐가 비어있지 않으면
        front += 1
        n = q[front] # 다음 노드를 꺼내고
        if n == M:
            return v[n] - 1
        t = [n-10, n-1, n+1, n*2] # 인접 노드번호 계산
        for x in t:
            # 유효한 노드 번호이고
            if 1 <= x <= 1000000:
                # 아직 방문하지 않았다면
                if v[x] == 0:
                    v[x] = v[n] + 1 # 거리를 기록하고
                    rear += 1
                    q[rear] = x # 큐에 추가한다.


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs(N, M)}')
