# BRONZE1
T = int(input())
for tc in range(T):
    N, X, Y = map(int, input().split()) # N은 장난감 자동차의 수, X는 트랙의 길이, Y는 부스터 속도 한계치
    V = list(map(int, input().split()))
    times = []
    # 1. 각 인원별로 트랙을 완주하는데 소요되는 시간을 계산한다.
    for v in V:
        times.append(X / v)

    # 만약 부스터를 쓰지 않아도 우승인 경우 0 출력
    # N-1번이 내 참가번호
    # 만약 이미 공동 우승이라면.. 안된다!
    if times.index(min(times)) == (N-1):
        print(0)
        continue

    # 이외의 경우는 부스터를 써야만 1등을 할 수 있는 경우이다.
    min_z = 0
    factor = False
    for Z in range(Y, 0, -1):
        # 트랙의 길이 X에서 1초 간 Z의 속도로 이동한다.
        x_afterBooster = X - Z
        # 이제 남은 거리를 원래의 속도로 이동했을 때 초를 계산해보자.
        sec = (x_afterBooster / V[N-1]) + 1 # 1초는 부스터로 이동했을 때 걸린 시간
        if min(times) > sec:
            min_z = Z
            factor = True
        # 만약 최단 시간보다 부스터를 사용한 시간이 짧지 않다면 break
        else:
            break
    if not factor:
        print(-1)
        continue
    else:
        print(min_z)