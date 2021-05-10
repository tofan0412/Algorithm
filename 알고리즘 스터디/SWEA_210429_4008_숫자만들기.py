def calc(num1, num2, op):
    global op_info
    if op == 0:
        op_info[0] -= 1
        return num1 + num2
    elif op == 1:
        op_info[1] -= 1
        return num1 - num2
    elif op == 2:
        op_info[2] -= 1
        return num1 * num2
    elif op == 3:
        op_info[3] -= 1
        if num2 != 0:
            return num1 // num2
        elif num2 == 0:
            return False


def perm(idx, val):
    a = 0
    global max_val, min_val
    if idx == N:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val
        return
    else:
        num = nums[idx]
        for i in range(4):
            # 4가지 연산을 모두 수행.. 단 주어진 연산자 개수를 만족하면서
            tmp = val
            val = calc(val, num, i)
            if -1 not in op_info:
                # val이 false가 될수도 있다.
                if val:
                    perm(idx+1, val)
                    val = tmp
                else: # val이 False라면, 즉 나눗셈 기호 뒤에 0이 위치했다면
                    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    op_info = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_val = 1000001
    max_val = -1000001
    perm(1, nums[0])

    print(f'#{tc} {max_val - min_val}')
