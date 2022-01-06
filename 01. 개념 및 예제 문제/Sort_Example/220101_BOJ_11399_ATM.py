# SILVER3
N = int(input())
p = list(map(int, input().split()))

# p의 범위는 1분 ~ 1,000분이다.
count = [0] * 1001

for i in p:
    count[i] += 1

# count 배열은 소요 시간을 오름차순으로 정렬한 것이다.
result = []
for (index, cnt) in enumerate(count):
    for j in range(cnt):
        result.append(index)

answer = 0
for i in range(len(result), 0, -1):
    answer += result[len(result) - i] * i
print(answer)
