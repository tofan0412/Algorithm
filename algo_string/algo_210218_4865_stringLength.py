T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 1. str1에 포함되어 있는 글자를 추가한다.
    tmp = set()
    for char in str1:
        tmp.add(char)

    # 다시 list로 변환한다.
    alphabet_list = list(tmp)
    cnt = [0]*len(alphabet_list)

    for i in range(len(alphabet_list)): # 기준 알파벳이다.
        for j in range(len(str2)): # 검사할 str의 한글자 한글자.
            if str2[j] == alphabet_list[i]:
                cnt[i] += 1

    # max 찾기
    max = -1
    index = 0
    for i in range(len(cnt)):
        if max < cnt[i]:
            max = cnt[i]
            index = i

    print(f'#{tc} {max}')

