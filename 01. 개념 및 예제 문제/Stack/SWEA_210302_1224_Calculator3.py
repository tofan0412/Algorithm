op_order = {"-": 1, "+": 1, "*": 2, "/": 2, "(": 0}

for tc in range(1, 11):
    N = int(input())
    arr = input()
    res = ''
    stack = []
    for i in range(len(arr)):
        if arr[i] == '(' or arr[i] == ')':
            if arr[i] == '(':
                stack.append(arr[i])
            else:
                while stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
        elif arr[i].isdigit():
            res += arr[i]
        else:
            if len(stack) > 0:
                while op_order[stack[-1]] >= op_order[arr[i]]:
                    res += stack.pop()
                    if len(stack) == 0:
                        break
                stack.append(arr[i])
            else:
                stack.append(arr[i])
    while len(stack) > 0:
        res += stack.pop()

    # 해당 후위 표기법을 이제 계산하자.

    stack = []
    for word in res:
        # 주의해야 할 점 : 연산자에 대해 피 연산자가 2개가 아닌 경우 error

        # 숫자인 경우 stack에 그냥 넣는다.
        if word.isdigit():
            stack.append(int(word))
        # 연산자를 만난 경우
        #  모든 연산 과정에서, 피연산자가 2개가 안되는 경우에는? error가 발생한다.
        if word == '+':
            try:
                back_num= stack.pop()
                front_num = stack.pop()
            except(IndexError):
                print(f'#{tc} error')
                break
            tmp = front_num + back_num
            stack.append(tmp)
        if word == '-':
            try:
                back_num = stack.pop()
                front_num = stack.pop()
            except(IndexError):
                print(f'#{tc} error')
                break
            tmp = front_num - back_num
            stack.append(tmp)
        if word == '*':
            try:
                back_num = stack.pop()
                front_num = stack.pop()
            except(IndexError):
                print(f'#{tc} error')
                break
            tmp = front_num * back_num
            stack.append(tmp)
        if word == '/':
            try:
                back_num = stack.pop()
                front_num = stack.pop()
            except(IndexError):
                print(f'#{tc} error')
                break
            tmp = front_num / back_num
            stack.append(tmp)
    print(f'#{tc} {stack[-1]}')


