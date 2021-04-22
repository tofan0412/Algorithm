def change(cnt):
    if cnt == N:
        return
    else:


T = int(input())
for tc in range(1, T+1):
    boards, N = input().split() # N은 교환 횟수

    answer = list(boards)
    answer = list(map(int, answer))

    # N번 교환할 때, 모든 경우의 수를 구한다.
    change(0)



