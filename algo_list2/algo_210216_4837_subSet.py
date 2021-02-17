arr = [1,2,3,4,5,6,7,8,9,10,11,12]

T = int(input())
for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    # 이때 N은 부분집합의 원소의 개수, K는 부분집합의 원소의 합이다.
    result = 0
    # 모든 부분집합을 계산한다.
    for subset in range(1<<len(arr)): # 모든 부분집합에 대하여
        cnt = 0 # 원소의 개수를 세기 위한 장치.
        tmp = []
        for element in range(len(arr)):
            if subset & (1<<element):
                cnt += 1
                tmp.append(arr[element])
        # cnt가 N인 경우
        if cnt == N:
            # 내부의 원소합을 계산해봐야 한다.
            sum = 0
            for i in tmp:
                sum += i
            if sum == K:
                result += 1

    print(f'#{tc} {result}')