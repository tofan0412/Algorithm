# SILVER1
import itertools

N = int(input()) # N은 1부터 1,000,000보다 작거나 같은 자연수이다.
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 전체 경우의 수가 1024가지 밖에 되지 않기 때문에, 그냥 해도 된다.
for length in range(2, 11):
    numbers = list(itertools.combinations(arr, length))
    for cand in numbers:
        tmp = sorted(cand, reverse=True)
        # 이제 줄어드는 수인지 확인해 보자.
        factor = True
        number = ''
        for i in range(len(tmp)):
            if i == len(tmp)-1:
                pass
            else:
                if tmp[i] <= tmp[i+1]:
                    factor = False
            number += str(tmp[i])
        if factor:
            result.append(int(number))


result = sorted(result)
if N+1 > len(result):
    print(-1)
else:
    print(result[N])
