def RPS(arr):
    if len(arr) == 1:
        return arr[0]

    if len(arr) == 2: # arr의 길이가 2인 경우 승자 판별
        # 가위바위보로 승자를 반환한다.
        # return 유형은 [번호, 1or2or3] 꼴이다.
        if arr[0][1] == 1 and arr[1][1] == 1:
            if arr[0][0] < arr[1][0]:
                return arr[0]
            else:
                return arr[1]
        elif arr[0][1] == 1 and arr[1][1] == 2:
            return arr[1]
        elif arr[0][1] == 1 and arr[1][1] == 3:
            return arr[0]

        if arr[0][1] == 2 and arr[1][1] == 2:
            if arr[0][0] < arr[1][0]:
                return arr[0]
            else:
                return arr[1]
        elif arr[0][1] == 2 and arr[1][1] == 1:
            return arr[0]
        elif arr[0][1] == 2 and arr[1][1] == 3:
            return arr[1]

        if arr[0][1] == 3 and arr[1][1] == 3:
            if arr[0][0] < arr[1][0]:
                return arr[0]
            else:
                return arr[1]
        elif arr[0][1] == 3 and arr[1][1] == 1:
            return arr[1]
        elif arr[0][1] == 3 and arr[1][1] == 2:
            return arr[0]

    # 만약 arr의 길이가 >2 인 경우 쪼갠다.
    if len(arr) > 2:
        center = len(arr) // 2
        group1 = []
        group2 = []
        if len(arr) % 2 == 0:
            group1 = arr[0:center]  # center까지만 포함한다.
            group2 = arr[center:len(arr)]
        else: # 홀수인 경우
            group1 = arr[0:center+1]  # center까지만 포함한다.
            group2 = arr[center+1:len(arr)]

        winner1 = RPS(group1)
        winner2 = RPS(group2)
        result = [winner1, winner2]
        return RPS(result)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 인원수
    member_arr = []
    cards = list(map(int, input().split()))

    for i in range(N):
        member_arr.append([i+1, cards[i]]) # 전자는 참가자 번호를, 후자는 해당 사람이 낸 수를 의미한다.

    result = RPS(member_arr)
    print(f'#{tc} {result[0]}')