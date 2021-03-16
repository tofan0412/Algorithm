T = int(input())

for tc in range(1, T+1):
    case = list(input().split())
    stack = []

    for word in case:
        # 주의해야 할 점 : 연산자에 대해 피 연산자가 2개가 아닌 경우 error
        if word == '.':
            # .을 만나 결과값을 반환할 때, stack에 쌓인 값이 2개 이상인 경우 error
            # .은 항상 연산식의 마지막에 오므로, break을 할 필요가 없다.
            if len(stack) > 1:
                print(f'#{tc} error')
            else:
                print(f'#{tc} {int(stack.pop())}')

        # 숫자인 경우 stack에 그냥 넣는다.
        if word.isdigit():
            stack.append(int(word))
        # 연산자를 만난 경우
        #  모든 연산 과정에서, 피연산자가 2개가 안되는 경우에는? error가 발생한다.
        if word == '+':
            try:
                back_num = stack.pop()
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







