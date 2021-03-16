T = int(input())

def top(arr):
    return arr[-1]

for tc in range(1,T+1):
    # 괄호만 따로 저장한다.
    str = input()
    case = ''
    for word in str:
        if word == '{' or word == '}' or word == '(' or word == ')':
            case += word

    # case에 대해 검사한다.
    s = []
    result = '0'
    for bracket in case:
        # 여는 괄호 (, { 인 경우 스택에 추가한다.
        if bracket == '(' or bracket == '{':
            s.append(bracket)
        # 닫히는 괄호인 경우 : 종류가 2가지이다.
        if bracket == '}':
            if len(s) == 0:
                result = '0'
                break
            # 스택의 길이가 0이 아닌경우에는 판단을 해야한다.
            elif top(s) != '{': # 짝이 안맞는 경우이다.
                result = '0'
                break
            else:
                # 스택의 길이가 0보다 크고, 짝이 맞는 경우 마지막 값을 제거한다.
                s.pop(-1)

        if bracket == ')':
            if len(s) == 0:
                result = '0'
                break
            elif top(s) != '(':
                result = '0'
                break
            else:
                s.pop(-1)

        # 여기까지 와서, 스택에 남은 값이 있는지를 확인하고
        # 남은 값이 있으면 괄호가 잘못 표기되었다는 뜻이다.
        if len(s) == 0:
            result = '1'

    print(f'#{tc} {result}')
