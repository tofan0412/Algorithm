def binarySearch(val, left, right):
    global factor, result
    if left > len(A) - 1 or left > right:
        return
    m = (left + right) // 2
    # 왼쪽 탐색
    if A[m] > val:
        factor += 'L'
        binarySearch(val, left, m - 1)
    # 오른쪽 탐색
    elif A[m] < val:
        factor += 'R'
        binarySearch(val, m + 1, right)
    # 찾은 경우
    elif A[m] == val:
        # m이 2개 중에서 왼쪽일 수도 있고, 오른쪽일 수도 있다.
        if not ('LL' in factor or 'RR' in factor):
            result += 1
        else:
            return 0
    else: # 못찾은 경우
        return 0


T = int(input())
for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    # 이진 탐색의 전제조건은 정렬된 상태이다.
    A = list(map(int, input().split())) # 길이는 N개
    A.sort()
    B = list(map(int, input().split())) # 길이는 M개
    # 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
    result = 0


    for i in B:
        factor = ''
        binarySearch(i, 0, len(A)-1)
    print(f'#{tc} {result}')