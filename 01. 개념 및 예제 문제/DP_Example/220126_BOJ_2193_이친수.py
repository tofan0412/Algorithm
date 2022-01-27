# SILVER3
# 이진수 중 특별한 성질을 갖는 수를 이친수라 한다. 이친수는 다음의 특성을 갖는다.
# 1. 이친수는 0으로 시작하지 않는다.
# 2. 이친수에서는 1이 두 번 연속으로 나타나지 않는다.
def make_binary(number):
    result = ''

    while True:
        if number == 0:
            break

        left = number % 2
        result += str(left)

        number = number // 2
    return "".join(reversed(result))


# 1부터 점차 점차 키워 가면서, N+1 자리수 이진수가 나올 때까지 반복한다.
N = int(input())
num = 1
number_N = 0
while True:
    binary = make_binary(num)

    if len(binary) > N:
        break

    if len(binary) == N:
        number_N += 1

    num += 1

print()


