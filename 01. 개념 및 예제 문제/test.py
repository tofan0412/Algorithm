T = int(input())
for tc in range(T):

    N = int(input())

    result = ''
    while True:
        if N == 0:
            break

        left = N % 2
        result += str(left)
        N = N // 2

    result = "".join(reversed(result))
    print(result)

