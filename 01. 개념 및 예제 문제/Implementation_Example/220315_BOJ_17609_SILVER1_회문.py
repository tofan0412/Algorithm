# SILVER1
tc = int(input())
cases = []
for _ in range(tc):
    cases.append(list(input()))

for case in cases:
    is_palindrome = True
    is_half_palindrome = False
    is_string = False
    cnt = 0
    p1 = 0
    p2 = len(case) - 1

    while p1 < p2:
        if case[p1] != case[p2]:
            is_palindrome = False

            # pop()을 해서 하지 말고, p1과 p2를 조작해서 해보자.
            if case[p1+1] != case[p2] and case[p1] != case[p2-1]:
                # 일치하지 않는 문자 중 어느 하나를 제거하더라도, 일치하지 않는다면 문자를 2개 이상 지워야 한다는 뜻이다.
                is_half_palindrome = False
                is_string = True
                break
            # 어느 한 문자를 지워서 다시 양 포인터 값이 동일해진 경우
            elif case[p1+1] == case[p2]:
                case.pop(p1)
                cnt += 1 # 문자를 제거한 횟수를 뜻한다.
                p2 -= 1
                continue
            elif case[p1] == case[p2-1]:
                case.pop(p2)
                cnt += 1
                p1 += 1
                p2 -= 1
                continue
        p1 += 1
        p2 -= 1

    if is_palindrome:
        print(0)
    elif cnt == 1:
        print(1)
    else:
        print(2)


# 현재 코드의 문제점 : 2문자 이상을 제거해서 palindrome이 되는 경우 True를 반환..
