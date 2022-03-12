# dp문제다.
T = int(input())
for tc in range(T):
    case = [(0, 1, 2), (1, 2, 0), (0, 2, 1)]
    stones = list(map(int, input().split())) # x, y, z는 반드시 1 이상이다.

    dp = {}
    dp['111'] = "B"
    dp['100'] = "R"
    dp['010'] = "R"
    dp['001'] = "R"
    # (1, 1, 1)에 1씩 더해가며 경우의 수를 계산해 보자.
    # (2, 1, 1), (1, 2, 1), (1, 1, 2) 해보고 또 각각의 경우에 대해서..
    # 이렇게 하다보면 우리가 원하는 (x, y, z)가 나오지 않을까?

    tmp = list(stones)
    while True:
        for i in range(3):
            tmp[i] 



