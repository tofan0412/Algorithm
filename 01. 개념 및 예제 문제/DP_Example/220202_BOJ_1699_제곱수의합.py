# SILVER3
# 11의 경우 3^2 + 1^2 + 1^2으로 표현 가능하다.

# 주어진 자연수 N을 이렇게 제곱수들의 합으로 표현할 때에, 그 항의 최소개수를 구하는 프로그램을 작성하시오.
dp = [0] * 100001
dp[1] = 1
N = int(input())


# N이 제곱수인 경우 바로 memo에 저장
# 그렇지 않은 경우 f(n) = f(n-1) + f(1)
def check(num):
    return int(num ** 0.5) ** 2 == num

number = 1
keep = 0 # 이전에 나온 가장 큰 정수 제곱근
while True:
    if number > N:
        break

    if check(number):
        dp[number] = 1
        keep = number
    else:
        dp[number] = dp[keep] + dp[number - keep]
    number += 1

print(dp[N])

