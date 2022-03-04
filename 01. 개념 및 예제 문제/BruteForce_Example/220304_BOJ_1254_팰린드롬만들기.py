# SILVER1
def is_palindrome(s):
    mid = len(s) // 2
    for i in range(mid):
        if s[i] != s[-(1+i)]:
            return False
    return True


def find_palindrome(s): # xyaba에서 aba를 어떻게 찾지? 뒤에 a를 기준으로 찾아야 한다.
    for i in range(len(s)):
        if s[i] == s[-1]:
            # 중간 지점을 기준으로 서로 같은지 비교해보자.
            if s[i:] == reversed(s[i:]):
                return i
    return -1


s = list(input())
# 1. 최초에 팰린드롬인 경우를 검사한다.
if is_palindrome(s):
    print(len(s))
else:
    # 2. 최초에 팰린드롬이 아닌 경우. 팰린드롬인 부분을 찾아보자.




# 1. 팰린드롬인 문자만 존재하는 경우 : aba
# 2. 팰린드롬인 부분 문자열이 좌측에 위치하는 경우 : aba'xy
# 3. 팰린드롬인 부분 문자열이 우측에 위치하는 경우 : xy'aba
# 4. 팬린드롬인 부분이 존재하지 않는 경우 : asdf

# 2의 경우 결국 abaxyxaba와 같이 작성해야 한다.
# 3의 경우 팰린드롬이 아닌 부분만 뒤에 붙이면 된다. 따라서 xyabayx가 된다.
# 4의 경우 전체를 반복해야 한다. 따라서 asdfdsa가 된다.