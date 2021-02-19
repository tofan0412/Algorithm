# 5432. 쇠막대기 자르기 문제 해결법

# 순차적으로 char를 확인하면서, 열린 괄호가 몇개인지를 count한다.
# (((()의 경우 cnt의 값은 4가 된다.
# )를 만나면 레이저를 의미하므로, cnt에서 하나를 빼고, ans에 cnt만큼의 값을 더한다.
# 레이저가 아닌데 )를 만나면 ans에 +1을 한다. (위에선 잘린 왼쪽만 생각한 것이므로, 오른쪽도 더해야 한다. )
# 또한 닫힌 괄호를 만나면 cnt에서 1을 뺀다. ( cnt는 현재 쌓인 합판의 개수라고 할 수 있으므로, 닫힌 괄호를 만나면 한판이 하나 끝난 것이다.)

T = int(input())

for tc in range(1,T+1):
    iron_bar = input()

    cnt = 0 # 막대 수
    ans = 0 # 정답

    for i in range(len(iron_bar)):
        if iron_bar[i] == "(":
            cnt += 1 # 열린 괄호라면 무조건 적으로 +1을 한다.
        else: # 레이저인지, 합판이 끝나는 걸 나타내는 닫힌 괄호인지는 모르지만
            # 레이저인 경우에는 잘못 넣었으니까 -1하고
            # 닫힌 괄호인 경우에는 하나의 합판이 끝났으므로 -1
            cnt += 1

            # 레이저라면
            if iron_bar[i-1] == "(":
                ans += cnt # 레이저로 인해 잘린 막대들이 생겼으므로
            else: # 막대 끝이라는 뜻
                ans += 1
    print(f'#{tc} {ans}')

# Answer 2

for tc in range(1, int(input()+1)):
    iron_bar = input()
    # 실제로 철봉이 담길 리스트
    s = [] # 스택을 의미한 것이다.
    ans = 0

    for i in range(len(iron_bar)):
        # 열린 괄호라면 s 리스트에 넣어두기
        if iron_bar[i] == "(":
            s.append("(")
        else:
            # 무조건 꺼내기
            s.pop()
            # 괄호 안에 -1을 넣게 되면 가장 끝 인덱스를 가져와서 뽑는다.
            #아무런 값도 넣지 않아도 가장 끝 값을 뺀다.

            if iron_bar[i-1] == "(": # 레이저라는 뜻이다.
                ans += len(s)
            else:
                ans += 1

    print(f'#{tc} {ans}')
