import sys
from collections import deque
t = int(input())

for _ in range(t):
    p = list(sys.stdin.readline())
    n = int(input())
    x = sys.stdin.readline()

    di = 1
    try:
        if n == 0:
            x = []
        else:
            x = deque(list(map(int, x.strip()[1:-1].split(','))))

        for i in p:
            if i == 'R':
                di *= -1
            elif i == 'D':
                if x:
                    if di == 1:
                        x.popleft()
                    else:
                        x.pop()
                else:
                    raise ValueError
    except ValueError:
        print("error")
    else:
        if di == -1:
            x = reversed(x)
        print("[" + ",".join(list(map(str, x))) + "]")