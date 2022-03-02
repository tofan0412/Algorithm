# SILVER2

# 지민이는 세계에서 가장 유명한 사람이 누구인지 궁금해졌다. 가장 유명한 사람을 구하는 방법은 각 사람의 2-친구를 구하면 된다.
# 어떤 사람 A가 또 다른 사람 B의 2-친구가 되기 위해선, 두 사람이 친구이거나, A와 친구이고 B와 친구인 C가 존재해야 된다.
# 여기서 가장 유명한 사람은 2-친구의 수가 가장 많은 사람이다.

INF = int(1e9)
n = int(input()) # 사람의 수 N. 50보다 작다.
graph = [list(input()) for _ in range(n)]

result = [0] * n

for a in range(n):
    friends = []
    for b in range(n):
        # 1. 일차적으로 나와 Direct 친구인 대상을 계산한다.
        if graph[a][b] == 'Y':
            friends.append(b)
            result[a] += 1
    # 2. 친구의 친구를 계산해본다.
    for friend in friends:
        friends2 = []
        for k in range(n):
            if k == a:
                continue

            if graph[friend][k] == 'Y' and k not in friends:
                # friends.append(k) # 이러면 for문이 영향을 받는다.
                friends2.append(k)
                result[a] += 1
        friends = friends + friends2
    # print(str(a) + "의 친구는!", friends)
print(max(result))

