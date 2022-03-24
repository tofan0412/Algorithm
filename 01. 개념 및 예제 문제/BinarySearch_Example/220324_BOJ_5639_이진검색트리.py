# GOLD5
'''
이진 검색 트리는 다음과 같은 세 가지 조건을 만족하는 이진트리이다.
노드의 왼쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 작다
노드의 오른쪽 서브트리에 있는 모든 노드의 키는 노드의 키보다 크다.

전위 순회는 루트 - 왼쪽 - 오른쪽
후위 순회는 왼쪽 오른쪽 루트


'''


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.node


