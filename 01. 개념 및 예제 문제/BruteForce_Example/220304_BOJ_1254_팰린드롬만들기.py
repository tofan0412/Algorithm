# SILVER1
s = list(input())
# 1. 최초에 팰린드롬인 경우를 검사한다.
factor = True
for i in range(len(s) // 2):
    if s[i] != s[-(1 + i)]:
        factor = False

if factor:
    print(len(s))
# 2. 최초에 팰린드롬이 아닌 경우, 하나씩 붙여준다.
else:
    idx = len(s) - 2
    while idx > -1:
        s.append(s[idx])

        # 붙이고 나서 한번 검사해본다.
        factor = True
        for i in range(len(s) // 2):
            if s[i] != s[-(1 + i)]:
                factor = False
                break
        if factor: # 붙였더니 팰린드롬이 됐다면 해당 길이 출력
            print(len(s))
            break
        else: # 여전히 팰린드롬이 아닌 경우 추가적으로 붙여준다.
            idx -= 1
            continue


# 처음에는 문자 전체를 갖다 붙이면 된다고 생각했지만, 반례 존재
# 문자 abdfhdyrbdbsdfghjkllkjhgfds의 경우 abdfhdyrbdb와 sdfghjkllkjhgfds로 나눌 수 있으며
# 2번째인 sdfghjkllkjhgfds의 경우 이미 완전히 팰린드롬이다.
# 따라서 abdfhdyrbdb를 뒤에서부터 하나씩 붙여주면 된다.

# ex. qew'asdfdsa'rby 의 경우 ->