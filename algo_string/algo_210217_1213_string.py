for tc in range(1, 11):
    case_num = int(input())
    keyword = input()
    keyword_length = len(keyword)
    str = input()

    cnt = 0
    for word in str:
        # 첫글자가 찾고자 하는 단어의 첫글자와 동일하다면,, 나머지를 비교한다.
        # 이 때, keyword의 길이만큼 index 범위가 존재가능한 영역인지를 먼저 검사해야 한다. -> N-M+1로 하면 안해도 된다!!!