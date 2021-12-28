# SILVER5
# 주의할 점 : N의 최대 수가 1,000,000이다

N = int(input())
arr = []
for i in range(N):
    number = int(input())
    arr.append(number)

# 1. 이전과 동일하게, 선택 정렬로 정렬해보자.
# 결과 : 시간 초과
for i in range(N):
    min_index = i
    for j in range(i+1, N):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

for number in arr:
    print(number)

# 2. 퀵 정렬을 이용해보자.


