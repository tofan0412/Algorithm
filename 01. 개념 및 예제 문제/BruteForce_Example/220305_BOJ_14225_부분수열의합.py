# SILVER1
# 시간 초과가 발생하니까, combination 쓰자
from itertools import combinations
from collections import Counter


n = int(input())
s = list(map(int, input().split()))

result = []
for i in range(1, n+1):
    comb = list(combinations(s, i))
    for j in comb:
        result.append(sum(j))

result = sorted(result)
num_list = [i for i in range(1, result[-1]+2)]

# 여기서 시간초과 발생
# for num in num_list:
#     if num not in result:
#         print(num)
#         break


fin = Counter(num_list) - Counter(result)
print(list(fin.keys())[0])
