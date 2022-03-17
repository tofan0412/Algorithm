# SILVER1

def check_palindrome(s, pt1, pt2):
    # pt1과 pt2부터 검사를 시작한다.
    result = True
    while pt1 < pt2:
        if s[pt1] != s[pt2]:
            result = False
            break
        pt1 += 1
        pt2 -= 1
    return result


tc = int(input())
cases = []
for _ in range(tc):
    cases.append(list(input()))

for case in cases:
    is_palindrome = True
    is_half_palindrome = False
    is_string = False

    p1 = 0
    p2 = len(case) - 1

    # 회문을 검사한다.
    while p1 < p2:
        if case[p1] != case[p2]:
            is_palindrome = False

            # 하나씩 검사해보자.
            r1 = check_palindrome(case, p1+1, p2)
            r2 = check_palindrome(case, p1, p2-1)
            if r1 or r2:
                is_half_palindrome = True
                break # 나머지 부분이 모두 회문임을 확인했으므로, 더이상 진행할 필요가 없다.
            else:
                is_string = True
                break # 나머지 부분이 회문이 아닌 것을 확인했으므로, 더이상 진행할 필요가 없다.
        p1 += 1
        p2 -= 1

    if is_palindrome:
        print(0)
    elif is_half_palindrome:
        print(1)
    elif is_string:
        print(2)

# 시간초과 발생..