def preorder(i):
    if i <= V+1:
        print("<전위>현재 노드는 {}".format(i))
        if ch1[i] != 0:
            preorder(ch1[i]) # 존재하는 경우에만
        if ch2[i] != 0:
            preorder(ch2[i]) # 존재하는 경우에만


def middleorder(i):
    if i <= V+1:
        if ch1[i] != 0:
            middleorder(ch1[i])  # 존재하는 경우에만
        print("<중위>현재 노드는 {}".format(i))
        if ch2[i] != 0:
            middleorder(ch2[i])  # 존재하는 경우에만


def postorder(i):
    if i <= V+1:
        if ch1[i] != 0:
            postorder(ch1[i])  # 존재하는 경우에만
        if ch2[i] != 0:
            postorder(ch2[i])  # 존재하는 경우에만
        print("<후위>현재 노드는 {}".format(i))

# 12
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
T = int(input())
for tc in range(1, T+1):
    V = int(input()) # 간선의 개수가 V개라면, 노드의 개수는 V+1이다.
    info = list(map(int, input().split()))
    ch1 = [0] * (V+2)
    ch2 = [0] * (V+2)

    for i in range(0, len(info), 2):
        if ch1[info[i]] == 0:
            ch1[info[i]] = info[i+1]
        else:
            ch2[info[i]] = info[i+1]

    preorder(1)
    print('-----------')
    middleorder(1)
    print('-----------')
    postorder(1)


