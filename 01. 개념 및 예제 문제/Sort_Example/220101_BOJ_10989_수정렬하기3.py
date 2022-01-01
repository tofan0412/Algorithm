# SILVER5
import sys

N = int(sys.stdin.readline())
numbers = []
count = [0] * 10001

for _ in range(N):
    count[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    for j in range(count[i]):
        sys.stdout.write(str(i) + "\n")

# sys.stdout과 sys.stdin을 쓰는 거에 익숙해질까..