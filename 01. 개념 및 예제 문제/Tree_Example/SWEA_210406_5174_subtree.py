def preorder(n):
    global cnt
    if n != 0: # 왼쪽 자식 노드가 존재하는 경우.
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


T = int(input())
for tc in range(1, T+1):
    E, N = list(map(int, input().split())) # 이때 N은 ROOT NODE 번호를 의미한다.
    node = E + 1
    info = list(map(int, input().split()))
    ch1 = [0]*(node+1)
    ch2 = [0]*(node+1)

    for i in range(0, len(info)-1, 2):
        if ch1[info[i]] == 0:
            ch1[info[i]] = info[i+1]
        else:
            ch2[info[i]] = info[i+1]

    cnt = 0
    preorder(N)
    print(f'#{tc} {cnt}')