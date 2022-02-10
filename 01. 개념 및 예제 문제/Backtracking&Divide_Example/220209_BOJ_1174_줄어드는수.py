# SILVER1
# N번째로 작은, 줄어드는 수를 출력하는 프로그램을 작성하시오.
import itertools

N = int(input()) # N은 1부터 1,000,000보다 작거나 같은 자연수이다.
results = []
results.append(0)
results.append(1)
results.append(2)
results.append(3)
results.append(4)
results.append(5)
results.append(6)
results.append(7)
results.append(8)
results.append(9)
number = 10 # 음이 아닌 정수가 기준이다.

# 1~9C(자릿수: 2 ~ 10)
while True:
    if len(results) >= N or number > 9876543210:
        break

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = []
    for number in range(2, 11):
        # tmp는 여러 개의 튜플이 담긴 리스트이다.
        tmp = list(itertools.combinations(arr, number))






    num_list = list(str(number))
    result = True
    nono = True
    # 1. 같은 수가 있는 경우 안된다.
    cnt = [0] * 10
    for i in num_list:
        cnt[int(i)] += 1
        if cnt[int(i)] > 1:
            nono = False

    if not nono:
        number += 1
        continue

    for i in range(len(num_list)-1):
        if int(num_list[i]) <= int(num_list[i+1]):
            result = False
            break

    if result:
        results.append(number)

    number += 1

if not nono:
    print(-1)
elif len(results) >= N:
    print(results[N-1])
else:
    print(-1)
