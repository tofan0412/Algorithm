# SILVER2
N = int(input()) # 회의의 수
start_time = []
end_time = []
for _ in range(N):
    st, et = map(int, input().split())
    start_time.append(st)
    end_time.append(et)

# 우선 시작 시간이 빠른 순으로 정렬하자.
# count_sort 통해 시작 시간 기준으로 나열하자. -> 수의 범위가 int 범위여서 안된다.


