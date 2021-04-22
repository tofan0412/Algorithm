def f(b,t): # 가능한 모든 이진수!
    # bint = int(b, 2)
    bint = 0
    for x in b:
        bint = bint*2 + int(x)
    binary = []
    for i in range(len(b)):
        binary.append(bint ^ (1<<i)) # 2진수의 1비트씩을 바꿔서 저장

T = int(input())
for tc in range(1, T+1):
    b = input()
    t = input()
    r = f(b,t)

    print(f'#{tc} {r}')


