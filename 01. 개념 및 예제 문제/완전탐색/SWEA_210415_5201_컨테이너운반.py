# 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려고 한다.
# 트럭당 한대의 컨테이너 운반 가능.
# 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
# A도시에서 B도시로 최대 M대의 트럭이 편도로 한번만 운행한다고 한다.

# 최대한 중량을 많이 옮겨야 한다.

T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split())) # N은 컨테이너의 개수, M은 트럭의 개수
    W = list(map(int, input().split())) # N개의 컨테이너 개개의 무게
    T = list(map(int, input().split())) # M개 트럭의 적재용량

    # 컨테이너 개개의 무게를 먼저 정렬한다.
    W.sort(reverse=True)
    # 컨테이너 하나하나에 대해 트럭에 실을 수 있는지부터 확인한다..
    result = 0
    for truck in range(len(T)):
        for container in range(len(W)):
            if T[truck] >= W[container]: # 적재 가능하다.
                result += W[container]
                W.pop(container) # 이미 적재했으므로 제거한다.
                break # 해당 트럭에 대해 적재했으므로 for문 종료

    print(f'#{tc} {result}')



