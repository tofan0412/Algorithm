## 1. 중위순회 코드
# def inorder(n):
#     if n != 0:
#         # 왼쪽 자식 노드 - 부모 노드 - 오른쪽 자식 노드 순으로 읽는다.
#         inorder(ch1[n])
#         print(tree[n], end='')
#         inorder(ch2[n])
#
# for tc in range(1, 11):
#     N = int(input())
#     tree = [0 for _ in range(N+1)]
#     ch1 = [0] * (N + 1)
#     ch2 = [0] * (N + 1)
#
#     for _ in range(N):
#         info = input().split()
#         tree[int(info[0])] = info[1]
#         if len(info) > 2: # 자식 노드를 하나 또는 2개 가지고 있다는 뜻이다.
#             child_info = info[2:]
#             for i in range(len(child_info)):
#                 if ch1[int(info[0])] == 0: # 왼쪽 자식 노드가 비어있다면
#                     ch1[int(info[0])] = int(child_info[i])
#                 else:
#                     ch2[int(info[0])] = int(child_info[i])
#
#     # 중위순회로 읽으면 된다.
#     inorder(1)


## 2. 사칙연산
# 후위순회로 읽어야 한다..!


## 3. subtree
# def preorder(n):
#     global cnt
#     if n != 0:
#         cnt += 1
#         preorder(ch1[n])
#         preorder(ch2[n])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     E, N = list(map(int, input().split())) # E는 간선의 개수, N은 기준이 될 노드의 인덱스 번호.
#     # 간선의 개수 +1 = 전체 노드의 개수.
#     ch1 = [0] * (E + 2)
#     ch2 = [0] * (E + 2)
#     cnt = 0
#
#     info = list(map(int, input().split()))
#     for i in range(0, len(info), 2):
#         if ch1[info[i]] == 0: # 첫번째 자식이 비어있는 경우
#             ch1[info[i]] = info[i+1]
#         else: # 첫번째 자식이 존재하는 경우
#             ch2[info[i]] = info[i + 1]
#
#     preorder(N)
#     print(f'#{tc} {cnt}')


## 4. 이진탐색
# 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 이진 탐색 트리의 특징 : 부모 노드를 기준으로 왼쪽은 부모 노드보다 작은값, 오른쪽은 부모 노드보다 큰값을 저장한다.
# 위 규칙이 모든 subtree에 적용된다.
# N/2번(홀수인 경우 소수점 버림) 노드에 저장된 값을 출력하는 프로그램을 만드시오.

# def makeT(n):
#     global idx
#     global N
#     if n <= N:
#         makeT(n*2)
#         tree[n] = idx
#         idx += 1
#         makeT(n*2 + 1)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input()) # 노드의 끝번호
#     tree = [0 for _ in range(N+1)]
#     idx = 1
#     makeT(1)


## 5. 노드의 합
# T = int(input())
# for tc in range(1,T+1):
#     N, M, L = list(map(int, input().split())) # N은 노드의 개수, M은 리프 노드의 개수, 값을 출력할 노드 번호 L
#     tree = [0] * (N+1)
#     for i in range(M):
#         info = list(map(int, input().split())) # 리프 노드 번호, 1000 이하의 자연수
#         tree[info[0]] = info[1]
#
#     for j in range(N, 0, -1): # 1번까지만 하면 된다.
#         # 부모 노드에 현재 노드 값을 더한다.
#         tree[j // 2] += tree[j]
#     print(f'#{tc} {tree[L]}')

## 6. 광교 문제
T = int(input())
for tc in range(1, T+1):
    N, V = list(map(int, input().split())) # N은 마지막 노드 번호, V는 간선 개수. V + 1이 노드의 개수
    info = list(map(int, input().split()))
    ch1 = [0] * (V+2)
    ch2 = [0] * (V+2)

    for i in range(0, len(info), 2):
        if ch1[info[i]] == 0:
            ch1[info[i]] = info[i+1]
        else:
            ch2[info[i]] = info[i + 1]

    level = 0
    # 트리의 높이를 계산해서 출력하시오.
    def treeheight(n, l):
        global level
        # 높이가 3인 노드들 출력하기
        if l == 3:
            print("{}의 높이는 3입니다.".format(n))
        if n != 0:
            print("현재 노드값은 {}".format(n))
            treeheight(ch1[n], l+1)
            treeheight(ch2[n], l+1)
        elif n == 0:
            level = l
    treeheight(1, 0)
    print("트리의 높이는 {}입니다".format(level))

    # 높이가 3인 노드들을 출력하시오.

    # 3번 노드가 루트인 트리의 전체 노드수.

    # 8번 노드와 10번 노드의 공통 조상을 출력하시오.





