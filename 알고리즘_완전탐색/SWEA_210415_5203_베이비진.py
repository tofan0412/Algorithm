def checkBabygin(arr):
    run = 0
    trip = 0
    for i in range(len(arr)):
        # TRIPLET 검사
        if arr[i] == 3:
            trip += 1
            arr[i] -= 3
        # RUN 검사
        if i in range(0, len(arr)-2):
            if arr[i] > 0 and arr[i+1] > 0 and arr[i+2] > 0:
                run += 1
                arr[i] -= 1
                arr[i+1] -= 1
                arr[i+2] -= 1

    if run == 1 or trip == 1:
        return True
    else:
        return False

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    # 번갈아 나눠갖는다.
    counting_A = [0] * 10
    counting_B = [0] * 10
    result = 0

    for i, card in enumerate(cards):
        if i % 2 == 0: # 플레이어 1번한테 카드를 준다.
            counting_A[card] += 1
            factor = checkBabygin(counting_A) # 카드를 받을 때마다, run과 triplet을 검사한다.
            if factor:
                result = 1
                break
        else:
            counting_B[card] += 1
            factor = checkBabygin(counting_B)
            if factor:
                result = 2
                break

    print(f'#{tc} {result}')
