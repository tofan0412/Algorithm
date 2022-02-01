# SILVER2
# n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장
# 큰 합을 구하려고 한다. 단, 수는 1개 이상 선택해야 한다.
# n < 100,000

N = int(input())
numbers = list(map(int, input().split()))

