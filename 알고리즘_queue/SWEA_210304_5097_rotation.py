# N개의 숫자로 이루어진 수열이 주어진다.
# 주의 : 10억 이하의 자연수 N개가 주어진다.
# 따라서 append, pop()을 사용해선 안된다. 이 두 내장함수를 사용하면 리스트의 모든 원소가 이동해야 하기 때문에
T = int(input())
for tc in range(1,T+1):
    # N은 수열에서 item의 개수, M은 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 했을 때이다.
    N, M = list(map(int, input().split()))
    queue = list(map(int, input().split()))

    # 일단, append와 pop을 사용해보자.
    for i in range(M):
        t = queue.pop(0)
        queue.append(t)

    print(f'#{tc} {queue[0]}')

# 원형큐와 유사하다.

# Answer
# M = M % N 으로 치환을 해버리자.

# M = M % N
# print(queue[M])
