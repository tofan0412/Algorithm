T = int(input())

for tc in range(1, T+1):
    N = int(input())
    queue = []
    for i in range(1,N+1):
        queue.append(i)
    while len(queue) != 1:
        # 처음에는 가장 윗장을 버린다.
        queue.pop(0)
        # 그 다음 카드는 뽑아서 아래로 옮긴다.
        t = queue.pop(0)
        queue.append(t)

    print(f'#{tc} {queue[-1]}')