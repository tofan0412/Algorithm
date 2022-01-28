# SILVER3
# https://velog.io/@skyepodium/%EB%B0%B1%EC%A4%80-14501-%ED%87%B4%EC%82%AC-exjyfr5vgj
N = int(input())
t, p = [], []
for _ in range(N):
    time, pay = map(int, input().split())
    t.append(time)
    p.append(pay)

result = 0
# 1. 먼저 완전탐색으로 문제를 풀어보자.
# 1일차부터 N일차까지, 해당하는 상담을 하거나 안하거나 둘 중 하나.
def solution(day, pay):
    global result
    if day > N:
        return

    # 정확히 N일동안 상담을 진행한 경우
    if day == N:
        if result < pay:
            result = pay
        return

    # day에 상담을 진행하는 경우, t[day] 기간 동안 상담을 진행할 수 없다.
    solution(day+t[day], pay + p[day])
    # day에 상담을 진행하지 않는 경우
    solution(day+1, pay)


solution(0, 0)
print(result)
