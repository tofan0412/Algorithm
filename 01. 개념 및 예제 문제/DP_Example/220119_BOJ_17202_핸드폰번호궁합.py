# BRONZE1
A = list(map(int, list(input())))
B = list(map(int, list(input())))

memo = {}

# 1. 미리 모든 경우의 수를 저장해둔다.
for i in range(0, 10):
    for j in range(0, 10):
        # 뒤집어서 있다면 제외
        if memo.get(str(j) + str(i)) is not None:
            continue
        else:
            memo[str(i) + str(j)] = (i + j) % 10

tmp = []
for i in range(len(A)):
    tmp.append(A[i])
    tmp.append(B[i])

# 이제 하나씩 계산해보자.
result = []
while True:
    if len(result) == 2:
        print(f'{result[0]}{result[1]}')
        break

    result = [] # 인접한 두 수를 더한 새로운 리스트를 만들어야 하므로 한번 초기화.
    for i in range(len(tmp)-1):
        v = 0
        if memo.get(str(tmp[i]) + str(tmp[i+1])) is not None:
            v = memo.get(str(tmp[i]) + str(tmp[i+1]))
        elif memo.get(str(tmp[i+1]) + str(tmp[i])) is not None:
            v = memo.get(str(tmp[i+1]) + str(tmp[i]))
        result.append(v)
    tmp = list(result)
