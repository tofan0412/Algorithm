'''
그래프를 DFS와 BFS로 탐색한 결과를 출력하는 프로그램을 출력하시오. 단, 방문할 수 있는 정점이 여러 개인 경우
정점 번호가 작은 것을 먼저 방문하고 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
'''


def bfs():

    return

def dfs():

    return


N, M, V = map(int, input().split())  # 정점(node)의 개수 N, 간선(edge)의 개수 M, 시작점 V
adj = [[] for i in range(M+1)] # N이 1에서부터 시작하므로

'''
[[]] * 10 과 [[] for i in range(10)]의 차이
전자의 경우 하나의 []를 만들고 10개의 메모리상 주소가 모두 동일한 곳을 가리키고 있다.
후자의 경우 각각 10개의 []를 만드므로 메모리상 주소가 모두 다르다.
또한 후자의 경우 리스트 표현식(comprehension)으로 만든 것이다. 원래 코드는 다음과 같다. 
a = []
for i in range(3):
    line = []
    a.append(line)
'''

'''
리스트 표현식은 다음과 같은 예시가 존재한다.
[식 for 변수 in 리스트
list(식 for 변수 in 리스트)
ex)
a = [i for i in range(10)] # 결과 : [0,1,2,3,4,5,6,7,8,9]
즉 range(10)으로 0부터 9까지 생성하여 변수 i에 숫자를 꺼내고, 최종적으로 i를 이용하여 
리스트를 만든다는 뜻이다.
'''


print(adj)
for i in range(M):
    node1, node2 = map(int, input().split())
    adj[node1].append(node2)

print(adj)


