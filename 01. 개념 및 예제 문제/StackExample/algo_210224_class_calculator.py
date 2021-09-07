# 중위 표기법을 후위 표기법으로 변경하기
# 컴퓨터는 실제로 모든 수식을 후위 표기법을 이용하여 처리한다.
# 처리 속도가 빨리지고, 복잡한 괄호를 모두 생략할 수 있다.
# 피연산자는 바로 출력하고 연산자는 stack에 push하여
# 수식이 끝나면 남아있는 연산자를 모두 pop하여 출력하시오

str = '2+3*4/5'
stack = []
result = ''
for word in str:
    if word == '+' or word == '-' or word == '*' or word == '/':
        stack.append(word)
    else:
        result += word
while len(stack):
    result += stack.pop(-1)
print(result)

# 교수님 코드 : top pointer를 이용하여 계산하였다.
# stack에 하나씩 넣을 때마다 top을 1씩 증가 시켰다. (시작은 -1)
# 이후 다음과 같은 코드를 작성한다.

# for i in range(0, top+1):
#     print(stack.pop(), end="") # stack에서 연산자를 꺼내어 출력한다.


