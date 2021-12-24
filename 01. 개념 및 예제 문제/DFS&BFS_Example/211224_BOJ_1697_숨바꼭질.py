# SILVER1
from collections import deque

N, K = map(int, input().split())
seconds = 0
result = 0

numbers = set()
queue = deque()

queue.append(N)
numbers.add(N)

queue.append('sec')

while queue:
    now = queue.popleft()
    # 'sec'인 경우, 초를 세고 queue에 추가한다.
    if now == 'sec':
        seconds += 1
        queue.append('sec')
    # 2가지가 동일한 경우 고려
    elif now == K:
        result = seconds
        break
    else:
        minus = now - 1
        plus = now + 1
        multiple = now * 2
        # 연산한 결과가 K인 경우, seconds + 1을 해서 바로 Break
        if minus == K:
            result = seconds + 1
            break
        if plus == K:
            result = seconds + 1
            break
        if multiple == K:
            result = seconds + 1
            break
        # 연산한 결과가 K가 아닌 경우. N의 최대값은 100,000이다!
        else:
            if not (minus in numbers) and minus <= 100000:
                queue.append(minus)
                numbers.add(minus)
            if not (plus in numbers) and plus <= 100000:
                queue.append(plus)
                numbers.add(plus)
            if not (multiple in numbers) and multiple <= 100000:
                queue.append(multiple)
                numbers.add(multiple)
print(result)
