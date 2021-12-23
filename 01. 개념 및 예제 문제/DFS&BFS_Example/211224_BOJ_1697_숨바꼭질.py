# SILVER1
from collections import deque

N, K = map(int, input().split())
seconds = 0
result = 80000

numbers = set() # Memoization 위해
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
        result = seconds
        break
    else:
        if not (now - 1) in numbers:
            number = now - 1
            if number == 17:
                result = seconds + 1
                break
            else:
                queue.append(now - 1)
                numbers.add(now - 1)
        if not (now + 1) in numbers:
            number = now + 1
            if number == 17:
                result = seconds + 1
                break
            else:
                queue.append(now + 1)
                numbers.add(now + 1)
        if not (now * 2) in numbers:
            number = now * 2
            if number == 17:
                result = seconds + 1
                break
            else:
                queue.append(now * 2)
                numbers.add(now * 2)
print(result)
