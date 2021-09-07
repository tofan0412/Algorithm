T = int(input())

for tc in range(1, T+1):
    str = list(input())
    s = []
    i = 0
    while i < len(str):
        word = str[i] # Stack에 넣을 문자이다.

        # 최초로 넣는 경우에는 바로 넣는다.
        if len(s) == 0:
            s.append(word)
        else: # stack의 크기가 0이 아닌 경우
            before = s[-1]
            if before == word:
                s.pop(-1)
            else:
                s.append(word)
        i += 1
    print(f'#{tc} {len(s)}')