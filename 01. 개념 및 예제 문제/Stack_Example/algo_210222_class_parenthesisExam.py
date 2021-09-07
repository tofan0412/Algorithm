test1 = '()()((()))'
test2 = '((()((((()()((()())((())))))'

def exam(str):
    s = []
    for word in str:
        # 여는 괄호인 경우, 삽입
        # 다만, 스택의 크기가 정해져 있다면 데이터를 넣을 공간이 존재하는지를 먼저 검사해야 한다.
        if True: # 검사하는 부분
            pass

        if word == '(':
            s.append(word)
        # 닫는 괄호일 경우, 리스트에서 마지막 값 삭제
        elif word == ')':
            # 리스트의 길이가 0인 경우 제거할 여는 괄호가 존재하지 않으므로 false를 반환한다.
            if len(s) == 0:
                print('리스트의 길이가 0입니다.')
                return False
            s.pop(-1) # 이게 가능한 이유 : 여는 괄호 없이 닫는 괄호만 단독으로 나오지 않는다는 규칙이 존재한다.
    if len(s) == 0:
        return True
    else:
        return False

print(exam(test1))
print(exam(test2))