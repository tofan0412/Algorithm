def perm(idx):
    if idx == length: # 베이비진인지 검사한다.
        run = 0
        triplet = 0
        # 앞 3자리에 대해 run, triplet 검사, 뒤 3자리에 대해 run, triplet 검사!
        if arr[0] == arr[1] == arr[2]:
            triplet += 1
        if arr[3] == arr[4] == arr[5]:
            triplet += 1
        if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
            run += 1
        if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
            run += 1
        # 판단하기
        if run == 2 or triplet == 2 or (run == 1 and triplet == 1):
            print(f'다음은 베이비진입니다 : {arr}')
        return
    else:
        for i in range(idx, length):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx + 1)
            arr[i], arr[idx] = arr[idx], arr[i] # 원복
            perm(idx + 1)

T = int(input())
for tc in range(1, T+1):
    arr = list(input())
    length = len(arr)
    # str -> int
    for i in range(len(arr)):
        arr[i] = int(arr[i])

    # 가능한 모든 조합을 확인한다.
    perm(0)

# 메모이제이션을 통해 단축할 수 있다.