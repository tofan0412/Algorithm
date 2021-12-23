# SILVER1
from collections import deque

N, K = map(int, input().split())
seconds = 0
result = 80000

queue = deque()

queue.append(N)
queue.append('sec')

while queue:
    now = queue.popleft()
    # 'sec'인 경우, 초를 세고 queue에 추가한다.
    if now == 'sec':
        seconds += 1
        queue.append('sec')
    # 값이 17인 경우, 그 때까지 소모된
    elif now == 17:
        if result > seconds:
            result = seconds
            break
    else:
        queue.append(now - 1)
        queue.append(now + 1)
        queue.append(now * 2)


print(result)
