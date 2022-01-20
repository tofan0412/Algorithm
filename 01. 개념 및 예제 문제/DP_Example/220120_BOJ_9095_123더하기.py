# SILVER3
def solution(n, selected):
    # n이 0이 되었으며 A+B의 형태로 표현할 수 있다면
    if n == 0 and len(selected) >= 1:
        return 1
    # n이 0이 되었지만, A+B의 형태로 표현할 수 없다면
    result = 0
    if n - 3 >= 0:
        selected.append(3)
        result += solution(n-3, selected)
        selected.pop()
    if n - 2 >= 0:
        selected.append(2)
        result += solution(n-2, selected)
        selected.pop()
    if n - 1 >= 0:
        selected.append(1)
        result += solution(n-1, selected)
        selected.pop()
    return result


T = int(input())
for tc in range(T):
    N = int(input())
    print(solution(N, []))

