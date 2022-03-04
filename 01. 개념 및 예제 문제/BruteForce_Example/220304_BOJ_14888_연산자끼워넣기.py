# SILVER1
def solution(res, idx, op):
    global max_result, min_result, operators, arr
    a = 3
    if idx == n: # 마지막까지 계산을 다한 경우
        if res > max_result or max_result == int(2e12):
            max_result = res
        if res < min_result or min_result == -int(2e12):
            min_result = res
        return

    # 1. 덧셈해본다.
    tmp = list(op)
    if tmp[0] > 0:
        tmp[0] -= 1
        solution(res + arr[idx], idx+1, tmp)
        tmp[0] += 1
    # 2. 뺄셈해본다.
    if tmp[1] > 0:
        tmp[1] -= 1
        solution(res - arr[idx], idx+1, tmp)
        tmp[1] += 1
    # 3. 곱셈 해본다.
    if tmp[2] > 0:
        tmp[2] -= 1
        solution(res * arr[idx], idx+1, tmp)
        tmp[2] += 1
    # 4. 나눗셈 해본다.
    if tmp[3] > 0:
        tmp[3] -= 1
        # 4-1. 나누고자 하는 수가 음수인 경우
        if res < 0:
            num = abs(res) // arr[idx]
            solution(-num, idx + 1, tmp)
        else:
            num = res // arr[idx]
            solution(num, idx + 1, tmp)


n = int(input()) # 수의 개수
arr = list(map(int, input().split()))
operators = list(map(int, input().split())) # 순서대로 덧셈, 뺄셈, 곱셈, 나눗셈이다.
max_result = -int(2e12)
min_result = int(2e12)
solution(arr[0], 1, operators)

print(max_result)
print(min_result)

