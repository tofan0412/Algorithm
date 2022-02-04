# SILVER2
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장
# 큰 합을 구하려고 한다. 단, 수는 1개 이상 선택해야 한다.
# n < 100,000

N = int(input())
numbers = list(map(int, input().split()))

# 1. 완전 탐색으로 풀기. 이때 시간 복잡도는 O(N^2)이다.
memo = [-1001] * (N + 1)
for length in range(1, N+1):
    for index in range(len(numbers)):
        tmp = sum(numbers[index:index+length])
        if memo[length] < tmp:
            memo[length] = tmp
print(max(memo))

