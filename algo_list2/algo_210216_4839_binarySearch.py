T = int(input())

for tc in range(1, T+1):
    P,Pa,Pb = list(map(int, input().split()))

    right = P
    left = 1 # 첫 페이지
    cnt_a = 0
    factor_a = False
    # A 먼저 탐색한다.
    while left <= right: # 시작 - 끝 페이지가 같아지면 탐색을 끝낸다.
        center = int((left + right) / 2)

        if Pa == center:
            # 찾은 경우이다.
            factor_a = True
            break
        elif center > Pa:
            right = center
        elif center < Pa:
            left = center
        else: #못찾은 경우
            break

        cnt_a += 1

    # B도 탐색한다.
    left = 1 # 초기화
    right = P
    cnt_b = 0
    factor_b = False

    while left <= right:
        center = int((left + right) / 2)

        if Pb == center:
            factor_b = True
            break
        elif center > Pb:
            right = center
        elif center < Pb:
            left = center
        else: # 못찾은 경우
            break

        cnt_b += 1

    # 검색 횟수를 떠나서, 어느한쪽만 찾은 경우에는 찾은 사람이 승자이다.
    # if factor_a and not factor_b:
    #     print(f'#{tc} A')
    # elif factor_b and not factor_a:
    #     print(f'#{tc} B')

    # 이제부터는 둘다 해당 페이지를 찾은 경우이다.
    if cnt_a > cnt_b:
        print(f'#{tc} B')
    elif cnt_a < cnt_b:
        print(f'#{tc} A')
    else:
        print(f'#{tc} 0')