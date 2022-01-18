# BRONZE1
# 이번에는 완전탐색이 아닌, DP로 풀어보자.

# DP의 조건 1. 큰 문제는 작은 문제로 풀 수 있다.
# DP의 조건 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다. ex) fibo(1)과 fibo(4)에서 사용되는 fibo(1)

# 아래 코드는 21년 8월 31일에 내가 제출한 코드이다.
# 설탕은 3x + 5y로 표현할 수 있다. (x는 3kg 봉지의 개수, y는 5kg 봉지의 개수)
# 이 때 x + y의 합이 최소가 되어야 한다.
def solution(N):
    result = -1
    # x는 3Kg 설탕 봉지의 개수, y는 5Kg 설탕 봉지의 개수이다.
    x, y = 0, 0

    # 5kg 봉지는 0부터 시작한다.
    while 5*y <= N:
        temp = N - (5 * y) # 먼저 5Kg 봉지로 하나씩 담는다. y는 1씩 증가한다.
        if temp % 3 != 0: # 5Kg 봉지로 담고 난 후에 남은 설탕의 양이 3Kg으로 담을 수 없다면 다시 5Kg 봉지로 뺀다.
            pass # 아무것도 하지 않고 다음으로 넘어간다.
        else: # 5Kg 봉지로 설탕을 담고 남은 양이 3Kg 봉지로 담을 수 있다면
            x = temp // 3
            if result > x + y or result == -1: # 더 적은 봉투의 양이 나왔거나, 이전까지 담을 수 없었다면
                result = x + y
        x = 0
        y += 1

    print(f'{result}')


N = int(input())
solution(N)
