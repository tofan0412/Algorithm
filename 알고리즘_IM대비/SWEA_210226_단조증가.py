# 정곤이의 단조 증가하는 수
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split())) # N개의 정수

    # 이 중에서 두 수를 뽑는 모든 부분집합을 구하고
    # 해당 부분 집합 중에서 곱이 단조증가인 대상을 선별한다.

    subsets = []
    for subset in range(1 << len(A)):
        print(bin(subset))

        tmp = []
        for element in range(len(A)):
            if subset & (1 << element):
                tmp.append(A[element])
        if len(tmp) == 2:
            subsets.append(tmp[0] * tmp[1])

    # 문제점 : N이 1000개인 경우 부분집합의 개수는 2**1000개이다.
    # subset을 이진수로 바꿨을 때, 1을 2개만 포함하고 있는 대상을 선별해야 한다.

    results = []
    for number in subsets:
        # numbers에 대해 단조증가하는 수인지 확인한다.
        factor = True
        num_str = list(str(number))
        for j in range(len(num_str)-1):
            if num_str[j] > num_str[j+1]:
                # 단조 증가하는 수가 아니다.
                factor = False
                break
        if factor:
            results.append(number)

    # 마지막으로, 단조 증가하는 수 중에서 최대값을 찾는다.
    max_num = 0
    for number in results:
        if number >= max_num:
            max_num = number
    print(f'#{tc} {max_num}')




