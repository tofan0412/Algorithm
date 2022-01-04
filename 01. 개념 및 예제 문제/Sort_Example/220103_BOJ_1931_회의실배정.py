# SILVER2
N = int(input())
time = []
for _ in range(N):
    time1, time2 = map(int, input().split())
    time.append([time1, time2])

# 정렬은 내장함수를 이용하자... 시간 초과 뜬다 ㅠㅠ -> 혹시 종료 시간 기준으로 하지 않았기 때문에...?
time = sorted(time, key=lambda time:time[0])
# 종료 시간이 빨라야, 더 많은 회의를 집어넣을 수 있다.
# 이후 종료시간을 기준으로 다시 한번 정렬해 준다. 그 이유 : (9, 10) 과 (10, 10)
time = sorted(time, key=lambda time:time[1])

now = time[0]
end_time = now[1] # 종료 시간을 기록해 둔다.
cnt = 1
for lecture in time[1:]: # 자기 자신은 제외해야 한다.
    if now[0] < lecture[0] < now[1]:
        continue
    if lecture[0] < end_time:
        continue
    # 시작 시간이 현재 강의 시간과 겹치지 않으며, 현재 시작한 강의 이후에 시작하는 강의인 경우
    else:
        cnt += 1
        now = lecture
        end_time = now[1]
print(cnt)