# SILVER3
# 지금까지 플레이한 게임횟수 X, 이긴 게임의 수 Y가 주어졌을 때
# 형택이가 최소 몇 게임을 더 해야 Z가 변하는지 구하는 프로그램을 작성하시오.
def binary_search(start, end, total, win, rate):
    global result
    if start > end:
        return

    # mid는 더 플레이해야 할 게임 수를 뜻한다.
    mid = (start + end) // 2

    # 승률을 계산해보자. 앞으로 질 일은 없기 때문에 새로 하는 게임 = 이긴 게임이다.
    after_win = win + mid
    after_end = total + mid # 전체 게임수도 변화한다.

    tmp = after_win * 100 // after_end

    # 만약 tmp가 변화하지 않았다면. 더 많은 게임을 해야한다는 뜻..?
    if tmp == rate:
        binary_search(mid+1, end, total, win, rate)
    # 만약 승률이 변화했다면. mid를 기록해 두고, 더 적은 게임수로도 승률이 변하는지 확인해보자.
    elif tmp > rate:
        result = mid
        binary_search(start, mid-1, total, win, rate)


X, Y = map(int, input().split())
# Z = int((Y / X) * 100) # 이건 안된다.
Z = Y * 100 // X


# 현재 승률 Z가 변하려면, 최소 1판은 해야 한다. 따라서 start는 1판으로 하고, end는 전체 게임 회수인 X로 하자.
result = -1
binary_search(1, 2000000001, X, Y, Z)
print(result)


# 원인 : float을 int로 바꾸는 것이 문제다.
# 3 1 OR 3 2를 입력해 보자.