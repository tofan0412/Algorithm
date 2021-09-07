# 교수님 코드.. !

def makeT(n):
    global idx # 트리의 인덱스. 1번부터 시작해서 N번까지 존재한다.
    global N # 트리의 가장 마지막 인덱스 번호.
    if n <= N:
        makeT(n * 2)  # 왼쪽 서브트리 방문
        tree[n] = idx  # 중위 순회로 현재 노드값 저장
        idx += 1
        makeT(n * 2 + 1)  # 오른쪽 서브트리 방문


# 부모 노드의 인덱스 번호가 N일 때
# 왼쪽 자식 노드의 인덱스 번호는 N*2, 오른쪽 자식 노드의 인덱스 번호는 N*2+1이다.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    idx = 1
    tree = [0 for i in range(N + 1)]  # 리스트를 이용한 완전 이진 트리 저장
    makeT(1) # 1번 인덱스부터 시작한다.
    print('#{} {} {}'.format(tc, tree[1], tree[N // 2]))