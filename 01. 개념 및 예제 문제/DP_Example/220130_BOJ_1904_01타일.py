# SILVER3
N = int(input())
memo = [0] * 1000001
memo[1] = 1
memo[2] = 2

num = 3
while True:
    if num > N:
        break

    memo[num] = (memo[num-1] + memo[num-2]) % 15746 # 나눈 값으로 저장하지 않으면 메모리 초과 발생...
    num += 1

print(memo[N])
